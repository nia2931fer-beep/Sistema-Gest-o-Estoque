# datetime permite pegar a data e a hora atuais para registrar no histórico.
from datetime import datetime

from dados import estoque, historico
from Cadastro import ler_inteiro
from consultar import exibir_produto


def ler_quantidade_movimento(mensagem):
    """Pede a quantidade de uma movimentação. Precisa ser maior que zero."""
    while True:
        quantidade = ler_inteiro(mensagem)
        if quantidade <= 0:
            # Mover zero ou número negativo não faz sentido.
            print("A quantidade deve ser maior que zero.")
        else:
            return quantidade


def registrar_movimentacao(codigo, tipo, quantidade):
    """Guarda uma movimentação no histórico."""
    # append() adiciona um item no final da lista.
    historico.append({
        # strftime formata a data/hora: dia/mês/ano hora:minuto
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "codigo": codigo,
        "nome": estoque[codigo]["nome"],
        "tipo": tipo,  # "ENTRADA" ou "SAÍDA"
        "quantidade": quantidade,
    })


def entrada_produto():
    """Registra a chegada de produtos, aumentando o estoque."""
    print("\n--- Entrada de produto ---")

    codigo = ler_inteiro("Código do produto: ")
    if codigo not in estoque:
        print("Produto não encontrado.")
        return

    exibir_produto(codigo, estoque[codigo])
    quantidade = ler_quantidade_movimento("Quantidade que entrou: ")

    # "+=" soma o valor na quantidade que já existe.
    estoque[codigo]["quantidade"] += quantidade
    registrar_movimentacao(codigo, "ENTRADA", quantidade)

    print(f"Entrada registrada! Novo estoque: {estoque[codigo]['quantidade']}")


def saida_produto():
    """Registra a saída de produtos, diminuindo o estoque."""
    print("\n--- Saída de produto ---")

    codigo = ler_inteiro("Código do produto: ")
    if codigo not in estoque:
        print("Produto não encontrado.")
        return

    exibir_produto(codigo, estoque[codigo])
    quantidade = ler_quantidade_movimento("Quantidade que saiu: ")

    # Requisito do projeto: não deixar sair mais do que existe no estoque.
    if quantidade > estoque[codigo]["quantidade"]:
        print("Saída negada! Quantidade maior que o estoque disponível.")
        return  # sai sem alterar nada

    # "-=" subtrai o valor da quantidade que já existe.
    estoque[codigo]["quantidade"] -= quantidade
    registrar_movimentacao(codigo, "SAÍDA", quantidade)

    print(f"Saída registrada! Novo estoque: {estoque[codigo]['quantidade']}")

    # Mensagem útil: avisa se o produto acabou.
    if estoque[codigo]["quantidade"] == 0:
        print("Atenção: o produto ficou SEM ESTOQUE.")


def mostrar_historico():
    """Mostra todas as movimentações feitas desde que o programa abriu."""
    print("\n--- Histórico de movimentações ---")

    if not historico:
        print("Nenhuma movimentação registrada.")
        return

    # Percorre a lista na ordem em que as movimentações aconteceram.
    for mov in historico:
        print(f"{mov['data_hora']} | {mov['tipo']} | "
              f"Cód {mov['codigo']} - {mov['nome']} | Qtd: {mov['quantidade']}")
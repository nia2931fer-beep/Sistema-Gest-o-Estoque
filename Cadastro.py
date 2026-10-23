# Importa o dicionário "estoque" do arquivo dados.py.
# Assim, este módulo guarda os produtos no mesmo lugar que os outros módulos.
from dados import estoque


def ler_inteiro(mensagem):
    """Pede um número inteiro ao usuário e repete até ele digitar certo."""
    while True:  # repete para sempre, até o "return" encerrar a função
        try:
            # input() devolve texto; int() tenta converter para número inteiro.
            # Se der certo, "return" devolve o número e a função termina.
            return int(input(mensagem))
        except ValueError:
            # Se o usuário digitar letras ou algo que não é inteiro,
            # o int() dá erro (ValueError) e cai aqui.
            print("Valor inválido. Digite um número inteiro.")


def ler_preco(mensagem):
    """Pede um preço ao usuário e só aceita valor maior que zero."""
    while True:
        try:
            # replace troca vírgula por ponto, para aceitar "3,50" e "3.50".
            # float() converte o texto em número decimal.
            preco = float(input(mensagem).replace(",", "."))

            if preco <= 0:
                # Número válido, mas não faz sentido um preço zero ou negativo.
                print("O preço deve ser maior que zero.")
            else:
                return preco  # preço válido: devolve e encerra a função
        except ValueError:
            # Entrou texto que não dá para converter em número.
            print("Valor inválido. Digite um número.")

def ler_quantidade(mensagem):
    """Pede uma quantidade inteira e só aceita zero ou mais."""
    while True:
        quantidade = ler_inteiro(mensagem)  # reaproveita a função que já valida inteiro
        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
        else:
            return quantidade

def cadastrar_produto():
    """Cadastra um novo produto no estoque, com todas as validações."""
    print("\n--- Cadastrar produto ---")

    # 1) Código: precisa ser inteiro e não pode já existir no estoque.
    codigo = ler_inteiro("Código (número): ")
    if codigo in estoque:  # "in" verifica se a chave já existe no dicionário
        print("Já existe um produto com esse código.")
        return  # sai da função sem cadastrar nada

    # 2) Nome e categoria: são textos.
    # strip() remove espaços sobrando no começo e no fim.
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()

    # 3) Preço: usa a função que já valida o valor.
    preco = ler_preco("Preço unitário: ")

    # 4) Quantidade: inteiro e não pode ser negativa.
    # Pode ser zero (produto cadastrado, mas sem estoque).
    quantidade = ler_quantidade("Quantidade disponível: ")
    
    # 5) Guarda o produto: a chave é o código e o valor é outro dicionário
    # com os dados do produto.
    estoque[codigo] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
    }
    print("Produto cadastrado com sucesso!")

    # Importa só a função que vamos usar do módulo cadastro.py.
from Cadastro import cadastrar_produto


def menu():
    """Mostra o menu e repete até o usuário escolher sair."""
    while True:  # mantém o menu funcionando até o "break"
        print("\n=== GESTÃO DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()  # chama a função do outro arquivo
        elif opcao == "0":
            print("Encerrando o sistema.")
            break  # quebra o while e encerra o menu
        else:
            # Qualquer outra coisa digitada cai aqui.
            print("Opção inválida.")


# Inicia o programa chamando a função do menu.
menu()
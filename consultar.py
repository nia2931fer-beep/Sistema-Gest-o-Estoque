# Importa o estoque (onde os produtos ficam guardados)
# e a função ler_inteiro, que já criamos no cadastro.py.
from dados import estoque
from Cadastro import ler_inteiro


def exibir_produto(codigo, produto):
    """Mostra os dados de UM produto na tela."""
    print(f"Código: {codigo}")
    print(f"  Nome: {produto['nome']}")
    print(f"  Categoria: {produto['categoria']}")
    # :.2f mostra o preço sempre com 2 casas decimais (ex.: 3.50)
    print(f"  Preço: R$ {produto['preco']:.2f}")
    print(f"  Quantidade: {produto['quantidade']}")

    # Requisito do projeto: identificar produtos com estoque zerado.
    if produto["quantidade"] == 0:
        print("  *** SEM ESTOQUE ***")
    print("-" * 30)  # linha separadora ("-" repetido 30 vezes)


def listar_produtos():
    """Mostra todos os produtos cadastrados."""
    print("\n--- Lista de produtos ---")

    # Dicionário vazio vale False, então "not estoque" é True quando não há nada.
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    # .items() devolve pares (chave, valor): aqui, (código, dados do produto).
    for codigo, produto in estoque.items():
        exibir_produto(codigo, produto)


def pesquisar_produtos():
    """Pesquisa produtos por código, nome ou categoria."""
    print("\n--- Pesquisar produto ---")
    print("1 - Por código")
    print("2 - Por nome")
    print("3 - Por categoria")
    opcao = input("Escolha: ")

    encontrou = False  # marcador: vira True se acharmos pelo menos um produto

    if opcao == "1":
        codigo = ler_inteiro("Digite o código: ")
        # O código é a chave do dicionário, então a busca é direta.
        if codigo in estoque:
            exibir_produto(codigo, estoque[codigo])
            encontrou = True

    elif opcao == "2":
        # lower() deixa tudo minúsculo, para "Arroz" e "arroz" serem iguais.
        texto = input("Digite o nome (ou parte dele): ").strip().lower()
        for codigo, produto in estoque.items():
            # "in" aqui verifica se o texto aparece dentro do nome.
            # Ex.: "arr" é encontrado em "arroz".
            if texto in produto["nome"].lower():
                exibir_produto(codigo, produto)
                encontrou = True

    elif opcao == "3":
        texto = input("Digite a categoria: ").strip().lower()
        for codigo, produto in estoque.items():
            if texto in produto["categoria"].lower():
                exibir_produto(codigo, produto)
                encontrou = True

    else:
        print("Opção inválida.")
        return  # sai sem mostrar a mensagem de "não encontrado"

    # Se o marcador continuou False, nada foi encontrado.
    if not encontrou:
        print("Nenhum produto encontrado.")
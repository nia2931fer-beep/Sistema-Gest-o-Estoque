# Importa o estoque e as funções de leitura com validação do cadastro.py.
from dados import estoque
from Cadastro import ler_inteiro, ler_preco, ler_quantidade
from consultar import exibir_produto


def atualizar_produto():
    """Altera um dado de um produto que já existe."""
    print("\n--- Atualizar produto ---")

    codigo = ler_inteiro("Código do produto: ")

    # Só dá para atualizar o que existe.
    if codigo not in estoque:
        print("Produto não encontrado.")
        return

    # Guardamos o produto numa variável para facilitar a escrita.
    # Como é um dicionário, mudar "produto" muda o que está no estoque.
    produto = estoque[codigo]
    exibir_produto(codigo, produto)  # mostra como está agora

    print("O que deseja atualizar?")
    print("1 - Nome")
    print("2 - Categoria")
    print("3 - Preço")
    print("4 - Quantidade")
    opcao = input("Escolha: ")

    if opcao == "1":
        produto["nome"] = input("Novo nome: ").strip()
    elif opcao == "2":
        produto["categoria"] = input("Nova categoria: ").strip()
    elif opcao == "3":
        produto["preco"] = ler_preco("Novo preço: ")
    elif opcao == "4":
        produto["quantidade"] = ler_quantidade("Nova quantidade: ")
    else:
        print("Opção inválida.")
        return  # sai sem mostrar a mensagem de sucesso

    print("Produto atualizado com sucesso!")
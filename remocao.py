# Importa o estoque e as funções que vamos reaproveitar.
from dados import estoque
from Cadastro import ler_inteiro
from consultar import exibir_produto


def remover_produto():
    """Remove um produto do estoque, pedindo confirmação antes."""
    print("\n--- Remover produto ---")

    codigo = ler_inteiro("Código do produto: ")

    if codigo not in estoque:
        print("Produto não encontrado.")
        return

    exibir_produto(codigo, estoque[codigo])  # mostra o que será apagado

    # Remover é uma ação sem volta, então confirmamos antes.
    # lower() aceita "S" e "s".
    confirmacao = input("Tem certeza que deseja remover? (s/n): ").strip().lower()

    if confirmacao == "s":
        del estoque[codigo]  # "del" apaga a chave (e o valor dela) do dicionário
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")
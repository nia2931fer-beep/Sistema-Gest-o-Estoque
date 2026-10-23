from dados import estoque
from Cadastro import ler_inteiro
from consultar import exibir_produto
 
 
def relatorio_geral():
    """Mostra valor total, total de unidades, produtos abaixo do limite e zerados."""
    print("\n--- Relatório do estoque ---")
 
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
 
    # O usuário define qual quantidade é considerada "estoque baixo".
    limite = ler_inteiro("Limite mínimo de estoque: ")
 
    valor_total = 0
    total_unidades = 0
    abaixo_do_limite = []  # lista de produtos com estoque baixo
    zerados = []           # lista de produtos sem estoque
 
    # Percorre todos os produtos acumulando os totais.
    for codigo, produto in estoque.items():
        # Valor armazenado = preço de uma unidade x quantidade disponível.
        valor_total += produto["preco"] * produto["quantidade"]
        total_unidades += produto["quantidade"]
 
        # Se está abaixo do limite, guardamos na lista.
        if produto["quantidade"] < limite:
            abaixo_do_limite.append((codigo, produto))
 
        # Se a quantidade é zero, guardamos na lista de zerados.
        if produto["quantidade"] == 0:
            zerados.append((codigo, produto))
 
    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Total de unidades: {total_unidades}")
 
    print(f"\nProdutos abaixo do limite ({limite}):")
    if not abaixo_do_limite:
        print("Nenhum produto abaixo do limite.")
    for codigo, produto in abaixo_do_limite:
        exibir_produto(codigo, produto)
 
    print("\nProdutos com estoque zerado:")
    if not zerados:
        print("Nenhum produto zerado.")
    for codigo, produto in zerados:
        exibir_produto(codigo, produto)
 
 
def ordenar_produtos():
    """Lista os produtos ordenados por nome, preço ou quantidade."""
    print("\n--- Ordenar produtos ---")
 
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
 
    print("1 - Por nome")
    print("2 - Por preço")
    print("3 - Por quantidade")
    opcao = input("Escolha: ")
 
    # sorted() devolve uma lista nova ordenada, sem mexer no estoque original.
    # O "key" diz pelo QUE ordenar. A "lambda" é uma mini-função sem nome:
    # recebe um item (código, produto) e devolve o campo usado na comparação.
    # item[1] é o produto (o dicionário com os dados).
    if opcao == "1":
        # lower() para "arroz" e "Arroz" ficarem juntos na ordem alfabética.
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["nome"].lower())
    elif opcao == "2":
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["preco"])
    elif opcao == "3":
        ordenados = sorted(estoque.items(), key=lambda item: item[1]["quantidade"])
    else:
        print("Opção inválida.")
        return
 
    for codigo, produto in ordenados:
        exibir_produto(codigo, produto)
 
 
def listar_por_categoria():
    """Lista os produtos agrupados por categoria, sem repetir a categoria."""
    print("\n--- Produtos por categoria ---")
 
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
 
    # set() guarda só valores únicos: se a categoria aparece 10 vezes,
    # ela entra uma vez só. É isso que evita repetir categorias.
    categorias = set()
    for produto in estoque.values():  # .values() dá só os dados, sem o código
        categorias.add(produto["categoria"])
 
    # sorted() coloca as categorias em ordem alfabética.
    for categoria in sorted(categorias):
        print(f"\n[{categoria}]")  # o título da categoria aparece uma vez
        # Mostra só os produtos que pertencem a essa categoria.
        for codigo, produto in estoque.items():
            if produto["categoria"] == categoria:
                exibir_produto(codigo, produto)
# Importa as funções de cada módulo.
from Cadastro import cadastrar_produto
from consultar import listar_produtos, pesquisar_produtos
from atualizacao import atualizar_produto
from remocao import remover_produto
from movimentacao import entrada_produto, saida_produto, mostrar_historico
from relatorio import relatorio_geral, ordenar_produtos, listar_por_categoria
 
 
def menu():
    """Mostra o menu e repete até o usuário escolher sair."""
    while True:
        print("\n=== GESTÃO DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("6 - Entrada de produto")
        print("7 - Saída de produto")
        print("8 - Histórico de movimentações")
        print("9 - Relatório do estoque")
        print("10 - Ordenar produtos")
        print("11 - Listar por categoria")
        print("0 - Sair")
        opcao = input("Escolha: ")
 
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produtos()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            entrada_produto()
        elif opcao == "7":
            saida_produto()
        elif opcao == "8":
            mostrar_historico()
        elif opcao == "9":
            relatorio_geral()
        elif opcao == "10":
            ordenar_produtos()
        elif opcao == "11":
            listar_por_categoria()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")
 
 
menu()
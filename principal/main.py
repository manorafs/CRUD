from bd import *
from usuarios import *
conecta_banco()
def menu_inicial():
    opcao = -1
    while opcao not in ["0","1","2","3","4"]:
        print("1- Listar usuários")
        print("2- Adicionar usuário")
        print("3- Atualizar usuário")
        print("4- Deletar usuários")
        print("0- Sair")
        opcao = input("Escolha uma opção: ").strip()
        print(opcao)
        match opcao :
            case  "0":
                print("Saindo...")
                exit()
            case  "1":
                listar_usuarios()
                return int(opcao)
            case  "2":
                adicionar_usuarios()
                return int(opcao)
            case  "3":
                atualizar_usuario()
                return int(opcao)      
            case  "4":
                deletar_usuario()
                return int(opcao)
        print("\nDigite uma opção válida!")      
menu_inicial()



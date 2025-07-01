from bd import *

def listar_usuarios():
    try:
        cur.execute("SELECT * FROM Usuario;")
        usuarios = cur.fetchall()
        print("          LISTANDO USUÁRIOS          ")
        print("--------------------------------------")
        for usuario in usuarios:
            
            print(f"ID: {usuario[0]} | {usuario[1]}")
    except Exception as e:
        print("Erro ao listar usuarios: ",e)
    finally:
        cur.close()
        conn.close()
def adicionar_usuarios():
    try:
        nome = input("Insira o seu usuário: ")
        senha = input("Insira sua senha: ")
        cur.execute("INSERT INTO Usuario (nome, senha_hash) VALUES (%s, %s)",(nome, senha))
        print(f"Usuário {nome} inserido com sucesso!")
        conn.commit()

    except Exception as e:
        print("Erro ao inserir no banco de dados",e)
    finally:
        cur.close()
        conn.close()
def atualizar_usuario():
    try:
        id_usuario_update = int(input("Insira o ID do usuário que quer atualizar."))
        choice_nome = input("Insira o novo nome: ")
        choice = input("Deseja atualizar a senha também? S ou N").lower()
        while choice not in ["s","n"]:
            choice = input("Resposta inválida, tente novamente: ").lower()
        if choice == "s":
            choice_senha = input("Insira a nova senha: ")
            sql = "UPDATE Usuario SET nome = %s, senha_hash = %s WHERE id = %s"
            valores = (choice_nome, choice_senha, id_usuario_update)
        else:
            sql = "UPDATE Usuario SET nome = %s WHERE id = %s"
            valores = (choice_nome, id_usuario_update)

        cur.execute(sql, valores)
        conn.commit()
        print("Usuário atualizado com sucesso!")
    except Exception as e:
        print("Não foi possível atualizar o usuario.")
    finally:
        cur.close()
        conn.close()
def deletar_usuario():
    try:
        id_a_deletar = input("Insira o ID do usuário que quer deletar: ")
        cur.execute("Select * from Usuario where id = %s",id_a_deletar)
        usuario = cur.fetchone()
        if usuario is None:
            print(f"Nenhum usuário encontrado com o ID: {id_a_deletar}")
            return
        else:
            delete = input(f"DESEJA MESMO DELETAR O USUÁRIO {usuario[1]}? (s ou n)").lower()
            if delete == "s":
                cur.execute("DELETE FROM Usuario WHERE id = %s",(id_a_deletar,))
                conn.commit()
                print(f"Usuário {usuario[1]} Deletado com sucesso!")
            else:
                print("Operação cancelada.")
                exit()
    except Exception as e:
        print("Erro inesperado ao excluir usuário, abortando operação.",e)
    finally:
        cur.close()
        conn.close()

        
        
from DB.config import engine, Base, session
from Models.usuario import Usuario
from Models.livro import Livro
from Models.emprestimo import Emprestimo
from sqlalchemy import DateTime
from datetime import datetime

Base.metadata.create_all(engine)

def cadastrar_usuario():
    nome = input("\nDigite seu nome: ")
    email = input("Digite seu email: ")
    novo_usuario = Usuario(nome=nome, email=email)
    session.add(novo_usuario)
    session.commit()
    print("Usuário adicionado com sucesso!")

def listar_usuarios():
    usuarios = session.query(Usuario).all()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

def excluir_usuario():
    id_usuario = input("Digite o ID do usuário a ser excluído: ")
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    verificar_emprestimo = session.query(Emprestimo).filter(Emprestimo.usuario_id == id_usuario).first()
    if verificar_emprestimo:
        print("Esse usuario ainda possui um emprestimo cadastrado!")
    
    elif usuario:
        session.delete(usuario)
        session.commit()
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario():
    id_usuario = input("Digite o ID do usuário a ser atualizado: ")
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if usuario:
        novo_nome = input("Digite o novo nome: ")
        novo_email = input("Digite o novo email: ")
        usuario.nome = novo_nome
        usuario.email = novo_email
        session.commit()
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def buscar_usuario():
    nome_usuario = input("Digite o nome do usuario que deseja buscar: ")
    usuario = session.query(Usuario).filter(Usuario.nome == nome_usuario).first()
    if usuario:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
    else:
        print("Usuário não encontrado.")

def cadastrar_livro():
        titulo = input("Digite o nome do livro: "), 
        autor = input("Digite o nome do autor: ")
        novo_livro = Livro(titulo=titulo, autor=autor)
        session.add(novo_livro)  
        session.commit()  
        print("Livro adicionado com sucesso")

def listar_livros():
    livros = session.query(Livro).all()
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}")

def excluir_livro():
    id_livro = input("Digite o ID do livro que deseja excluir: ")
    livro = session.query(Livro).filter(Livro.id == id_livro).first()
    if livro:
        session.delete(livro)
        session.commit()
        print("Livro excluído com sucesso!")
    else:
        print("Livro não encontrado.")

def atualizar_livro():
    id_livro = input("Digite o ID do livro que deseja atualizar: ")
    livro = session.query(Livro).filter(Livro.id == id_livro).first()
    if livro:
        novo_titulo = input("Digite o novo título: ")
        novo_autor = input("Digite o novo autor: ")
        livro.titulo = novo_titulo
        livro.autor = novo_autor
        session.commit()
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.")

def buscar_livro():
    titulo_livro = input("Digite o título do livro que deseja buscar: ")
    livro = session.query(Livro).filter(Livro.titulo == titulo_livro).first()
    if livro:
        print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}")
    else:
        print("Livro não encontrado.")

def cadastrar_emprestimo():
    nome_usuario = input("Digite o nome do usuario: ")
    nome_livro = input("Digite o nome do livro que será emprestado: ")
    usuario = session.query(Usuario).filter(Usuario.nome == nome_usuario).first()
    if not usuario:
        print("Usuario não encontrado")
        return
    livro = session.query(Livro).filter(Livro.titulo == nome_livro).first()
    if not livro:
        print("Livro não encontrado")
        return
    novo_emprestimo = Emprestimo(
        usuario_id=usuario.id, livro_id=livro.id, data_emprestimo=datetime.now(), data_devolucao = None)
    session.add(novo_emprestimo)
    session.commit()
    print("Emprestimo cadastrado com sucesso")

def listar_emprestimos():
    resultado = (session.query(Emprestimo.id, Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo, Emprestimo.data_devolucao).join(Emprestimo, Usuario.id == Emprestimo.usuario_id).join(Livro, Livro.id == Emprestimo.livro_id).all())
    if not resultado:
        print("Nenhum emprestimo cadastrado")
    else:
        for id, nome, titulo, data_emprestimo, data_devolucao in resultado:
            devolucao = "Não devolvido" if data_devolucao is None else data_devolucao
            print (f'ID: {id} , Nome do usuario: "{nome}", Nome do livro emprestado: "{titulo}", Data do emprestimo: "{data_emprestimo}", Devolucao do emprestimo: {devolucao}')
        
def excluir_emprestimo():
    id_emprestimo = input("Digite o ID do emprestimo que deseja excluir: ")
    emprestimo = session.query(Emprestimo).filter(Emprestimo.id == id_emprestimo).first()
    if emprestimo:
        session.delete(emprestimo)
        session.commit()
        print("Emprestimo excluido com sucesso")
    else:
        print("Emprestimo não encontrado")

def checar_emprestimo_usuario():
    nome = input("Digite o nome do usuario que deseja ver os emprestimos: ")
    usuario = session.query(Usuario).filter(Usuario.nome == nome).first()

    emprestimo = session.query(
        Emprestimo.id, Usuario.nome, Livro.titulo, Emprestimo.data_emprestimo).join(
        Emprestimo, Usuario.id == Emprestimo.usuario_id).join(
        Livro, Livro.id == Emprestimo.livro_id).all()
    
    if usuario == emprestimo:
        for emprestimos in emprestimo:
            print(f"ID:{Emprestimo.id}, Nome:{Usuario.nome}, Livro: {Livro.titulo}, Data do emprestimo:{Emprestimo.data_emprestimo}")
    else:
        print("Não encontrado emprestimos para esse usuario")
    

def cadastrar_data_devolucao():
    id = input("Digite o ID do emprestimo que deseja finalizar")
    emprestimo = session.query(Emprestimo).filter(Emprestimo.id == id).first()
    if emprestimo:
        data_devolucao = datetime.now()
        emprestimo.data_devolucao = data_devolucao
        session.commit()
        print("Emprestimo finalizado com sucesso")
    else:
        print("Emprestimo não encontrado")



while True:
    print("\nMenu de Opções:")
    print("\n1 - Cadastrar novo usuario\n"
        "2 - Listar usuarios\n"
        "3 - Excluir usuario\n"
        "4 - Atualizar usuario\n"
        "5 - Buscar usuario\n"
        "\n6 - Cadastrar novo livro\n"
        "7 - Listar livros\n"
        "8 - Excluir livro\n"
        "9 - Atualizar livro\n"
        "10 - Buscar livro\n"
        "\n11 - Cadastrar novo emprestimo\n"
        "12 - Verificar todos os emprestimo\n"
        "13 - Excluir um emprestimo\n"
        "14 - Chegar emprestimo por usuario\n"
        "15 - Devolução de emprestimo\n"
        "\n0 - Sair do programa\n"
        )
    
    opcao = (input("Digite a opção desejada: "))
    if opcao == "":
        print("Opção inválida. Tente novamente.")
        continue

    match opcao:
    
        case "1":
            cadastrar_usuario()
        case "2":
            listar_usuarios()
        case "3":
            excluir_usuario()
        case "4":
            atualizar_usuario()
        case "5":
            buscar_usuario()
        case "6":
            cadastrar_livro()
        case "7":
            listar_livros()
        case "8":
            excluir_livro()
        case "9":
            atualizar_livro()
        case "10":
            buscar_livro()
        case "11":
            cadastrar_emprestimo()
        case "12":
            listar_emprestimos()
        case "13":
            excluir_emprestimo()
        case "14":
            checar_emprestimo_usuario()
        case "15":
            cadastrar_data_devolucao()
        case "0":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")

                    





            
        
    
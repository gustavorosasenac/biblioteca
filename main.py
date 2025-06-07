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
    id_usuario = int(input("Digite o ID do usuário a ser excluído: "))
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario():
    id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
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
    id_livro = int(input("Digite o ID do livro que deseja excluir: "))
    livro = session.query(Livro).filter(Livro.id == id_livro).first()
    if livro:
        session.delete(livro)
        session.commit()
        print("Livro excluído com sucesso!")
    else:
        print("Livro não encontrado.")

def atualizar_livro():
    id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
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
    data_emprestimo = DateTime
    usuario = session.query(Usuario).filter(Usuario.nome == nome_usuario).first()
    if not usuario:
        print("Usuario não encontrado")
        return
    livro = session.query(Livro).filter(Livro.titulo == nome_livro).first()
    if not livro:
        print("Livro não encontrado")
        return
    novo_emprestimo = Emprestimo(
        usuario_id=usuario.id, livro_id=livro.id, data_emprestimo=datetime.now()
    )
    session.add(novo_emprestimo)
    session.commit()
    print("Emprestimo cadastrado com sucesso")

def listar_emprestimos():
    emprestimos = session.query(Emprestimo).all()
    
    if not Emprestimo:
        print("Nenhum emprestimo cadastrado")
    else:
        for emprestimo in emprestimos:
            print(f"ID: {emprestimo.id}, Nome do usuario:{}, Nome do livro emprestado:{}, Data do emprestimo:{}, Devolucao do emprestimo:{} ")
def excluir_emprestimo():
    pass

def checar_emprestimo_usuario():
    pass

def cadastrar_data_devolucao():
    pass




while True:
    print("\nMenu de Opções:")
    print("1 - Cadastrar novo Usuario\n"
        "2 - Listar usuarios\n"
        "3 - Excluir usuario\n"
        "4 - Atualizar usuario\n"
        "5 - Buscar usuario\n"
        "6 - Cadastrar novo Livro\n"
        "7 - Listar livros\n"
        "8 - Excluir livro\n"
        "9 - Atualizar livro\n"
        "10 - Buscar livro\n"
        "11 - Cadastrar novo emprestimo\n"
        "12 - Verificar todos os emprestimo\n"
        "13 - Excluir um emprestimo\n"
        "14 - Editar um emprestimo\n"
        "15 - Devolução de emprestimo\n"
        "0 - Sair do programa\n"
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
        case "0":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")

            aaa
        





            
        
    
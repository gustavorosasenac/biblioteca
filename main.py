from DB.config import engine, Base, session
from Models.usuario import Usuario
from Models.livro import Livro

Base.metadata.create_all(engine)

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    novo_usuario = Usuario(nome=nome, email=email)
    session.add(novo_usuario)
    session.commit()
    print("Usuário adicionado com sucesso!")

def listar_usuarios():
    pass

def excluir_usuario():
    pass

def atualizar_usuario():
    pass

def buscar_usuario():
    pass

def cadastrar_livro():
        titulo = input("Digite O nome do livro: "), 
        autor = input("Digite o nome do autor: ")
        novo_livro = Livro(titulo=titulo, autor=autor)
        session.add(novo_livro)  
        session.commit()  
        print("Livro adicionado com sucesso")

def listar_livros():
    pass

def excluir_livro():
    pass

def atualizar_livro():
    pass

def buscar_livro():
    pass
    





























while True:
    print("Menu de Opções")
    print("1 - Cadastrar novo Usuario")
    print("2 - Cadastrar novo Livro")
    opcao = (int(input("Digite a opção desejada: ")))

    match opcao:
        case 1:
            cadastrar_usuario()
            
        case 2:
            cadastrar_livro()
           



        case _:
            print("Opção inválida, tente novamente.")




            
        
    
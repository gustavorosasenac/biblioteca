while True:
    print("Menu de Opções")
    print("1 - Cadastrar novo Usuario")
    print("2 - Cadastrar novo Livro")
    opcao = (int(input("Digite a opção desejada: ")))

    match opcao:
        case 1:
            from Models.usuario import Usuario
            Usuario.cadastrar_usuario()
            
        case 2:
            from Models.livro import Livro
            Livro.cadastrar_livro()
           



        case _:
            print("Opção inválida, tente novamente.")
            
        
    
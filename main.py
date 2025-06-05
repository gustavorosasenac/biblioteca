while True:
    print("Menu de Opções")
    print("1 - Cadastrar Usuario")
    print("2 - Opção 2")
    opcao = (int(input("Digite a opção desejada: ")))

    match opcao:
        case 1:
            from Models.usuario import Usuario
            Usuario.cadastrar_usuario()
            break
        case 2:
            pass



        case _:
            print("Opção inválida, tente novamente.")
            
        
    
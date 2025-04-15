def exibir_menu():
    while True:
        print("\n=== Plataforma de Educação Digital ===")
        print("1. Ver conteúdo")
        print("2. Fazer exercício")
        print("3. Ver desempenho")
        print("0. Sair")

        opcão =input("EScolha uma opção: ")

        if opcão == "1":
            print(">>> Conteúdo ainda não disponivel.")
        elif opcão == "2":
            print(">>> Exercício em desenvolvimento...")
        elif opcão == "3":
            print(">>> Estatísticas em construção.")
        elif opcão == "0":
            print(">>> Saindo... Até logo!")
            break
        else:
            print(">>> Opção inválida. Tente novamente.")
        
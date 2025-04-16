from utils.helpers import carregar_usuarios, salvar_usuarios

def criar_usuario():
    usuarios = carregar_usuarios()

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    novo ={
        "id": len(usuarios) + 1,
        "nome": nome,
        "idade": idade,
        "pontuacoes": [],
        "tempo_uso": 0
    }

    usuarios.append(novo)
    salvar_usuarios(usuarios)
    print("✅ Usuário criado com sucesso!")


def listar_usuarios():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário encontrado.")
    else:
        print("📋 Lista de usuários:")
        for u in usuarios:
            print(f"{u['id']}: {u['nome']} ({u['idade']} anos)")


def editar_usuario():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return

    print("📋 Lista de usuários:")
    for u in usuarios:
        print(f"{u['id']}: {u['nome']} ({u['idade']} anos)")

    try:
        id_a_editar = int(input("Digite o ID que planeja editar: "))
    except ValueError:
        print("⚠️ ID inválido. Digite um número.")
        return
    
    for u in usuarios:
        if u['id'] == id_a_editar:
            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))

            u['nome'] = novo_nome
            u['idade'] = nova_idade

            salvar_usuarios(usuarios)
            print("✅ Usuário editado com sucesso!")
            return

    print("⚠️ Nenhum usuário com esse ID foi encontrado.")


def excluir_usuario():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return 
    
    print("📋 Lista de usuários:")
    for u in usuarios:
        print(f"{u['id']}: {u['nome']} ({u['idade']} anos)")
    
    try:
        id_a_excluir = int(input("Digite o ID que planeja excluir: "))
    except ValueError:
        print("⚠️ ID inválido. Digite um número.")
        return
    
    nova_lista = [u for u in usuarios if u['id'] != id_a_excluir]


    if len(nova_lista) == len(usuarios):
        print("⚠️ Nenhum usuário com esse ID foi encontrado.")
    else:
        salvar_usuarios(nova_lista)
        print("✅ Usuário excluído com sucesso!")




def exibir_menu():
    while True:
        print("\n=== Plataforma de Educação Digital ===")
        print("1. Ver conteúdo")
        print("2. Fazer exercício")
        print("3. Ver desempenho")
        print("4. Cadastrar novo usuário")
        print("5. Listar usuários")
        print("6. Editar usuário")
        print("7. Excluir usuário"  )
        print("0. Sair")

        opcao =input("EScolha uma opção: ")

        if opcao == "1":
            print(">>> Conteúdo ainda não disponivel.")
        elif opcao == "2":
            print(">>> Exercício em desenvolvimento...")
        elif opcao == "3":
            print(">>> Estatísticas em construção.")
        elif opcao == "4":
            criar_usuario()
        elif opcao == "5":
            listar_usuarios()
        elif opcao == "6":
            editar_usuario()
        elif opcao == "7":
            excluir_usuario()
        elif opcao == "0":
            print(">>> Saindo... Até logo!")
            break
        else:
            print(">>> Opção inválida. Tente novamente.")
        
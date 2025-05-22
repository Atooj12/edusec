from estatisticas import calcular_media, calcular_moda, calcular_mediana
from utils.cripto.cripto import criptografar, descriptografar
from utils.helpers import carregar_usuarios, salvar_usuarios
from exercicios import fazer_exercicio
from colorama import init, Fore, Style

init(autoreset=True)

VERDE = Fore.GREEN
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
AZUL = Fore.CYAN
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL 

def criar_usuario():
    usuarios = carregar_usuarios()

    nome = input(NEGRITO + "Nome: ")
    idade = int(input(NEGRITO + "Idade: "))

    proximo_id = max([u["id"] for u in usuarios], default=0) + 1

    novo = {
        "id": proximo_id,
        "nome": criptografar(nome),
        "idade": criptografar(str(idade)),
        "pontuacoes": [],
        "tempo_uso": 0
    }

    usuarios.append(novo)
    salvar_usuarios(usuarios)
    print(VERDE + "✅ Usuário criado com sucesso!")


def listar_usuarios():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
    else:
        print(NEGRITO + "📋 Lista de usuários:")
        for u in usuarios:
            total = sum(u['pontuacoes'])
            print(f"{u['id']}: {descriptografar(u['nome'])} ({descriptografar(u['idade'])} anos) - Total de pontos: {total}")


def editar_usuario():
    usuarios = carregar_usuarios()
    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return

    print(NEGRITO + "📋 Lista de usuários:")
    for u in usuarios:
        total = sum(u['pontuacoes'])
        print(f"{u['id']}: {descriptografar(u['nome'])} ({descriptografar(u['idade'])} anos) - Total de pontos: {total}")
    try:
        id_a_editar = int(input(NEGRITO + "Digite o ID que planeja editar: "))
    except ValueError:
        print(VERMELHO + "⚠️ ID inválido. Digite um número.")
        return
    
    for u in usuarios:
        if u['id'] == id_a_editar:
            novo_nome = input(NEGRITO + "Digite o novo nome: ")
            nova_idade = int(input(NEGRITO + "Digite a nova idade: "))
            u['nome'] = criptografar(novo_nome)
            u['idade'] = criptografar(str(nova_idade))

            salvar_usuarios(usuarios)
            print(VERDE + "✅ Usuário editado com sucesso!")
            return

    print(VERMELHO + "⚠️ Nenhum usuário com esse ID foi encontrado.")


def excluir_usuario():
    usuarios = carregar_usuarios()
    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return 
    
    print(NEGRITO + "📋 Lista de usuários:")
    for u in usuarios:
        total = sum(u['pontuacoes'])
        print(f"{u['id']}: {descriptografar(u['nome'])} ({descriptografar(u['idade'])} anos) - Total de pontos: {total}")
    
    try:
        id_a_excluir = int(input(NEGRITO + "Digite o ID que planeja excluir: "))
    except ValueError:
        print(VERMELHO + "⚠️ ID inválido. Digite um número.")
        return
    
    nova_lista = [u for u in usuarios if u['id'] != id_a_excluir]


    if len(nova_lista) == len(usuarios):
        print(VERMELHO + "⚠️ Nenhum usuário com esse ID foi encontrado.")
    else:
        salvar_usuarios(nova_lista)
        print(VERMELHO + "✅ Usuário excluído com sucesso!")


def desempenho_geral():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return
    
    print(NEGRITO + "\n📊 DESEMPENHO GERAL DOS USUÁRIOS 📊")

    total_pontos_geral = 0
    total_exercicios_geral = 0
    total_tempo_geral = 0
    usuarios_ativos = 0

    for u in usuarios:
        pontos = sum(u["pontuacoes"])
        exercicios = len(u["pontuacoes"])
        tempo = u["tempo_uso"]

        print(f"\n🧑 {descriptografar(u['nome'])}:")
        print(f"Idade: {descriptografar(u['idade'])}")
        print(f"Pontos: {pontos}")
        print(f"Exercícios feitos: {exercicios}")
        print(f"Tempo total de uso: {tempo} segundos")

        if exercicios > 0:
            usuarios_ativos += 1
            total_pontos_geral += pontos
            total_exercicios_geral += exercicios
            total_tempo_geral += tempo

    if usuarios_ativos == 0:
        print(AMARELO + "\nNenhum usuário respondeu exercícios ainda.")
        return
   
    media_pontos = total_pontos_geral / usuarios_ativos
    media_exercicios = total_exercicios_geral / usuarios_ativos
    media_tempo = total_tempo_geral / usuarios_ativos

    print(NEGRITO + "\n📈 MÉDIAS GERAIS DA TURMA 📈")
    print(f"Média de pontos por usuário: {media_pontos:.2f}")
    print(f"Média de exercícios por usuário: {media_exercicios:.2f}")
    print(f"Média de tempo de uso: {media_tempo:.2f} segundos")

def desempenho_individual(usuario_id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)

    if not usuario:
        print(VERMELHO + "Usuário não encontrado.")
        return

    print(NEGRITO + "\n🧾 Perfil do Usuário")
    print(f"ID: {usuario['id']}")
    print(f"Nome: {descriptografar(usuario['nome'])}")
    print(f"Idade: {descriptografar(usuario['idade'])}")
    print(f"Pontuações: {usuario['pontuacoes']}")
    print(f"Total de pontos: {sum(usuario['pontuacoes'])}")
    print(f"Tempo total de uso: {usuario['tempo_uso']} segundos")

def desempenho_geral_especifico():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return
    
    print(NEGRITO + "\n📊 DESEMPENHO GERAL ESPECIFICA DOS USUÁRIOS 📊")

    total_pontos_geral = 0
    total_exercicios_geral = 0
    total_tempo_geral = 0
    usuarios_ativos = 0

    for u in usuarios:
        pontos = sum(u["pontuacoes"])
        exercicios = len(u["pontuacoes"])
        tempo = u["tempo_uso"]

        print(f"\n🧑 {descriptografar(u['nome'])}:")
        print(f"Idade: {descriptografar(u['idade'])}")
        print(f"Pontos: {pontos}")
        print(f"Exercícios feitos: {exercicios}")
        print(f"Tempo total de uso: {tempo} segundos")

        if exercicios > 0:
            usuarios_ativos += 1
            total_pontos_geral += pontos
            total_exercicios_geral += exercicios
            total_tempo_geral += tempo

    if usuarios_ativos == 0:
        print(AMARELO + "\nNenhum usuário respondeu exercícios ainda.")
        return
       
    print(NEGRITO + "\n📈 MÉDIAS GERAIS ESPECIFICOS DA TURMA 📈")
    idades = [u["idade"] for u in usuarios]
    pontos = [sum(u["pontuacoes"]) for u in usuarios]
    exercicios = [len(u["pontuacoes"]) for u in usuarios]
    tempo = [u["tempo_uso"] for u in usuarios]
    print(NEGRITO + f"\n📊 Idades dos usuários:")
    print(f"Média: {calcular_media(idades):.2f}")
    print(f"Moda: {calcular_moda(idades)}")
    print(f"Mediana: {calcular_mediana(idades)}")
    print(NEGRITO + f"\n📊 Pontos dos usuários:")
    print(f"Média: {calcular_media(pontos):.2f}")
    print(f"Moda: {calcular_moda(pontos)}")
    print(f"Mediana: {calcular_mediana(pontos)}")
    print(NEGRITO + f"\n📊 Exercicios dos usuários:")
    print(f"Média: {calcular_media(exercicios):.2f}")
    print(f"Moda: {calcular_moda(exercicios)}")
    print(f"Mediana: {calcular_mediana(exercicios)}")
    print(NEGRITO + f"\n📊 Tempo dos usuários:")
    print(f"Média: {calcular_media(tempo):.2f}")
    print(f"Moda: {calcular_moda(tempo)}")
    print(f"Mediana: {calcular_mediana(tempo)}")


def ranking_de_usuarios_ponto():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return

    ranking = [
        {
            "nome": u["nome"],
            "pontos": sum(u["pontuacoes"]),
            "exercicios": u["pontuacoes"],
            "tempo_uso": u["tempo_uso"]
        }
        for u in usuarios
    ]
    
    ranking_ordenado = sorted(ranking, key=lambda x: x["pontos"], reverse=True)

    print(NEGRITO + "\n🏆 RANKING DOS USUÁRIOS POR PONTOS 🏆")
    for i, user in enumerate(ranking_ordenado[:10], start=1):
        print(f"{i}º lugar: {descriptografar(user['nome'])} - {user['pontos']} ponto(s) - {user['exercicios']} quant(s) de exercicios - {user['tempo_uso']} tempo de uso")


def ranking_de_usuarios_exercicio():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return
        
    ranking = [
        {
            "nome": u["nome"],
            "pontos": sum(u["pontuacoes"]),
            "exercicios": u["pontuacoes"],
            "tempo_uso": u["tempo_uso"]
        }
        for u in usuarios
    ]

    ranking_ordenado = sorted(ranking, key=lambda x: x["exercicios"], reverse=True)

    print(NEGRITO + "\n🏆 RANKING DOS USUÁRIOS POR EXERCICIOS 🏆")
    for i, user in enumerate(ranking_ordenado[:10], start=1):
        print(f"{i}º lugar: {descriptografar(user['nome'])} - {user['exercicios']} quant(s) de exercicios - {user['pontos']} ponto(s) - {user['exercicios']} quant(s) de exercicios - {user['tempo_uso']} tempo de uso")


def ranking_de_usuarios_tempo():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado.")
        return
        
    ranking = [
        {
            "nome": u["nome"],
            "pontos": sum(u["pontuacoes"]),
            "exercicios": u["pontuacoes"],
            "tempo_uso": u["tempo_uso"]
        }
        for u in usuarios
    ]

    ranking_ordenado = sorted(ranking, key=lambda x: x["tempo_uso"])

    print(NEGRITO + "\n🏆 RANKING DOS USUÁRIOS POR TEMPO 🏆")
    for i, user in enumerate(ranking_ordenado[:10], start=1):
        print(f"{i}º lugar: {descriptografar(user['nome'])} - {user['tempo_uso']} tempo de uso - {user['pontos']} ponto(s) - {user['exercicios']} quant(s) de exercicios")

def ver_conteudo():
    print(NEGRITO + "\n📘 CONTEÚDO EDUCATIVO")
    print(AZUL + """
    1. Lógica de Programação:
       - Um algoritmo é uma sequência de passos para resolver um problema.
       - Variáveis armazenam dados.
       - Condições (if/else) e loops (for/while) controlam o fluxo.

    2. Python Básico:
       - Tipos: int, str, float, bool
       - Funções são criadas com def
       - Listas guardam vários valores

    3. Segurança Digital:
       - Use senhas fortes e únicas
       - Não compartilhe dados pessoais
       - Cuidado com links suspeitos
    """)


def sobre():
    print(NEGRITO + "\n📄 SOBRE O SISTEMA")
    print(AZUL + """
    Este sistema foi desenvolvido como parte do Projeto Integrado Multidisciplinar (PIM)
    do curso de Análise e Desenvolvimento de Sistemas da UNIP - 2025/1.

    Objetivo:
    - Ensinar lógica de programação de forma acessível
    - Promover segurança digital
    - Respeitar os princípios da LGPD

    Desenvolvido em:
    - Python 3
    - Execução via terminal
    - Armazenamento em JSON
    - Cores com Colorama
        """)

def exibir_menu():
    while True:
        print(NEGRITO + "\n=== Plataforma de Educação Digital ===")
        print("1. Ver conteúdo")
        print("2. Fazer exercício")
        print("3. Ver desempenho")
        print("4. Cadastrar novo usuário")
        print("5. Listar usuários")
        print("6. Editar usuário")
        print("7. Excluir usuário")
        print("8. Sobre o sistema")
        print("9. Ver ranking dos usuários")
        print("0. Sair")

        opcao =input(NEGRITO + "Escolha uma opção: ")

        if opcao == "1":
            ver_conteudo()
        elif opcao == "2":
            listar_usuarios()

            try:
                id_usuario = int(input(NEGRITO + "Digite o ID do usuário que vai fazer o exercício: "))
            except ValueError:
                print(VERMELHO + "⚠️ ID inválido. Digite um número.")
                return

            fazer_exercicio(id_usuario)
        elif opcao == "3":
            print(NORMAL + "1. Desempenho Geral")
            print("2. Desempenho Geral Especifico")
            print("3. Desempenho individual")
            opcaodes = input(NEGRITO + "Digite a opção que planeja prosseguir: ")
            if opcaodes == "1":
                desempenho_geral()
            elif opcaodes == "2":
                desempenho_geral_especifico()
            elif opcaodes == "3":
                listar_usuarios()
                try:
                    id_usuario = int(input(NEGRITO + "Digite o ID do usuário para ver o perfil: "))
                    desempenho_individual(id_usuario)
                except ValueError:
                    print(VERMELHO + "⚠️ ID inválido. Digite um número.")
            else:
                print(AMARELO + ">>> Opção inválida. Tente novamente.")
        elif opcao == "4":
            criar_usuario()
        elif opcao == "5":
            listar_usuarios()
        elif opcao == "6":
            editar_usuario()
        elif opcao == "7":
            excluir_usuario()
        elif opcao == "8":
            sobre()
        elif opcao == "9":
            print(NORMAL + "1. Ranking por pontos")
            print("2. Ranking por exercicios")
            print("3. Ranking por tempo")
            opcaoRank = input(NEGRITO + "Digite a opção que planeja prosseguir: ")            
            if opcaoRank == "1":
                ranking_de_usuarios_ponto()
            elif opcaoRank == "2":
                ranking_de_usuarios_exercicio()
            elif opcaoRank == "3":
                ranking_de_usuarios_tempo()
            else:
                print(AMARELO + ">>> Opção inválida. Tente novamente.")
        elif opcao == "0":
            print(VERDE + ">>> Saindo... Até logo!")
            break
        else:
            print(AMARELO +">>> Opção inválida. Tente novamente.")
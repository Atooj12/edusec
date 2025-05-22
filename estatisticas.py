from utils.cripto.cripto import descriptografar
from utils.helpers import carregar_usuarios
from statistics import mode, median
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Cores
AZUL = Fore.CYAN
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL


def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0


def calcular_moda(lista):
    try:
        return mode(lista)
    except:
        return "Sem moda"


def calcular_mediana(lista):
    return median(lista) if lista else 0


def desempenho_geral():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    print(NEGRITO + AZUL + "\n📊 DESEMPENHO GERAL DOS USUÁRIOS 📊" + NORMAL)

    for u in usuarios:
        pontos = sum(u["pontuacoes"])
        exercicios = len(u["pontuacoes"])
        tempo = u["tempo_uso"]

        print(f"\n🧑 {descriptografar(u['nome'])}:")
        print(f"Idade: {descriptografar(u['idade'])}")
        print(f"Pontos: {pontos}")
        print(f"Exercícios feitos: {exercicios}")
        print(f"Tempo total de uso: {tempo} segundos")


def desempenho_detalhado():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    idades = [int(descriptografar(u["idade"])) for u in usuarios]
    pontos = [sum(u["pontuacoes"]) for u in usuarios]
    exercicios = [len(u["pontuacoes"]) for u in usuarios]
    tempo = [u["tempo_uso"] for u in usuarios]

    print(NEGRITO + AZUL + "\n📈 ESTATÍSTICAS DETALHADAS DA TURMA 📈" + NORMAL)

    print(NEGRITO + f"\n📊 Idades dos usuários:" + NORMAL)
    print(f"Média: {calcular_media(idades):.2f}")
    print(f"Moda: {calcular_moda(idades)}")
    print(f"Mediana: {calcular_mediana(idades)}")

    print(NEGRITO + f"\n📊 Pontos dos usuários:" + NORMAL)
    print(f"Média: {calcular_media(pontos):.2f}")
    print(f"Moda: {calcular_moda(pontos)}")
    print(f"Mediana: {calcular_mediana(pontos)}")

    print(NEGRITO + f"\n📊 Exercícios dos usuários:" + NORMAL)
    print(f"Média: {calcular_media(exercicios):.2f}")
    print(f"Moda: {calcular_moda(exercicios)}")
    print(f"Mediana: {calcular_mediana(exercicios)}")

    print(NEGRITO + f"\n📊 Tempo dos usuários:" + NORMAL)
    print(f"Média: {calcular_media(tempo):.2f}")
    print(f"Moda: {calcular_moda(tempo)}")
    print(f"Mediana: {calcular_mediana(tempo)}")


def desempenho_individual():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    for u in usuarios:
        print(f"{u['id']}: {descriptografar(u['nome'])}")

    try:
        id_usuario = int(input(NEGRITO + AMARELO + "Digite o ID do usuário para ver o perfil: " + NORMAL))
    except ValueError:
        print(VERMELHO + "⚠️ ID inválido. Digite um número." + NORMAL)
        return

    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)

    if not usuario:
        print(VERMELHO + "⚠️ Usuário não encontrado." + NORMAL)
        return

    print(NEGRITO + "\n🧾 PERFIL DO USUÁRIO" + NORMAL)
    print(f"ID: {usuario['id']}")
    print(f"Nome: {descriptografar(usuario['nome'])}")
    print(f"Idade: {descriptografar(usuario['idade'])}")
    print(f"Pontuações: {usuario['pontuacoes']}")
    print(f"Total de pontos: {sum(usuario['pontuacoes'])}")
    print(f"Total de exercícios: {len(usuario['pontuacoes'])}")
    print(f"Tempo total de uso: {usuario['tempo_uso']} segundos")


def ranking_usuarios(tipo):
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    ranking = [
        {
            "nome": descriptografar(u["nome"]),
            "pontos": sum(u["pontuacoes"]),
            "exercicios": len(u["pontuacoes"]),
            "tempo_uso": u["tempo_uso"]
        }
        for u in usuarios
    ]

    if tipo == "pontos":
        ranking_ordenado = sorted(ranking, key=lambda x: x["pontos"], reverse=True)
        print(NEGRITO + AZUL + "\n🏆 RANKING POR PONTOS 🏆" + NORMAL)
    elif tipo == "exercicios":
        ranking_ordenado = sorted(ranking, key=lambda x: x["exercicios"], reverse=True)
        print(NEGRITO + AZUL + "\n🏆 RANKING POR EXERCÍCIOS 🏆" + NORMAL)
    elif tipo == "tempo":
        ranking_ordenado = sorted(ranking, key=lambda x: x["tempo_uso"])
        print(NEGRITO + AZUL + "\n🏆 RANKING POR TEMPO 🏆" + NORMAL)
    else:
        print(AMARELO + ">>> Opção inválida." + NORMAL)
        return

    for i, user in enumerate(ranking_ordenado, start=1):
        print(f"{i}º lugar: {user['nome']} - {user['pontos']} pontos - {user['exercicios']} exercícios - {user['tempo_uso']} segundos")

import time
import random
from utils.cripto.cripto import descriptografar
from utils.helpers import carregar_usuarios, salvar_usuarios, carregar_perguntas
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Cores
AZUL = Fore.CYAN
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
VERDE = Fore.GREEN
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL


def escolher_tema():
    perguntas = carregar_perguntas()

    if not perguntas:
        print(VERMELHO + "⚠️ Nenhuma pergunta encontrada. Verifique o arquivo perguntas.json." + NORMAL)
        return "Misto"

    print(NEGRITO + AZUL + "\n=== Escolha um tema ===" + NORMAL)
    temas = list(perguntas.keys())

    for i, tema in enumerate(temas, 1):
        print(f"{i}. {tema}")

    print(f"{len(temas) + 1}. Quiz Misto (todas as áreas)")

    try:
        escolha = int(input(NEGRITO + AMARELO + "Digite o número do tema: " + NORMAL))
        if escolha == len(temas) + 1:
            return "Misto"
        elif 1 <= escolha <= len(temas):
            return temas[escolha - 1]
        else:
            print(VERMELHO + "❌ Opção inválida. Escolhendo Misto por padrão." + NORMAL)
            return "Misto"
    except ValueError:
        print(VERMELHO + "❌ Opção inválida. Escolhendo Misto por padrão." + NORMAL)
        return "Misto"


def fazer_exercicio(usuario_id):
    perguntas = carregar_perguntas()

    if not perguntas:
        print(VERMELHO + "⚠️ Nenhuma pergunta encontrada. Verifique o arquivo perguntas.json." + NORMAL)
        return

    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)

    if not usuario:
        print(VERMELHO + "Usuário não encontrado." + NORMAL)
        return

    nome = descriptografar(usuario['nome'])
    print(NEGRITO + f"\n👋 Olá, {nome}! Vamos começar os exercícios...\n" + NORMAL)

    tema = escolher_tema()
    acertos = 0
    inicio = time.time()

    if tema == "Misto":
        todas_perguntas = []
        for lista in perguntas.values():
            todas_perguntas.extend(lista)
        perguntas_quiz = random.sample(todas_perguntas, min(5, len(todas_perguntas)))
    else:
        perguntas_quiz = random.sample(perguntas[tema], min(5, len(perguntas[tema])))

    for q in perguntas_quiz:
        print(NEGRITO + "\n📌", q["pergunta"] + NORMAL)
        for opcao in q["opcoes"]:
            print(opcao)

        resposta = input(AMARELO + "Sua resposta (a, b ou c): " + NORMAL).strip().lower()

        if resposta == q["resposta"]:
            print(VERDE + "✅ Correto!" + NORMAL)
            acertos += 1
        else:
            print(VERMELHO + f"❌ Errado. {q['explicacao']}" + NORMAL)

    fim = time.time()
    tempo = round(fim - inicio)

    usuario["pontuacoes"].append(acertos)
    usuario["tempo_uso"] += tempo

    salvar_usuarios(usuarios)

    print(NEGRITO + f"\n🏁 Fim do exercício! Você acertou {acertos} de {len(perguntas_quiz)} perguntas." + NORMAL)
    print(f"⏱️ Tempo gasto: {tempo} segundos.")

import time
import random
from utils.cripto.cripto import descriptografar
from utils.helpers import carregar_usuarios, salvar_usuarios, carregar_perguntas

# 🔥 Carrega as perguntas
perguntas = carregar_perguntas()

if not perguntas:
    print("⚠️ Nenhuma pergunta encontrada. Verifique o arquivo perguntas.json.")


def escolher_tema():
    print("\n=== Escolha um tema ===")
    temas = list(perguntas.keys())  # 🚩 Se perguntas estiver vazio, temas também fica vazio

    for i, tema in enumerate(temas, 1):
        print(f"{i}. {tema}")

    print(f"{len(temas) + 1}. Quiz Misto (todas as áreas)")

    try:
        escolha = int(input("Digite o número do tema: "))
        if escolha == len(temas) + 1:
            return "Misto"
        elif 1 <= escolha <= len(temas):
            return temas[escolha - 1]
        else:
            print("❌ Opção inválida. Escolhendo Misto por padrão.")
            return "Misto"
    except ValueError:
        print("❌ Opção inválida. Escolhendo Misto por padrão.")
        return "Misto"



def fazer_exercicio(usuario_id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    nome = descriptografar(usuario['nome'])
    print(f"\n👋 Olá, {nome}! Vamos começar os exercícios...\n")

    tema = escolher_tema()
    acertos = 0
    inicio = time.time()

    # 🔀 Escolher perguntas
    if tema == "Misto":
        todas_perguntas = []
        for lista in perguntas.values():
            todas_perguntas.extend(lista)
        perguntas_quiz = random.sample(todas_perguntas, min(5, len(todas_perguntas)))
    else:
        perguntas_quiz = random.sample(perguntas[tema], min(5, len(perguntas[tema])))

    # 🔄 Loop das perguntas
    for q in perguntas_quiz:
        print("\n📌", q["pergunta"])
        for opcao in q["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta (a, b ou c): ").strip().lower()

        if resposta == q["resposta"]:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado. {q['explicacao']}")

    fim = time.time()
    tempo = round(fim - inicio)

    # 💾 Salvar pontuação e tempo
    usuario["pontuacoes"].append(acertos)
    usuario["tempo_uso"] += tempo

    salvar_usuarios(usuarios)

    print(f"\n🏁 Fim do exercício! Você acertou {acertos} de {len(perguntas_quiz)} perguntas.")
    print(f"⏱️ Tempo gasto: {tempo} segundos.")

import time
from utils.helpers import carregar_usuarios, salvar_usuarios


def fazer_exercicio(usuario_id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    print(f"\n👋 Olá, {usuario['nome']}! Vamos começar os exercício...\n")

    acertos = 0
    inicio = time.time()

    print("Pergunta 1: Qual é o próximo número da sequência? 2, 4, 6, 8, ...")
    resposta1 = input("Sua resposta: ")

    if resposta1.strip().lower() == "10":
        print("✅ Correto!")
        acertos += 1
    else:
        print("❌ Errado. Resposta correta: 10")

    print("Pergunta 2: Qual é o próximo número da sequência? 5, 10, 20, 40, ...")
    resposta2 = input("Sua resposta: ")

    if resposta2.strip().lower() == "80":
        print("✅ Correto!")
        acertos += 1
    else:
        print("❌ Errado. Resposta correta: 80")

    print("Pergunta 3: Qual é o próximo número da sequência? 1, 3, 9, 27, ...")
    resposta2 = input("Sua resposta: ")

    if resposta2.strip().lower() == "81":
        print("✅ Correto!")
        acertos += 1
    else:
        print("❌ Errado. Resposta correta: 81")

    print("Pergunta 4: Qual o valor de 2 * (3 + 4)?")
    resposta2 = input("Sua resposta: ")

    if resposta2.strip().lower() == "14":
        print("✅ Correto!")
        acertos += 1
    else:
        print("❌ Errado. Resposta correta: 14")

    print("Pergunta 5: Se 2 + 2 = 4 e 4 + 4 = 8, quanto é 8 + 8?")
    resposta2 = input("Sua resposta: ")

    if resposta2.strip().lower() == "16":
        print("✅ Correto!")
        acertos += 1
    else:
        print("❌ Errado. Resposta correta: 16")

    fim = time.time()
    tempo = round(fim - inicio)

    usuario["pontuacoes"].append(acertos)
    usuario["tempo_uso"] += tempo

    salvar_usuarios(usuarios)

    print(f"\n🏁 Fim do exercício! Você acertou {acertos} pergunta(s).")
    print(f"⏱️ Tempo gasto: {tempo} segundos.")

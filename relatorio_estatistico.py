from utils.helpers import carregar_usuarios
from estatisticas import calcular_media, calcular_moda, calcular_mediana

def gerar_relatorio_estatistico():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário encontrado.")
        return

    idades = [u["idade"] for u in usuarios]
    pontos = [sum(u["pontuacoes"]) for u in usuarios]
    exercicios = [len(u["pontuacoes"]) for u in usuarios]
    tempos = [u["tempo_uso"] for u in usuarios]

    with open("relatorio_estatistico.txt", "w", encoding="utf-8") as f:
        f.write("📊 RELATÓRIO ESTATÍSTICO DA PLATAFORMA 📊\n\n")

        def escrever_categoria(nome, lista):
            f.write(f"--- {nome} ---\n")
            f.write(f"Média: {calcular_media(lista):.2f}\n")
            f.write(f"Moda: {calcular_moda(lista)}\n")
            f.write(f"Mediana: {calcular_mediana(lista)}\n\n")

        escrever_categoria("Idade dos usuários", idades)
        escrever_categoria("Total de pontos", pontos)
        escrever_categoria("Exercícios feitos", exercicios)
        escrever_categoria("Tempo total de uso (segundos)", tempos)

    print("✅ Relatório gerado com sucesso: relatorio_estatistico.txt")

if __name__ == "__main__":
    gerar_relatorio_estatistico()

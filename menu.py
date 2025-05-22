from usuarios import criar_usuario, listar_usuarios, editar_usuario, excluir_usuario
from estatisticas import (
    desempenho_geral,
    desempenho_detalhado,
    desempenho_individual,
    ranking_usuarios
)
from exercicios import fazer_exercicio
from informacoes import sobre, ver_conteudo
from utils.cripto.cripto import gerar_chaves_automaticamente
from utils.helpers import carregar_usuarios
from colorama import Fore, Style, init

# 🔥 Inicializa o Colorama
init(autoreset=True)

# 🎨 Cores
AZUL = Fore.CYAN
VERDE = Fore.GREEN
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL

# 🔑 Gera as chaves na inicialização
gerar_chaves_automaticamente()


def exibir_menu():
    while True:
        print(NEGRITO + AZUL + "\n=== Plataforma de Educação Digital ===" + NORMAL)
        print(NEGRITO + """
1. Ver conteúdo
2. Cadastrar usuário
3. Listar usuários
4. Fazer exercício
5. Editar usuário
6. Excluir usuário
7. Ver desempenho
8. Ver ranking
9. Sobre o sistema
0. Sair
        """ + NORMAL)

        opcao = input(NEGRITO + AMARELO + "Escolha uma opção: " + NORMAL)

        if opcao == "1":
            ver_conteudo()

        elif opcao == "2":
            criar_usuario()

        elif opcao == "3":
            listar_usuarios()

        elif opcao == "4":
            while True:
                listar_usuarios()
                id_usuario = input(NEGRITO + AMARELO + "\nDigite o ID do usuário (ex.: R1) ou 9 para Voltar: " + NORMAL).upper()

                if id_usuario == "9":
                    break

                existe = any(u["id"] == id_usuario for u in carregar_usuarios())

                if existe:
                    fazer_exercicio(id_usuario)
                    break
                else:
                    print(VERMELHO + "⚠️ ID não encontrado. Tente novamente." + NORMAL)

        elif opcao == "5":
            editar_usuario()

        elif opcao == "6":
            excluir_usuario()

        elif opcao == "7":
            while True:
                print(NEGRITO + AZUL + "\n=== Menu de Desempenho ===" + NORMAL)
                print(NEGRITO + """
1. Desempenho Geral
2. Estatísticas Detalhadas
3. Desempenho Individual
9. Voltar
                """ + NORMAL)

                op_desempenho = input(NEGRITO + AMARELO + "Escolha uma opção: " + NORMAL)

                if op_desempenho == "1":
                    desempenho_geral()
                elif op_desempenho == "2":
                    desempenho_detalhado()
                elif op_desempenho == "3":
                    desempenho_individual()
                elif op_desempenho == "9":
                    break
                else:
                    print(AMARELO + ">>> Opção inválida." + NORMAL)

        elif opcao == "8":
            while True:
                print(NEGRITO + AZUL + "\n=== Menu de Ranking ===" + NORMAL)
                print(NEGRITO + """
1. Ranking por pontos
2. Ranking por exercícios
3. Ranking por tempo de uso
9. Voltar
                """ + NORMAL)

                op_ranking = input(NEGRITO + AMARELO + "Escolha uma opção: " + NORMAL)

                if op_ranking == "1":
                    ranking_usuarios("pontos")
                elif op_ranking == "2":
                    ranking_usuarios("exercicios")
                elif op_ranking == "3":
                    ranking_usuarios("tempo")
                elif op_ranking == "9":
                    break
                else:
                    print(AMARELO + ">>> Opção inválida." + NORMAL)

        elif opcao == "9":
            sobre()

        elif opcao == "0":
            print(VERDE + ">>> Saindo... Até logo!")
            break

        else:
            print(AMARELO + ">>> Opção inválida. Tente novamente." + NORMAL)
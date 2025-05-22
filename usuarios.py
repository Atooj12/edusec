from colorama import Fore, Style

from utils.cripto.cripto import criptografar, descriptografar
from utils.helpers import carregar_usuarios, salvar_usuarios


VERDE = Fore.GREEN
VERMELHO = Fore.RED
AMARELO = Fore.YELLOW
AZUL = Fore.CYAN
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL 

def criar_usuario():
    usuarios = carregar_usuarios()

    nome = input(NEGRITO + "Nome: " + NORMAL)
    idade = input(NEGRITO + "Idade: " + NORMAL)

    # Pega o maior número já usado nos IDs
    numeros_ids = [
        int(u["id"].replace("R", ""))
        for u in usuarios
        if u["id"].startswith("R")
    ]
    proximo_numero = max(numeros_ids, default=0) + 1
    proximo_id = f"R{proximo_numero}"

    novo = {
        "id": proximo_id,
        "nome": criptografar(nome),
        "idade": criptografar(idade),
        "pontuacoes": [],
        "tempo_uso": 0
    }

    usuarios.append(novo)
    salvar_usuarios(usuarios)
    print(VERDE + f"✅ Usuário criado com sucesso! ID: {proximo_id}" + NORMAL)



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
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    listar_usuarios()

    id_a_editar = input(NEGRITO + "Digite o ID que deseja editar ou 0 para Voltar: " + NORMAL).upper()

    if id_a_editar == "0":
        return

    for u in usuarios:
        if u['id'] == id_a_editar:
            novo_nome = input(NEGRITO + "Novo nome: " + NORMAL)
            nova_idade = input(NEGRITO + "Nova idade: " + NORMAL)
            u['nome'] = criptografar(novo_nome)
            u['idade'] = criptografar(nova_idade)

            salvar_usuarios(usuarios)
            print(VERDE + "✅ Usuário editado com sucesso!" + NORMAL)
            return

    print(VERMELHO + "⚠️ Usuário não encontrado." + NORMAL)



def excluir_usuario():
    usuarios = carregar_usuarios()

    if not usuarios:
        print(AMARELO + "Nenhum usuário encontrado." + NORMAL)
        return

    listar_usuarios()

    id_a_excluir = input(NEGRITO + "Digite o ID que deseja excluir ou 0 para Voltar: " + NORMAL).upper()

    if id_a_excluir == "0":
        return

    nova_lista = [u for u in usuarios if u['id'] != id_a_excluir]

    if len(nova_lista) == len(usuarios):
        print(VERMELHO + "⚠️ Usuário não encontrado." + NORMAL)
    else:
        salvar_usuarios(nova_lista)
        print(VERMELHO + "✅ Usuário excluído com sucesso!" + NORMAL)

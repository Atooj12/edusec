import json
import os
import sys

def caminho_absoluto(relativo):
    if getattr(sys, 'frozen', False):  # se estiver compilado com pyinstaller
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relativo)


# ================== USUÁRIOS ==================

CAMINHO_JSON = caminho_absoluto("dados/usuarios.json")

def carregar_usuarios():
    if not os.path.exists(CAMINHO_JSON):
        return []

    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_usuarios(lista):
    pasta = os.path.dirname(CAMINHO_JSON)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


# ================== PERGUNTAS ==================

CAMINHO_PERGUNTAS = caminho_absoluto("dados/perguntas.json")

def carregar_perguntas():
    if not os.path.exists(CAMINHO_PERGUNTAS):
        return {}  # Se não existir, retorna vazio

    with open(CAMINHO_PERGUNTAS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {}

def salvar_perguntas(perguntas):
    pasta = os.path.dirname(CAMINHO_PERGUNTAS)
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    with open(CAMINHO_PERGUNTAS, "w", encoding="utf-8") as arquivo:
        json.dump(perguntas, arquivo, indent=4, ensure_ascii=False)

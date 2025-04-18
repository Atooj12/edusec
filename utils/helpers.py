import json
import os
import sys

def caminho_absoluto(relativo):
    if getattr(sys, 'frozen', False):  # se estiver compilado com pyinstaller
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relativo)

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
    def salvar_usuarios(lista):
    # Garante que a pasta existe
        pasta = os.path.dirname(CAMINHO_JSON)
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

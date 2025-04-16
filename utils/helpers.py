import json
import os

CAMINHO_JSON= "dados/usuarios.json"

def carregar_usuarios():
    if not os.path.exists(CAMINHO_JSON):
        return []
    
    with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return[]
        

def salvar_usuarios(lista):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)
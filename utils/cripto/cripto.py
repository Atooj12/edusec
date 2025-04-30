from cryptography.fernet import Fernet

def gerar_chave():
    with open("chave.key", "wb") as chave_file:
        chave_file.write(Fernet.generate_key())

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar(texto):
    chave = carregar_chave()
    f = Fernet(chave)
    return f.encrypt(texto.encode()).decode()

def descriptografar(texto_criptografado):
    chave = carregar_chave()
    f = Fernet(chave)
    return f.decrypt(texto_criptografado.encode()).decode()

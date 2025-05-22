from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os

def carregar_chave_publica():
    with open("chave_publica.pem", "rb") as f:
        return serialization.load_pem_public_key(f.read())


def carregar_chave_privada():
    with open("chave_privada.pem", "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def criptografar(texto: str) -> str:
    chave_publica = carregar_chave_publica()
    texto_bytes = texto.encode()

    criptografado = chave_publica.encrypt(
        texto_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return criptografado.hex()  # Salvar como string no JSON


def descriptografar(texto_criptografado: str) -> str:
    chave_privada = carregar_chave_privada()
    texto_bytes = bytes.fromhex(texto_criptografado)

    descriptografado = chave_privada.decrypt(
        texto_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return descriptografado.decode()


# 🔑 Verifica se as chaves existem
def gerar_chaves_automaticamente():
    if not os.path.exists("chave_privada.pem") or not os.path.exists("chave_publica.pem"):
        print("🔐 Gerando chaves...")

        chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        with open("chave_privada.pem", "wb") as f:
            f.write(
                chave_privada.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        chave_publica = chave_privada.public_key()

        with open("chave_publica.pem", "wb") as f:
            f.write(
                chave_publica.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

        print("✅ Chaves geradas com sucesso!")
    else:
        print("🔑 Chaves já existem.")


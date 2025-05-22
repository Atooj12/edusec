from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# 🔥 Gera o par de chaves
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 🔑 Salvar chave privada
with open("chave_privada.pem", "wb") as f:
    f.write(
        chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# 🔓 Extrair chave pública
chave_publica = chave_privada.public_key()

# 🔑 Salvar chave pública
with open("chave_publica.pem", "wb") as f:
    f.write(
        chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("✅ Chaves geradas com sucesso!")

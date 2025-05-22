from colorama import Fore, Style

AZUL = Fore.CYAN
NEGRITO = Style.BRIGHT
NORMAL = Style.RESET_ALL



def ver_conteudo():
    print(NEGRITO + "\n📘 CONTEÚDO EDUCATIVO")
    print(AZUL + """
==========================
💡 LÓGICA DE PROGRAMAÇÃO
==========================
- Entender como resolver problemas com algoritmos.
- Uso de variáveis para armazenar informações.
- Estruturas condicionais (if, else).
- Laços de repetição (for, while).

==========================
💻 TECNOLOGIA DA INFORMAÇÃO (TI BÁSICA)
==========================
- O que é hardware e software.
- Componentes básicos de um computador.
- Conceitos de rede, internet e armazenamento.

==========================
🔐 SEGURANÇA DA INFORMAÇÃO
==========================
- Importância de senhas fortes.
- Como se proteger de golpes, como phishing.
- Boas práticas de segurança no dia a dia digital.

==========================
📜 LGPD (Lei Geral de Proteção de Dados)
==========================
- O que são dados pessoais.
- O que é consentimento e como funciona na LGPD.
- Direitos dos titulares de dados.
- Boas práticas para proteção e privacidade.

==========================
✅ INCLUSÃO DIGITAL
==========================
- Aprender conceitos básicos de tecnologia.
- Utilizar ferramentas digitais com segurança.
- Incentivar o desenvolvimento de habilidades digitais.
    """+ NORMAL)


def sobre():
    print(NEGRITO + "\n📄 SOBRE O SISTEMA")
    print(AZUL + """
Este sistema foi desenvolvido como parte do Projeto Integrado Multidisciplinar (PIM)
do curso de Análise e Desenvolvimento de Sistemas da Universidade Paulista - UNIP (2025/1).

🎯 Objetivo do sistema:
- Promover a inclusão digital de forma acessível e segura.
- Ensinar conceitos básicos de tecnologia, segurança digital e LGPD.
- Conscientizar sobre a importância da proteção de dados e privacidade.

🔐 Segurança:
- Os dados dos usuários são protegidos através de criptografia assimétrica,
utilizando chave pública e privada.

🗄️ Armazenamento:
- Os dados são armazenados localmente em arquivos JSON criptografados.

💻 Desenvolvido em:
- Linguagem: Python
- Execução: Terminal/Console
- Estrutura de dados: JSON
- Criptografia: RSA (assimétrica)
- Cores e interatividade: Biblioteca Colorama
    """ + NORMAL)

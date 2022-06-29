import smtplib, ssl

sender = 'REMETENTE'
password = 'SUA_SENHA'
receiver = 'DESTINATARIO'

body_msg = '''Subject: ASSUNTO DA SUA MENSAGEM

TEXTO DA SUA MENSAGEM
'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)

#FONTE: https://www.youtube.com/watch?v=Dg8L5t3kdAU&ab_channel=PythonPassiveIncome
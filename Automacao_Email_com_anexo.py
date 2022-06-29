#Bibliotecas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Função para logar no servidor Gmail
def gmail_login(username, password):
    smtp_server_name = "smtp.gmail.com"
    port_number = 587
    server = smtplib.SMTP(host=smtp_server_name, port=port_number)
    server.connect(host=smtp_server_name,port=port_number)
    server.starttls()
    server.login(user=username, password=password)
    return server

#Criando a mensagem
msg = MIMEMultipart()
msg['Subject'] = "ASSUNTO_DO_EMAIL"
msg['From'] = "REMETENTE"
msg['To'] = "DESTINATÁRIO"
msg['Bcc'] = 'DESTINATARIO_COPIA_OCULTA_SE_HOUVER'

#Criando a mensagem do corpo do e-mail
body = '''
<br>Dear honey, <br><br> Please find attachment. <br> <br> Thanks <br> Tiago. <br>
'''
msg.attach(MIMEText(body, 'html'))

#Criando arquivo em anexo
file_path = r"CAMINHO_DO_SEU_ARQUIVO_QUE_VAI_COMO_ANEXO"
file_name = "NOME_DO_SEU_ARQUIVO_QUE_VAI_COMO_ANEXO_COM_EXTENSÂO"
file = open(file_path+"\\"+file_name, "rb")

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(file.read())
file.close()
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=file_name)
msg.attach(payload)

#Enviando o e-mail
server = gmail_login(username='E_MAIL', password='SENHA')
server.send_message(msg)
server.quit()
print("E-mail enviado com anexo com sucesso!")

#Fonte, adaptado: https://www.youtube.com/watch?v=vtE5KtfqyPY&ab_channel=RamKrishna
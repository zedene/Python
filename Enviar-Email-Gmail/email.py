import os, smtplib,math,time
from email.message import EmailMessage
from login import password
from datetime import date
today = date.today()
data = today.strftime('%d/%m/%Y')

#CREDENCIAIS
#Alterar o Email

EMAIL_ADRESS = 'SEUEMAILAQUI'
EMAIL_PASSWORD = password


print('='*100)
print(f"{'Titulo do Programa'}".center(100)) 
print('='*100)

#Criar o E-mail
msg = EmailMessage()
msg['Subject'] = (f'ASSUNTO DO EMAIL {data}')
msg['From'] = 'SEU NOME'
msg['To'] = 'DESTINATARIO'
msg.set_content('DIGITE AQUI A MENSAGEM')

#Enviar o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
print('E-mail enviado com sucesso')

#Contador de segundos
startTime = time.time()
for i in range(10, 0, -1):
   print(f'O programa se encerrará em {i} segundos')
   time.sleep(1)

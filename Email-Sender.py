import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# SMTP SERVER CONFIG
smtp_server = '' #SMTP SERVER
smtp_port =  #YOU SHOULD PUT YOUR PORT
smtp_user = '' #YOUR PRIVATE EMAIL ACCOUNT
smtp_password = ''  #HERE YOUR PASSWORD FOR APPLITCATIONS

# HERE YOU SHOULD LIST YOUR RECIPIENTS. IF YOU SEPARATE THEM WITH COMMAS, THE EMAILS WILL BE SENT INDIVIDUALLY
destinatarios = ['example@example.com, example@example.com,']



# HERE YOU NEED TO COMPLETE THE EMAIL BODY
asunto = 'EXAMPLE: WORKS'
cuerpo = ''' HI, I AM JUAN MARCO CAPISANO,

I WANT TO HELP PEPOLE IN THE SEARCHING OF JOBS, HERE YOU SHOULD COMPLETE THE EMAIL BODY.

GRETTINGS FROM ARGENTINA.
HAVE A GOOD ONE :)
'''

#IF YOU NEED TO ATACH A PDF LIKE A CV, YOU SHOULD COMPLETE THIS. (THE FILE SHOULD BE IN THE SAME PATCH OF THIS SCRIPT)
archivos_adjuntos = ['example.pdf', 'example.pdf']


def enviar_correo(destinatario):

    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    
    mensaje.attach(MIMEText(cuerpo, 'plain'))


    for archivo in archivos_adjuntos:
        with open(archivo, 'rb') as f:
            adjunto = MIMEApplication(f.read(), _subtype='pdf')
            adjunto.add_header('Content-Disposition', 'attachment', filename=archivo)
            mensaje.attach(adjunto)

    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_user, smtp_password)  
            server.sendmail(smtp_user, destinatario, mensaje.as_string()) 
            print(f'Correo enviado a {destinatario}')
    except Exception as e:
        print(f'No se pudo enviar el correo a {destinatario}. Error: {str(e)}')


for destinatario in destinatarios:
    enviar_correo(destinatario)

import smtplib
from email.mime.text import MIMEText

def send_mail(nome, email, text):
    port =2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'b1609a4ef1c9ab'
    password = 'bd37e7053a350a'
    message = f'<h3> New Feedback Submission</h3><ul><li>Nome: {nome}</li><li>Email: {email}</li><li>Comments: {text}</li></ul>'

    sender_email = f'{email}'
    receiver_email = f'nlpprocessamento@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feed_Back_NLP'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
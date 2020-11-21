import smtplib
from email.message import EmailMessage
import os

sender = 'assassinvineet@gmail.com'
password = os.environ.get('gmail_id_2')
to = 'vineetmahajan2000@gmail.com'
subject = 'New Subject'

mes = EmailMessage()
mes['Subject']  = subject
mes['From']     = sender
mes['To']       = [to]

mes.set_content('Plain Content...')
with open('index.html', 'r') as fhand:
    file = fhand.read()
mes.add_alternative(file, subtype = 'html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)

    server.send_message(mes)
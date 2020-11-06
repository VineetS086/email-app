import smtplib


def send_mail_(args):
    #print('mail')
    from_addr   = args['From']
    password    = args['Password']

    to_addr     = args['To']
    cc_addr     = args['CC']
    bcc_addr    = args['BCC']
        
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_addr, password)

        SUBJECT = args['Subject']  
        TEXT = args['Text']  
        
        #message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        message     = "From: %s\r\n" % from_addr
        message    += "To: %s\r\n" % ",".join(to_addr)
        message    += "CC: %s\r\n" % ",".join(cc_addr)
        message    += "Subject: %s\r\n" % SUBJECT
        message    += "\r\n" 
        message    += TEXT

        to_addr    = to_addr + cc_addr + bcc_addr

        #print('message_compiled')
        #print(message)
        server.sendmail(from_addr, to_addr, message)
        #print('sent')
        
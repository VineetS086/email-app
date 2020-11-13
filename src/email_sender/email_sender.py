import smtplib

from .extra import process

def send_mail_(args):
    #print('mail')
    from_addr   = args['from_addr']  #
    password    = args['password']  #

    to_addr     = process(args['to_addr'])   #

    cc_addr     = process(args['cc_addr'])
    cc_addr     = [email for email in cc_addr if email not in to_addr]

    bcc_addr    = process(args['bcc_addr'])
    bcc_addr    = [email for email in bcc_addr if email not in to_addr or cc_addr]

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_addr, password)

        SUBJECT = args['subject']   #
        TEXT = args['text']         #
        
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
        server.quit()
        #print('sent')
        
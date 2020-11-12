import smtplib

from .extra import process

def send_mail_(args):
    #print('mail')
    from_addr   = args['from_addr']  #
    password    = args['password']  #

    to_addr     = process(args['to_addr'])   #
    cc_addr     = args['cc_addr'].split() 
    bcc_addr    = args['bcc_addr'].split() 
        
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

        print('message_compiled')
        print(message)
        #server.sendmail(from_addr, to_addr, message)
        #server.quit()
        #print('sent')
        
import smtplib


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='jobportal0098@gmail.com'
EMAIL_HOST_PASSWORD = 'rywrslckgyguimrr'

def mailsender(Email):
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    SUBJECT="new Job added"
    TEXT="New Job as Add Visit the link Job portal site http://127.0.0.1:5000/"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    smtpserver.sendmail(EMAIL_HOST_USER,Email,message)
    smtpserver.close()


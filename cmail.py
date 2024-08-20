import smtplib
from smtplib import SMTP
from email.message import EmailMessage 
def sendmail(to,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('thimmanacharan@gmail.com','cums ywoc wmpo ahto')
    msg=EmailMessage()
    msg['FROM']='thimmanacharan@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
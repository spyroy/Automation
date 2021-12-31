import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''
print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'test@gmail.com'
TO = 'test@gmail.com'
PASS = '****'

msg = MIMEMultipart()

msg['Subject'] = 'Please send corona test to Yuval' + ' ' + str(now.day) + '_' + str(now.month) + '_' + str(
    now.year) + '_' + str(now.strftime("%I:%M %p"))
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText("Dont forget to send a picture of corona test to Yuval from Gigantic"))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
msg = msg.as_string()
server.sendmail(FROM, TO, msg)

server.quit()
print('Email Sent...')
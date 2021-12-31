import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''


def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:<b>\n' + '<br>' * 5 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return (cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Messege')

print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'spyroy@gmail.com'
TO = 'spyroy@gmail.com'
PASS = '****'

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + '' + str(now.day) + '_' + str(now.month) + '_' + str(
    now.year) + '_' + str(now.strftime("%I:%M %p"))
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

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

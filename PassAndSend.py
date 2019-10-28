"""
Author: Aidan Jude
Date: 10/28/2019
"""

from PoemFetch import *
import smtplib
from email.mime.text import MIMEText
from time import sleep

#utilize a gmail account to send the desired text messages
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(GMAIL_ACCOUNT_HERE, PASSWORD_HERE)
end_users = [PHONE_NUMEBERS_BY_CARRIER]

author, title, lines = get_random_poem(15)
to_send = lines

#send barrier to separate today's poem from previous poem
for user in end_users:
    server.sendmail('Daily Poem', user, MIMEText('--------', 'html').as_string())
    sleep(1.0)
#send title of poem
for user in end_users:
    server.sendmail('Daily Poem', user, MIMEText('Todays Poem: ' + title, 'html').as_string())
    sleep(2.5)
#send lines
for user in end_users:
    for line in lines.splitlines():
        server.sendmail('Daily Poem', user, MIMEText(line, 'html').as_string())
        sleep(2.5)
#send author
for user in end_users:
    server.sendmail('Daily Poem', user, MIMEText(' - ' + author, 'html').as_string())

server.quit()

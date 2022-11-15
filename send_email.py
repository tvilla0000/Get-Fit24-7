from asyncio.windows_events import NULL
import smtplib
from email.message import EmailMessage
from data_set import main

user = "tvilla0000@gmail.com"
password = "uabtrdptvrawydoy"
test_name = "Joao"


def send_email(subject, body, to):
    email = EmailMessage()
    email.set_content(body)
    email['subject'] = subject
    email['to'] = to
    email['body'] = body
    email['from'] = user
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password) 
    server.send_message(email)
    server.quit()




if __name__ == '__main__':
    send_email("Hi" + " " + test_name + "!", "This is a test message! This message was sent using Python!", "alvesjoao98@yahoo.com")


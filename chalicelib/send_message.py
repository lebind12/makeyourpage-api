import smtplib
from email.mime.text import MIMEText


def send_mail(data):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(data['host_address'], data['host_password'])
    msg = MIMEText(data['content'])
    msg['Subject'] = data['subject']
    msg['To'] = data['address']
    msg['From'] = data['host_address']
    smtp.send_message(msg)
    smtp.quit()

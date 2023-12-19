# In the name of GOD

from config import settings

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

smtp_server = settings.SMTP_SERVER
smtp_port = settings.SMTP_PORT
smtp_email_host = settings.EMAIL_HOST
smtp_password = settings.EMIAL_PASSWORD

def send_email(to_email, subject, message, attachment_data:dict=None, from_email=smtp_email_host):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, "plain"))
    if attachment_data:
        msg.attach(attachment_data.get("content"), attachment_data.get("content"))
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(from_email, smtp_password)
        smtp.send_message(msg)

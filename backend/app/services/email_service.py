import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings


def send_email(subject: str, recipient: str, html_body: str) -> None:
    message = MIMEMultipart()
    message["From"] = settings.email_username
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as server:
        server.starttls()
        server.login(settings.email_username, settings.email_password.get_secret_value())
        server.sendmail(settings.email_username, recipient, message.as_string())

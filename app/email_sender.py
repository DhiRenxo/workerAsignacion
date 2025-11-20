import smtplib
from email.mime.text import MIMEText
from app.config import settings

def enviar_email(destinatario: str, asunto: str, mensaje: str):

    try:
        msg = MIMEText(mensaje, "html")
        msg["Subject"] = asunto
        msg["From"] = settings.MAIL_FROM
        msg["To"] = destinatario

        with smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ Email enviado a {destinatario} con Gmail SMTP")

    except Exception as e:
        print(f"❌ Error al enviar email SMTP: {str(e)}")

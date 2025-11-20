import smtplib
from email.mime.text import MIMEText

def enviar_email_smtp(destinatario: str, asunto: str, mensaje: str,
                    mail_from, mail_server, mail_port, mail_username, mail_password):
    try:
        msg = MIMEText(mensaje, "html", "utf-8")
        msg["Subject"] = asunto
        msg["From"] = mail_from
        msg["To"] = destinatario

        with smtplib.SMTP(mail_server, mail_port) as server:
            server.starttls()
            server.login(mail_username, mail_password)
            server.sendmail(mail_from, destinatario, msg.as_string())

        print(f"✅ Email enviado a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar email a {destinatario}: {str(e)}")

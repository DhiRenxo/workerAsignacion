import resend
from app.config import settings

resend.api_key = settings.RESEND_API_KEY

def enviar_email_resend(destinatario: str, asunto: str, mensaje: str):
    try:
        resend.Emails.send({
            "from": settings.RESEND_FROM,
            "to": destinatario,
            "subject": asunto,
            "html": mensaje
        })

        print(f"✅ Email enviado a {destinatario} con RESEND")

    except Exception as e:
        print(f"❌ Error al enviar email con RESEND a {destinatario}: {str(e)}")

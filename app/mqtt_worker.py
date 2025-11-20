import json
import paho.mqtt.client as mqtt
import uuid
from app.config import settings
from app.email_sender import enviar_email_smtp

# =========================
# Callback al recibir mensaje MQTT
# =========================
def on_message(client, userdata, msg):
    print(f"📩 Mensaje recibido en tópico: {msg.topic}")  # <-- print de prueba
    try:
        payload = json.loads(msg.payload.decode())
        print(f"🔹 Payload recibido: {payload}")  # <-- print de prueba
        enviar_email_smtp(
            destinatario=payload["destinatario"],
            asunto=payload["asunto"],
            mensaje=payload["mensaje"],
            mail_from=payload["mail_from"],
            mail_server=payload["mail_server"],
            mail_port=payload["mail_port"],
            mail_username=payload["mail_username"],
            mail_password=payload["mail_password"]
        )
    except Exception as e:
        print(f"❌ Error al procesar mensaje MQTT: {str(e)}")

# =========================
# Configuración cliente MQTT
# =========================
def iniciar_worker():
    client = mqtt.Client(client_id=f"MQTTWorker-{uuid.uuid4().hex[:8]}", transport="websockets")
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    client.tls_set()
    client.on_message = on_message

    # Callback al conectarse
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("✅ Conectado al broker MQTT correctamente")
        else:
            print(f"❌ Error al conectar al broker MQTT, código: {rc}")

    client.on_connect = on_connect

    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)
    client.subscribe(settings.MQTT_TOPIC_EMAIL)
    print(f"🔔 Worker iniciado. Escuchando en el tópico: {settings.MQTT_TOPIC_EMAIL}")
    client.loop_forever()

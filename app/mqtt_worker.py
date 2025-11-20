# mqtt_worker.py

import json
import paho.mqtt.client as mqtt
import uuid
from app.config import settings
from app.email_sender import enviar_email_resend


# ===============================
# CALLBACK: Al recibir mensaje
# ===============================
def on_message(client, userdata, msg):
    print(f"📩 Mensaje recibido en tópico: {msg.topic}")

    try:
        payload = json.loads(msg.payload.decode())
        print(f"🔹 Payload recibido: {payload}")

        enviar_email_resend(
            destinatario=payload["to"],
            asunto=payload["subject"],
            mensaje=payload["html"]
        )

    except Exception as e:
        print(f"❌ Error al procesar mensaje MQTT: {str(e)}")


# ===============================
# INICIAR WORKER MQTT (WSS 8884)
# ===============================
def iniciar_worker():
    client = mqtt.Client(
        client_id=f"MQTTWorker-{uuid.uuid4().hex[:8]}",
        transport="websockets"  # obligatorio para puerto 8884 en HiveMQ
    )

    # Credenciales HiveMQ Cloud
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

    # TLS obligatorio
    client.tls_set()

    # -------------------------------
    # Callback cuando conecta
    # -------------------------------
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("✅ Conectado al broker MQTT correctamente")

            # Suscripción SOLO cuando se conecte
            client.subscribe(settings.MQTT_TOPIC_EMAIL)
            print(f"🔔 Suscrito al tópico: {settings.MQTT_TOPIC_EMAIL}")
        else:
            print(f"❌ Error al conectar al broker MQTT, código: {rc}")

    client.on_connect = on_connect
    client.on_message = on_message

    # Conexión
    print("🚀 Conectando al broker MQTT…")
    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT)

    print("🔧 Worker iniciado y escuchando mensajes…")
    client.loop_forever()

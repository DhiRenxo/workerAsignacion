import os

# Puerto dummy para Render
os.environ["PORT"] = os.getenv("PORT", "10000")

from app.mqtt_worker import iniciar_worker

if __name__ == "__main__":
    iniciar_worker()

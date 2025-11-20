from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuración de correo
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587

    # Configuración MQTT
    MQTT_BROKER: str
    MQTT_PORT: int = 8884
    MQTT_USER: str
    MQTT_PASSWORD: str
    MQTT_TOPIC_EMAIL: str = "notificaciones/email"

    # Configuración para Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",  # Solo se usa localmente
        env_file_encoding="utf-8"
    )

# Instancia global
settings = Settings()

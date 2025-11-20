from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Resend
    RESEND_API_KEY: str
    RESEND_FROM: str

    # MQTT
    MQTT_BROKER: str
    MQTT_PORT: int = 8884
    MQTT_USER: str
    MQTT_PASSWORD: str
    MQTT_TOPIC_EMAIL: str = "notificaciones/email"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()

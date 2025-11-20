from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587

    MQTT_BROKER: str
    MQTT_PORT: int = 8884
    MQTT_USER: str
    MQTT_PASSWORD: str
    MQTT_TOPIC_EMAIL: str = "notificaciones/email"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict
import logging.config

class Settings(BaseSettings):
    MONGODB_HOST : str
    MONGODB_PORT : str
    MONGODB_DATABASE : str

    AUTH_NTF_KEY1 : str
    AUTH_NTF_KEY2 : str
    AUTH_NTF_KEY3 : str

    ACC_NTF_KEY1 : str
    ACC_NTF_KEY2 : str
    ACC_NTF_KEY3 : str

    NTF_AUTH_SHARED_KEY : str
    NTF_ACC_SHARED_KEY : str

    NTF_POD_KEY1 : str
    NTF_POD_SHARED_KEY: str

    AUTHENTICATION_SERVICE_URL : str
    ACCOUNT_SERVICE_URL : str
    
    SMTP_SERVER : str
    SMTP_PORT : int
    EMAIL_HOST : str
    EMIAL_PASSWORD : str


    model_config = SettingsConfigDict(env_file=".env", extra="allow")


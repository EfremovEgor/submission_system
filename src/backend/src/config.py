from dotenv import load_dotenv
import os
from pydantic import EmailStr

from pydantic_settings import BaseSettings

load_dotenv()

CONFIRMATION_LINK_EXPIRATION_TIME = 6000
DOMAIN_NAME = "https://confchair.org"
AUTH_PREFIX = "/auth"


class Settings(BaseSettings):
    # Postgres settings
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB_URL: str
    POSTGRES_ECHO: bool

    # Mailing settings
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: EmailStr
    EMAIL_STARTTLS: bool
    EMAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    # Auth
    OAUTH_SECRET_KEY: str
    OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES: float

    class Config:
        env_file = "../.env"


settings = Settings()

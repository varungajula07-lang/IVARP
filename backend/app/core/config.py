from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr, SecretStr, Field

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    secret_key: SecretStr = Field(..., env="SECRET_KEY")
    algorithm: str = Field("HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_minutes: int = Field(1440, env="REFRESH_TOKEN_EXPIRE_MINUTES")
    supabase_url: str = Field(..., env="SUPABASE_URL")
    supabase_key: SecretStr = Field(..., env="SUPABASE_KEY")
    openai_api_key: SecretStr | None = Field(None, env="OPENAI_API_KEY")
    gemini_api_key: SecretStr | None = Field(None, env="GEMINI_API_KEY")
    groq_api_key: SecretStr | None = Field(None, env="GROQ_API_KEY")
    virustotal_api_key: SecretStr | None = Field(None, env="VIRUSTOTAL_API_KEY")
    shodan_api_key: SecretStr | None = Field(None, env="SHODAN_API_KEY")
    abuseipdb_api_key: SecretStr | None = Field(None, env="ABUSEIPDB_API_KEY")
    nvd_api_key: SecretStr | None = Field(None, env="NVD_API_KEY")
    censys_api_id: str | None = Field(None, env="CENSYS_API_ID")
    censys_secret: SecretStr | None = Field(None, env="CENSYS_SECRET")
    email_username: EmailStr = Field(..., env="EMAIL_USERNAME")
    email_password: SecretStr = Field(..., env="EMAIL_PASSWORD")
    smtp_server: str = Field(..., env="SMTP_SERVER")
    smtp_port: int = Field(..., env="SMTP_PORT")
    slack_webhook_url: str | None = Field(None, env="SLACK_WEBHOOK_URL")

    class Config:
        case_sensitive = True


settings = Settings()
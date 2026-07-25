"""Configuration Settings"""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application Settings"""

    # Backend Configuration
    FASTAPI_ENV: str = "development"
    FASTAPI_DEBUG: bool = True
    FASTAPI_HOST: str = "0.0.0.0"
    FASTAPI_PORT: int = 8000

    # Security
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"

    # JWT Configuration
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 7

    # Database Configuration
    DATABASE_URL: str = "postgresql://plakyab:plakyab_password@localhost:5432/plakyab"
    DATABASE_ECHO: bool = True
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis Configuration
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_TTL: int = 3600
    REDIS_MAX_CONNECTIONS: int = 50

    # API Configuration
    API_VERSION: str = "v1"
    API_TITLE: str = "Vehicle Information & Diagnostics Platform"
    API_DESCRIPTION: str = "Enterprise-grade vehicle information management system"
    API_DOCS_URL: str = "/docs"
    API_REDOC_URL: str = "/redoc"

    # CORS Configuration
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8080",
    ]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60

    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "/app/logs/app.log"
    LOG_MAX_BYTES: int = 10485760  # 10MB
    LOG_BACKUP_COUNT: int = 5

    # Email Configuration
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "noreply@plakyab.com"

    # Vehicle Provider API Configuration
    VEHICLE_API_PROVIDER: str = "official-provider"
    VEHICLE_API_KEY: str = ""
    VEHICLE_API_URL: str = ""
    VEHICLE_API_TIMEOUT: int = 30
    VEHICLE_API_RETRIES: int = 3

    # VIN Decoder Configuration
    VIN_VALIDATION_ENABLED: bool = True
    VIN_ISO_3779_COMPLIANT: bool = True
    VIN_CACHE_TTL: int = 86400  # 24 hours

    # Mobile App Configuration
    MOBILE_APP_NAME: str = "Plakyab"
    MOBILE_APP_VERSION: str = "1.0.0"
    MOBILE_API_TIMEOUT: int = 30

    # Feature Flags
    FEATURE_OFFLINE_MODE: bool = True
    FEATURE_PUSH_NOTIFICATIONS: bool = True
    FEATURE_ANALYTICS: bool = True
    FEATURE_DARK_MODE: bool = True
    FEATURE_MULTI_LANGUAGE: bool = True

    # Admin Configuration
    ADMIN_EMAIL: str = "admin@plakyab.local"
    ADMIN_DEFAULT_PASSWORD: str = "admin123456"
    ADMIN_DASHBOARD_URL: str = "/admin"

    # Security Configuration
    SECURE_COOKIE: bool = False
    HTTP_ONLY_COOKIE: bool = True
    SAME_SITE_COOKIE: str = "lax"

    # Database Seeding
    DATABASE_SEED_INITIAL_DATA: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached)"""
    return Settings()


settings = get_settings()

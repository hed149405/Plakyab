"""Authentication Service"""

import logging
from datetime import datetime, timedelta
from typing import Optional

import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import settings
from app.models.user import User
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """Authentication Service"""

    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt"""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(user_id: int, expires_in_hours: int = settings.JWT_EXPIRATION_HOURS) -> str:
        """Create access token"""
        expire = datetime.utcnow() + timedelta(hours=expires_in_hours)
        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "access",
        }
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )
        return token

    @staticmethod
    def create_refresh_token(user_id: int, expires_in_days: int = settings.JWT_REFRESH_EXPIRATION_DAYS) -> str:
        """Create refresh token"""
        expire = datetime.utcnow() + timedelta(days=expires_in_days)
        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "refresh",
        }
        token = jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )
        return token

    @staticmethod
    def verify_token(token: str) -> Optional[dict]:
        """Verify and decode token"""
        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM],
            )
            return payload
        except jwt.ExpiredSignatureError:
            logger.warning("Token expired")
            return None
        except jwt.InvalidTokenError:
            logger.warning("Invalid token")
            return None

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user = self.user_repo.get_by_email(email)
        if not user:
            logger.warning(f"User not found: {email}")
            return None

        if not self.verify_password(password, user.password_hash):
            logger.warning(f"Invalid password for user: {email}")
            return None

        if not user.is_active:
            logger.warning(f"User inactive: {email}")
            return None

        # Update last login
        user.last_login = datetime.utcnow()
        self.db.commit()

        return user

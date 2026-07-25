"""User Repository"""

from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """User Repository Implementation"""

    def __init__(self, db: Session):
        super().__init__(db, User)

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(User).filter(
            User.email == email.lower()
        ).first()

    def get_active_users(self, skip: int = 0, limit: int = 20):
        """Get all active users"""
        return self.db.query(User).filter(
            User.is_active == True,
            User.deleted_at == None,
        ).offset(skip).limit(limit).all()

    def email_exists(self, email: str) -> bool:
        """Check if email exists"""
        return self.exists(email=email.lower())

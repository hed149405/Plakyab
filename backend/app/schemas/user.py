"""User Schemas"""

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr, validator

from app.utils.validators import PasswordValidator, EmailValidator


class UserBase(BaseModel):
    """Base User Schema"""
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=255)
    phone: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    """Create User Schema"""
    password: str = Field(..., min_length=8)

    @validator("password")
    def validate_password(cls, v):
        is_valid, error_msg = PasswordValidator.validate(v)
        if not is_valid:
            raise ValueError(error_msg)
        return v


class UserUpdate(BaseModel):
    """Update User Schema"""
    full_name: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None

    class Config:
        from_attributes = True


class UserPasswordChange(BaseModel):
    """Change Password Schema"""
    old_password: str
    new_password: str

    @validator("new_password")
    def validate_password(cls, v):
        is_valid, error_msg = PasswordValidator.validate(v)
        if not is_valid:
            raise ValueError(error_msg)
        return v


class UserResponse(UserBase):
    """User Response Schema"""
    id: int
    is_active: bool
    is_verified: bool
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserDetailResponse(UserResponse):
    """User Detail Response with Roles"""
    roles: List[str] = []

    class Config:
        from_attributes = True

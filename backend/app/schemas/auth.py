"""Authentication Schemas"""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class TokenResponse(BaseModel):
    """Token Response Schema"""
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    """Login Request Schema"""
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    """Register Request Schema"""
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=255)
    password: str = Field(..., min_length=8)
    phone: Optional[str] = None


class RefreshTokenRequest(BaseModel):
    """Refresh Token Request Schema"""
    refresh_token: str


class ForgotPasswordRequest(BaseModel):
    """Forgot Password Request Schema"""
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    """Reset Password Request Schema"""
    token: str
    new_password: str = Field(..., min_length=8)

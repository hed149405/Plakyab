"""Authentication Routes"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    RefreshTokenRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository
from app.models.user import User

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/register", response_model=dict)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """User registration endpoint"""
    user_repo = UserRepository(db)
    
    # Check if user exists
    if user_repo.email_exists(request.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    
    # Hash password
    auth_service = AuthService(db)
    hashed_password = auth_service.hash_password(request.password)
    
    # Create user
    user_data = {
        "email": request.email.lower(),
        "full_name": request.full_name,
        "password_hash": hashed_password,
        "phone": request.phone,
    }
    user = user_repo.create(user_data)
    logger.info(f"User registered: {user.email}")
    
    return {
        "status": "success",
        "message": "User registered successfully",
        "user_id": user.id,
    }


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """User login endpoint"""
    auth_service = AuthService(db)
    
    # Authenticate user
    user = await auth_service.authenticate_user(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    logger.info(f"User logged in: {user.email}")
    
    # Create tokens
    access_token = auth_service.create_access_token(user.id)
    refresh_token = auth_service.create_refresh_token(user.id)
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=24 * 3600,  # 24 hours in seconds
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(request: RefreshTokenRequest, db: Session = Depends(get_db)):
    """Refresh access token endpoint"""
    auth_service = AuthService(db)
    
    # Verify refresh token
    payload = auth_service.verify_token(request.refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    user_id = int(payload.get("sub"))
    
    # Create new access token
    access_token = auth_service.create_access_token(user_id)
    new_refresh_token = auth_service.create_refresh_token(user_id)
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token,
        expires_in=24 * 3600,
    )


@router.post("/logout", response_model=dict)
async def logout():
    """User logout endpoint"""
    logger.info("User logged out")
    return {"status": "success", "message": "Logged out successfully"}

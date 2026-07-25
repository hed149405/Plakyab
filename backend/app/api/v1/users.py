"""User Routes"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.user import (
    UserResponse,
    UserUpdate,
    UserDetailResponse,
)
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/me", response_model=UserDetailResponse)
async def get_current_user(db: Session = Depends(get_db)):
    """Get current user profile"""
    # TODO: Get user from JWT token
    raise HTTPException(status_code=401, detail="Not authenticated")


@router.put("/me", response_model=UserResponse)
async def update_current_user(
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    """Update current user profile"""
    # TODO: Get user from JWT token and update
    raise HTTPException(status_code=401, detail="Not authenticated")


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    repo = UserRepository(db)
    user = repo.get_by_id(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

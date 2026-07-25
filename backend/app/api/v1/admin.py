"""Admin Routes"""

import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.user import UserResponse

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/dashboard", response_model=dict)
async def get_dashboard(db: Session = Depends(get_db)):
    """Get admin dashboard data"""
    # TODO: Add admin authorization check
    
    user_repo = UserRepository(db)
    vehicle_repo = VehicleRepository(db)
    
    total_users = len(user_repo.get_all(limit=999999))
    total_vehicles = len(vehicle_repo.get_all(limit=999999))
    
    return {
        "status": "success",
        "data": {
            "total_users": total_users,
            "total_vehicles": total_vehicles,
            "total_searches": 0,  # TODO: Add search tracking
        },
    }


@router.get("/users", response_model=List[UserResponse])
async def list_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """List all users"""
    # TODO: Add admin authorization check
    
    repo = UserRepository(db)
    return repo.get_all(skip=skip, limit=limit)


@router.get("/stats", response_model=dict)
async def get_statistics(db: Session = Depends(get_db)):
    """Get system statistics"""
    # TODO: Add admin authorization check
    
    return {
        "status": "success",
        "data": {
            "api_calls": 0,
            "total_searches": 0,
            "active_sessions": 0,
            "cache_hits": 0,
            "cache_misses": 0,
        },
    }

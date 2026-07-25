"""Vehicle Routes"""

import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.vehicle import (
    VehicleCreate,
    VehicleUpdate,
    VehicleResponse,
    VehicleSearchRequest,
    VehicleSearchResponse,
)
from app.repositories.vehicle_repository import VehicleRepository
from app.services.vin_decoder import VINDecoder
from app.utils.validators import VINValidator
from app.middleware.error_handler import NotFoundError, ValidationError

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=VehicleResponse)
async def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    """Create new vehicle record"""
    repo = VehicleRepository(db)
    
    # Check if vehicle already exists
    if repo.get_by_vin(vehicle.vin):
        raise HTTPException(status_code=409, detail="Vehicle with this VIN already exists")
    
    # Create vehicle
    vehicle_data = vehicle.dict()
    vehicle_data["vin"] = vehicle_data["vin"].upper()
    created_vehicle = repo.create(vehicle_data)
    
    logger.info(f"Vehicle created: {created_vehicle.vin}")
    return created_vehicle


@router.get("/{vehicle_id}", response_model=VehicleResponse)
async def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    """Get vehicle by ID"""
    repo = VehicleRepository(db)
    vehicle = repo.get_by_id(vehicle_id)
    
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    return vehicle


@router.get("/by-vin/{vin}", response_model=VehicleResponse)
async def get_vehicle_by_vin(vin: str, db: Session = Depends(get_db)):
    """Get vehicle by VIN"""
    if not VINValidator.validate_format(vin):
        raise HTTPException(status_code=422, detail="Invalid VIN format")
    
    repo = VehicleRepository(db)
    vehicle = repo.get_by_vin(vin)
    
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
async def update_vehicle(
    vehicle_id: int,
    vehicle: VehicleUpdate,
    db: Session = Depends(get_db),
):
    """Update vehicle record"""
    repo = VehicleRepository(db)
    updated_vehicle = repo.update(vehicle_id, vehicle.dict(exclude_unset=True))
    
    if not updated_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    logger.info(f"Vehicle updated: {vehicle_id}")
    return updated_vehicle


@router.delete("/{vehicle_id}", response_model=dict)
async def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    """Delete vehicle record"""
    repo = VehicleRepository(db)
    
    if not repo.delete(vehicle_id):
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    logger.info(f"Vehicle deleted: {vehicle_id}")
    return {"status": "success", "message": "Vehicle deleted successfully"}


@router.post("/search", response_model=VehicleSearchResponse)
async def search_vehicles(
    request: VehicleSearchRequest,
    db: Session = Depends(get_db),
):
    """Search vehicles"""
    repo = VehicleRepository(db)
    
    vehicles, total = repo.search(
        manufacturer=request.manufacturer,
        model=request.model,
        model_year=request.model_year,
        skip=request.offset,
        limit=request.limit,
    )
    
    return VehicleSearchResponse(
        total=total,
        limit=request.limit,
        offset=request.offset,
        results=vehicles,
    )


@router.post("/vin/decode", response_model=dict)
async def decode_vin(vin: str = Query(..., min_length=17, max_length=17)):
    """Decode VIN"""
    if not VINValidator.validate_format(vin):
        raise HTTPException(status_code=422, detail="Invalid VIN format")
    
    decoded = VINDecoder.decode(vin)
    if not decoded:
        raise HTTPException(status_code=400, detail="Could not decode VIN")
    
    return {"status": "success", "data": decoded}


@router.get("/vin/validate/{vin}", response_model=dict)
async def validate_vin(vin: str):
    """Validate VIN"""
    is_valid = VINValidator.validate(vin)
    
    return {
        "status": "success",
        "vin": vin.upper(),
        "is_valid": is_valid,
        "format_valid": VINValidator.validate_format(vin),
        "checksum_valid": VINValidator.validate_checksum(vin) if VINValidator.validate_format(vin) else False,
    }

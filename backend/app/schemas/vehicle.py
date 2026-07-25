"""Vehicle Schemas"""

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, validator

from app.utils.validators import VINValidator, PlateValidator


class VehicleBase(BaseModel):
    """Base Vehicle Schema"""
    vin: str = Field(..., min_length=17, max_length=17)
    plate_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None
    manufacturer: str
    model: str
    model_year: int
    color: Optional[str] = None
    engine_type: Optional[str] = None
    engine_displacement: Optional[str] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    body_type: Optional[str] = None
    number_of_seats: Optional[int] = None
    number_of_doors: Optional[int] = None
    weight: Optional[int] = None
    length: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    notes: Optional[str] = None

    @validator("vin")
    def validate_vin(cls, v):
        if not VINValidator.validate(v):
            raise ValueError("Invalid VIN format or checksum")
        return v.upper()

    @validator("plate_number")
    def validate_plate(cls, v):
        if v and not PlateValidator.validate(v):
            raise ValueError("Invalid plate number format")
        return v

    class Config:
        from_attributes = True


class VehicleCreate(VehicleBase):
    """Create Vehicle Schema"""
    pass


class VehicleUpdate(BaseModel):
    """Update Vehicle Schema"""
    plate_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    model_year: Optional[int] = None
    color: Optional[str] = None
    engine_type: Optional[str] = None
    engine_displacement: Optional[str] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    body_type: Optional[str] = None
    number_of_seats: Optional[int] = None
    number_of_doors: Optional[int] = None
    weight: Optional[int] = None
    length: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class VehicleResponse(VehicleBase):
    """Vehicle Response Schema"""
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class VehicleSearchRequest(BaseModel):
    """Vehicle Search Request"""
    vin: Optional[str] = None
    plate_number: Optional[str] = None
    engine_number: Optional[str] = None
    chassis_number: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    model_year: Optional[int] = None
    limit: int = Field(20, le=100)
    offset: int = Field(0, ge=0)


class VehicleSearchResponse(BaseModel):
    """Vehicle Search Response"""
    total: int
    limit: int
    offset: int
    results: List[VehicleResponse]

    class Config:
        from_attributes = True

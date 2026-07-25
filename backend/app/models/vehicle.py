"""Vehicle Models"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, Text, Boolean, ForeignKey, JSONB
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Vehicle(Base):
    """Vehicle Model"""
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    
    # Identifiers
    vin = Column(String(17), unique=True, nullable=False, index=True)
    plate_number = Column(String(20), nullable=True, index=True)
    engine_number = Column(String(50), nullable=True, index=True)
    chassis_number = Column(String(50), nullable=True, index=True)
    
    # Vehicle Information
    manufacturer = Column(String(100), nullable=False, index=True)
    model = Column(String(100), nullable=False, index=True)
    model_year = Column(Integer, nullable=False, index=True)
    color = Column(String(50), nullable=True)
    
    # Technical Specs
    engine_type = Column(String(100), nullable=True)
    engine_displacement = Column(String(50), nullable=True)
    fuel_type = Column(String(50), nullable=True)
    transmission = Column(String(50), nullable=True)
    body_type = Column(String(50), nullable=True)
    number_of_seats = Column(Integer, nullable=True)
    number_of_doors = Column(Integer, nullable=True)
    
    # Dimensions & Weight
    weight = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    
    # Additional Info
    status = Column(String(20), default="active", nullable=False, index=True)
    notes = Column(Text, nullable=True)
    metadata = Column(JSONB, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)


class VehicleHistory(Base):
    """Vehicle Service/Maintenance History"""
    __tablename__ = "vehicle_history"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False, index=True)
    
    # Service Info
    service_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    service_date = Column(DateTime, nullable=False, index=True)
    
    # Details
    mileage = Column(Integer, nullable=True)
    cost = Column(String(50), nullable=True)
    service_provider = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

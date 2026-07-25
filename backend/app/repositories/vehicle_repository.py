"""Vehicle Repository"""

from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.repositories.base_repository import BaseRepository
from app.utils.enums import SearchType


class VehicleRepository(BaseRepository[Vehicle]):
    """Vehicle Repository Implementation"""

    def __init__(self, db: Session):
        super().__init__(db, Vehicle)

    def get_by_vin(self, vin: str) -> Optional[Vehicle]:
        """Get vehicle by VIN"""
        return self.db.query(Vehicle).filter(
            Vehicle.vin == vin.upper()
        ).first()

    def get_by_plate(self, plate: str) -> Optional[Vehicle]:
        """Get vehicle by plate number"""
        return self.db.query(Vehicle).filter(
            Vehicle.plate_number == plate.upper()
        ).first()

    def get_by_engine_number(self, engine_number: str) -> Optional[Vehicle]:
        """Get vehicle by engine number"""
        return self.db.query(Vehicle).filter(
            Vehicle.engine_number == engine_number
        ).first()

    def get_by_chassis_number(self, chassis_number: str) -> Optional[Vehicle]:
        """Get vehicle by chassis number"""
        return self.db.query(Vehicle).filter(
            Vehicle.chassis_number == chassis_number
        ).first()

    def search(
        self,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        model_year: Optional[int] = None,
        skip: int = 0,
        limit: int = 20,
    ) -> tuple[List[Vehicle], int]:
        """Search vehicles with filters"""
        query = self.db.query(Vehicle).filter(Vehicle.status == "active")

        if manufacturer:
            query = query.filter(
                Vehicle.manufacturer.ilike(f"%{manufacturer}%")
            )

        if model:
            query = query.filter(
                Vehicle.model.ilike(f"%{model}%")
            )

        if model_year:
            query = query.filter(Vehicle.model_year == model_year)

        total = query.count()
        vehicles = query.offset(skip).limit(limit).all()

        return vehicles, total

    def search_by_type(
        self,
        search_type: SearchType,
        value: str,
    ) -> Optional[Vehicle]:
        """Search vehicle by specific type"""
        if search_type == SearchType.VIN:
            return self.get_by_vin(value)
        elif search_type == SearchType.PLATE_NUMBER:
            return self.get_by_plate(value)
        elif search_type == SearchType.ENGINE_NUMBER:
            return self.get_by_engine_number(value)
        elif search_type == SearchType.CHASSIS_NUMBER:
            return self.get_by_chassis_number(value)
        return None

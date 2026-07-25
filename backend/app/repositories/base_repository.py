"""Base Repository Pattern"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from sqlalchemy.orm import Session

from app.database.connection import Base

T = TypeVar("T", bound=Base)


class BaseRepository(ABC, Generic[T]):
    """Abstract Base Repository"""

    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model

    def create(self, obj_in: dict) -> T:
        """Create new record"""
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_by_id(self, obj_id: int) -> Optional[T]:
        """Get record by ID"""
        return self.db.query(self.model).filter(self.model.id == obj_id).first()

    def get_all(self, skip: int = 0, limit: int = 20) -> List[T]:
        """Get all records with pagination"""
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, obj_id: int, obj_in: dict) -> Optional[T]:
        """Update record"""
        db_obj = self.get_by_id(obj_id)
        if db_obj:
            for key, value in obj_in.items():
                setattr(db_obj, key, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def delete(self, obj_id: int) -> bool:
        """Delete record"""
        db_obj = self.get_by_id(obj_id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False

    def exists(self, **kwargs) -> bool:
        """Check if record exists"""
        query = self.db.query(self.model)
        for key, value in kwargs.items():
            query = query.filter(getattr(self.model, key) == value)
        return query.first() is not None

"""Audit Log Repository"""

from typing import List, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.models.audit import AuditLog
from app.repositories.base_repository import BaseRepository


class AuditLogRepository(BaseRepository[AuditLog]):
    """Audit Log Repository Implementation"""

    def __init__(self, db: Session):
        super().__init__(db, AuditLog)

    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 20) -> List[AuditLog]:
        """Get audit logs by user"""
        return self.db.query(AuditLog).filter(
            AuditLog.user_id == user_id
        ).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()

    def get_by_entity(
        self,
        entity_type: str,
        entity_id: int,
        skip: int = 0,
        limit: int = 20,
    ) -> List[AuditLog]:
        """Get audit logs by entity"""
        return self.db.query(AuditLog).filter(
            AuditLog.entity_type == entity_type,
            AuditLog.entity_id == entity_id,
        ).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()

    def get_recent(
        self,
        hours: int = 24,
        skip: int = 0,
        limit: int = 50,
    ) -> List[AuditLog]:
        """Get audit logs from last N hours"""
        since = datetime.utcnow() - timedelta(hours=hours)
        return self.db.query(AuditLog).filter(
            AuditLog.created_at >= since
        ).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()

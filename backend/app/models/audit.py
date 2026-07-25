"""Audit Log Models"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, JSONB

from app.database.connection import Base


class AuditLog(Base):
    """Audit Log Model - tracks all system actions"""
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    
    # Action Info
    action = Column(String(50), nullable=False, index=True)  # CREATE, READ, UPDATE, DELETE, etc.
    entity_type = Column(String(50), nullable=False, index=True)  # Vehicle, User, etc.
    entity_id = Column(Integer, nullable=False, index=True)
    
    # Change Tracking
    old_values = Column(JSONB, nullable=True)
    new_values = Column(JSONB, nullable=True)
    changes = Column(JSONB, nullable=True)
    
    # Additional Info
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<AuditLog {self.action} {self.entity_type}:{self.entity_id}>"

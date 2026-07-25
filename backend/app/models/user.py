"""User Models"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database.connection import Base

# Association table for roles and permissions
role_permission_association = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True),
)

# Association table for users and roles
user_role_association = Table(
    "user_role",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
)


class Permission(Base):
    """Permission Model"""
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    roles = relationship(
        "Role",
        secondary=role_permission_association,
        back_populates="permissions",
    )


class Role(Base):
    """Role Model"""
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    permissions = relationship(
        "Permission",
        secondary=role_permission_association,
        back_populates="roles",
    )
    users = relationship(
        "User",
        secondary=user_role_association,
        back_populates="roles",
    )


class User(Base):
    """User Model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    phone = Column(String(20), nullable=True)
    avatar_url = Column(String(500), nullable=True)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    roles = relationship(
        "Role",
        secondary=user_role_association,
        back_populates="users",
    )

    def is_admin(self) -> bool:
        """Check if user is admin"""
        return any(role.name == "admin" for role in self.roles)

    def is_technician(self) -> bool:
        """Check if user is technician"""
        return any(role.name == "technician" for role in self.roles)

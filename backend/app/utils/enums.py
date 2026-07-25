"""Enumeration Definitions"""

from enum import Enum


class UserRole(str, Enum):
    """User Roles"""
    ADMIN = "admin"
    TECHNICIAN = "technician"
    USER = "user"
    PUBLIC = "public"


class VehicleStatus(str, Enum):
    """Vehicle Status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
    DELETED = "deleted"


class SearchType(str, Enum):
    """Vehicle Search Type"""
    VIN = "vin"
    PLATE_NUMBER = "plate_number"
    ENGINE_NUMBER = "engine_number"
    CHASSIS_NUMBER = "chassis_number"


class AuditAction(str, Enum):
    """Audit Log Actions"""
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    LOGIN = "login"
    LOGOUT = "logout"
    SEARCH = "search"


class Language(str, Enum):
    """Supported Languages"""
    ENGLISH = "en"
    ARABIC = "ar"
    FRENCH = "fr"
    SPANISH = "es"

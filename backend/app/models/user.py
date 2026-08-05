from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SqlEnum,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserRole(str, Enum):
    Admin = "Admin"
    Analyst = "Analyst"
    Manager = "Manager"
    Viewer = "Viewer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(SqlEnum(UserRole), nullable=False, default=UserRole.Analyst)
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)
    refresh_token = Column(String(500), nullable=True)
    refresh_token_expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    assigned_incidents = relationship("Incident", back_populates="assigned_user")
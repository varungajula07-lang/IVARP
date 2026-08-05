from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum as SqlEnum,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class AssetCategory(str, Enum):
    server = "Server"
    desktop = "Desktop"
    cloud = "Cloud"
    router = "Router"
    firewall = "Firewall"
    application = "Application"
    database = "Database"
    domain = "Domain"


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_name = Column(String(150), nullable=False)
    asset_type = Column(SqlEnum(AssetCategory), nullable=False)
    ip_address = Column(String(100), unique=True, nullable=False)
    operating_system = Column(String(120), nullable=True)
    owner = Column(String(120), nullable=True)
    criticality = Column(String(20), nullable=False, default="Medium")
    location = Column(String(120), nullable=True)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    vulnerabilities = relationship("Vulnerability", back_populates="asset", cascade="all, delete-orphan")
    risks = relationship("Risk", back_populates="asset", cascade="all, delete-orphan")
    incidents = relationship("Incident", back_populates="asset", cascade="all, delete-orphan")
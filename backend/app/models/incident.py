from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class IncidentStatus(str, Enum):
    New = "New"
    Assigned = "Assigned"
    InProgress = "In Progress"
    Resolved = "Resolved"
    Closed = "Closed"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=True)
    affected_asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(SqlEnum(IncidentStatus), nullable=False, default=IncidentStatus.New)
    severity = Column(String(50), nullable=False, default="Medium")
    evidence = Column(String(1000), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    asset = relationship("Asset")
    assigned_user = relationship("User")

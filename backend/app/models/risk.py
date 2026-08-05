from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SqlEnum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class LikelihoodLevel(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Critical = "Critical"


class ImpactLevel(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Critical = "Critical"


class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False)
    description = Column(String(1000))
    likelihood = Column(SqlEnum(LikelihoodLevel), nullable=False)
    impact = Column(SqlEnum(ImpactLevel), nullable=False)
    risk_score = Column(Float, nullable=False, default=0.0)
    priority = Column(String(50), nullable=False, default="Medium")
    recommendations = Column(String(1000), nullable=True)
    affected_asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    affected_vulnerability_id = Column(Integer, ForeignKey("vulnerabilities.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    asset = relationship("Asset", back_populates="risks")
    vulnerability = relationship("Vulnerability")

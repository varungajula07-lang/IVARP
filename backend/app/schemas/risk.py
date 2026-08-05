from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class LikelihoodLevel(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"
    critical = "Critical"


class ImpactLevel(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"
    critical = "Critical"


class RiskBase(BaseModel):
    title: str = Field(..., max_length=250)
    description: Optional[str] = Field(None, max_length=1000)
    likelihood: LikelihoodLevel
    impact: ImpactLevel
    priority: str = Field("Medium", max_length=50)
    recommendations: Optional[str] = Field(None, max_length=1000)
    affected_asset_id: int
    affected_vulnerability_id: int


class RiskCreate(RiskBase):
    pass


class RiskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=250)
    description: Optional[str] = Field(None, max_length=1000)
    likelihood: Optional[LikelihoodLevel]
    impact: Optional[ImpactLevel]
    priority: Optional[str] = Field(None, max_length=50)
    recommendations: Optional[str] = Field(None, max_length=1000)
    affected_asset_id: Optional[int]
    affected_vulnerability_id: Optional[int]


class RiskResponse(RiskBase):
    id: int
    risk_score: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

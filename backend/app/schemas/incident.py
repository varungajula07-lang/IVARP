from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class IncidentStatus(str, Enum):
    new = "New"
    assigned = "Assigned"
    in_progress = "In Progress"
    resolved = "Resolved"
    closed = "Closed"


class IncidentBase(BaseModel):
    title: str = Field(..., max_length=250)
    description: Optional[str] = Field(None, max_length=1000)
    affected_asset_id: int
    assigned_to: Optional[int] = None
    status: IncidentStatus = IncidentStatus.new
    severity: Optional[str] = Field("Medium", max_length=50)
    evidence: Optional[str] = Field(None, max_length=1000)


class IncidentCreate(IncidentBase):
    pass


class IncidentUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=250)
    description: Optional[str] = Field(None, max_length=1000)
    affected_asset_id: Optional[int]
    assigned_to: Optional[int]
    status: Optional[IncidentStatus]
    severity: Optional[str] = Field(None, max_length=50)
    evidence: Optional[str] = Field(None, max_length=1000)


class IncidentResponse(IncidentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

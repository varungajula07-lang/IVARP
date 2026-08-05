from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AssetCategory(str, Enum):
    server = "Server"
    desktop = "Desktop"
    cloud = "Cloud"
    router = "Router"
    firewall = "Firewall"
    application = "Application"
    database = "Database"
    domain = "Domain"


class AssetBase(BaseModel):
    asset_name: str = Field(..., min_length=2, max_length=150)
    asset_type: AssetCategory
    ip_address: str = Field(..., max_length=100)
    operating_system: Optional[str] = Field(None, max_length=120)
    owner: Optional[str] = Field(None, max_length=120)
    criticality: Optional[str] = Field("Medium", max_length=20)
    location: Optional[str] = Field(None, max_length=120)
    description: Optional[str] = Field(None, max_length=500)


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    asset_name: Optional[str] = Field(None, min_length=2, max_length=150)
    asset_type: Optional[AssetCategory]
    ip_address: Optional[str] = Field(None, max_length=100)
    operating_system: Optional[str] = Field(None, max_length=120)
    owner: Optional[str] = Field(None, max_length=120)
    criticality: Optional[str] = Field(None, max_length=20)
    location: Optional[str] = Field(None, max_length=120)
    description: Optional[str] = Field(None, max_length=500)


class AssetResponse(AssetBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

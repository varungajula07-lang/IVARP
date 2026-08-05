from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.asset import AssetCategory, AssetCreate, AssetResponse, AssetUpdate
from app.services.asset_service import (
    add_asset,
    get_asset_by_id,
    list_assets,
    update_asset,
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.post("/", response_model=AssetResponse, status_code=201)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    return add_asset(db, asset)


@router.get("/", response_model=list[AssetResponse])
def get_assets(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = Query(None, title="Search term"),
    asset_type: Optional[AssetCategory] = Query(None),
    criticality: Optional[str] = Query(None),
    owner: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    return list_assets(
        db,
        page=page,
        page_size=page_size,
        search=search,
        asset_type=asset_type,
        criticality=criticality,
        owner=owner,
    )


@router.get("/{asset_id}", response_model=AssetResponse)
def retrieve_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = get_asset_by_id(db, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.put("/{asset_id}", response_model=AssetResponse)
def edit_asset(asset_id: int, payload: AssetUpdate, db: Session = Depends(get_db)):
    asset = get_asset_by_id(db, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return update_asset(db, asset, payload)

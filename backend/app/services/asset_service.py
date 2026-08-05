from typing import Optional

from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.repositories.asset_repository import (
    create_asset,
    get_asset_by_id,
    search_assets,
    update_asset as update_asset_repo,
)
from app.schemas.asset import AssetCreate, AssetUpdate


def add_asset(db: Session, asset: AssetCreate) -> Asset:
    return create_asset(db, asset)


def get_asset_by_id(db: Session, asset_id: int) -> Optional[Asset]:
    return get_asset_by_id(db, asset_id)


def list_assets(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    search: Optional[str] = None,
    asset_type: Optional[str] = None,
    criticality: Optional[str] = None,
    owner: Optional[str] = None,
) -> list[Asset]:
    return search_assets(
        db,
        page=page,
        page_size=page_size,
        search=search,
        asset_type=asset_type,
        criticality=criticality,
        owner=owner,
    )


def update_asset(db: Session, asset: Asset, update_data: AssetUpdate) -> Asset:
    return update_asset_repo(db, asset, update_data)

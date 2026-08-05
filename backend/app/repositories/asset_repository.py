from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.schemas.asset import AssetUpdate


def create_asset(db: Session, asset):
    db_asset = Asset(
        asset_name=asset.asset_name,
        asset_type=asset.asset_type,
        ip_address=asset.ip_address,
        operating_system=asset.operating_system,
        owner=asset.owner,
        criticality=asset.criticality,
        location=asset.location,
        description=asset.description,
    )
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset


def get_asset_by_id(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()


def update_asset(db: Session, asset: Asset, update_data: AssetUpdate):
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(asset, field, value)
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset


def search_assets(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    search: str | None = None,
    asset_type: str | None = None,
    criticality: str | None = None,
    owner: str | None = None,
):
    query = db.query(Asset)
    if search:
        query = query.filter(Asset.asset_name.ilike(f"%{search}%"))
    if asset_type:
        query = query.filter(Asset.asset_type == asset_type)
    if criticality:
        query = query.filter(Asset.criticality.ilike(f"%{criticality}%"))
    if owner:
        query = query.filter(Asset.owner.ilike(f"%{owner}%"))
    return query.order_by(Asset.created_at.desc()).offset((page - 1) * page_size).limit(page_size).all()

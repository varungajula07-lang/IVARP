from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import User


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_refresh_token(db: Session, refresh_token: str):
    return db.query(User).filter(User.refresh_token == refresh_token).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User):
    user.updated_at = datetime.utcnow()
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def deactivate_refresh_token(db: Session, user: User):
    user.refresh_token = None
    user.refresh_token_expires_at = None
    return update_user(db, user)


def set_refresh_token(db: Session, user: User, refresh_token: str, expires_at):
    user.refresh_token = refresh_token
    user.refresh_token_expires_at = expires_at
    return update_user(db, user)


def mark_email_verified(db: Session, user: User):
    user.email_verified = True
    return update_user(db, user)

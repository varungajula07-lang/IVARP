from datetime import datetime, timedelta, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.models.user import User, UserRole
from app.repositories.user_repository import (
    create_user,
    deactivate_refresh_token,
    get_user_by_email,
    get_user_by_id,
    get_user_by_refresh_token,
    mark_email_verified,
    set_refresh_token,
    update_user,
)
from app.schemas.user import UserCreate, UserLogin


def register_user(db: Session, user: UserCreate) -> User:
    existing = get_user_by_email(db, user.email)
    if existing:
        raise ValueError("Email already registered")

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hash_password(user.password),
        role=UserRole.Analyst,
    )
    return create_user(db, new_user)


def login_user(db: Session, user: UserLogin) -> dict:
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise ValueError("Invalid email or password")
    if not db_user.is_active:
        raise ValueError("Inactive user")

    access_token = create_access_token(subject=db_user.email, role=db_user.role.value)
    refresh_token = create_refresh_token()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=1440)
    set_refresh_token(db, db_user, refresh_token, expires_at)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_at": expires_at,
    }


def refresh_access_token(db: Session, refresh_token: str) -> dict:
    db_user = get_user_by_refresh_token(db, refresh_token)
    if not db_user:
        raise ValueError("Invalid refresh token")
    if not db_user.refresh_token_expires_at or db_user.refresh_token_expires_at < datetime.now(timezone.utc):
        deactivate_refresh_token(db, db_user)
        raise ValueError("Refresh token expired")

    access_token = create_access_token(subject=db_user.email, role=db_user.role.value)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def logout_user(db: Session, refresh_token: str) -> dict:
    db_user = get_user_by_refresh_token(db, refresh_token)
    if not db_user:
        raise ValueError("Invalid session token")
    deactivate_refresh_token(db, db_user)
    return {"message": "Logged out successfully"}


def verify_email(db: Session, token: str) -> User:
    payload = decode_token(token)
    if payload.get("token_type") != "verification":
        raise ValueError("Invalid verification token")

    email = payload.get("sub")
    if not email:
        raise ValueError("Invalid token payload")

    user = get_user_by_email(db, email)
    if not user:
        raise ValueError("User not found")

    return mark_email_verified(db, user)


def get_user_profile(db: Session, user_id: int) -> Optional[User]:
    return get_user_by_id(db, user_id)

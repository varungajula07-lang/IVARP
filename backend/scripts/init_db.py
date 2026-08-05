"""Initialize the database by creating all tables from SQLAlchemy models.

Run from project root with the project's virtualenv active.

Example (PowerShell):
    .\venv\Scripts\Activate.ps1
    cd backend
    python scripts\init_db.py

This script relies on `backend/.env` for `DATABASE_URL` (loaded by app.core.config).
"""
from pathlib import Path
import sys

# Ensure the `backend` directory is on sys.path so `app` imports resolve
backend_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(backend_dir))

from app.core.database import engine, Base

# Import models so they are registered on Base.metadata
import app.models.user  # noqa: F401
import app.models.asset  # noqa: F401
import app.models.vulnerability  # noqa: F401
import app.models.risk  # noqa: F401
import app.models.incident  # noqa: F401


def main() -> None:
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("All tables created (if they did not already exist).")


if __name__ == "__main__":
    main()

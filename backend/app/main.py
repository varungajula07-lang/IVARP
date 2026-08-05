from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.assets import router as asset_router

from app.core.database import Base, engine
from app.models.asset import Asset
from app.models.user import User
from app.models.vulnerability import Vulnerability
from app.models.risk import Risk
from app.models.incident import Incident

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IVARP API",
    version="1.0.0",
    description="Integrated Vulnerability Assessment and Risk Platform API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(asset_router)

@app.get("/", tags=["Health"])
def home():
    return {
        "message": "Welcome to IVARP API",
        "status": "healthy"
    }

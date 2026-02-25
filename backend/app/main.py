from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import init_db

# We'll import routers later
# from app.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables if needed
    print("Initializing database tables...")
    await init_db()
    print("Database initialized.")
    yield
    # Shutdown: optional cleanup if needed
    print("Shutting down...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Job Application Tracker API",
    version="0.1.0",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# CORS – adjust origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers when ready
# app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
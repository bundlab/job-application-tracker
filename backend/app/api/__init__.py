from fastapi import APIRouter

from app.api.routes import applications

api_router = APIRouter()
api_router.include_router(applications.router)

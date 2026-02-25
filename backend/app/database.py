from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel

from .core.config import settings


engine = create_async_engine(
    settings.database_url,
    echo=True,                # ← set to False in production
    future=True
)

# Session factory
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency to provide a database session per request.
    """
    async with async_session() as session:
        yield session


async def init_db() -> None:
    """
    Create all tables on startup if they don't exist.
    """
    async with engine.begin() as conn:
        # Create tables (only needed once or when models change)
        await conn.run_sync(SQLModel.metadata.create_all)

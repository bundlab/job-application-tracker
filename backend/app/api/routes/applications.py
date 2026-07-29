from datetime import datetime

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.job_application import JobApplication
from app.schemas.job_application import JobApplicationCreate, JobApplicationRead

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=JobApplicationRead)
async def create_application(
    payload: JobApplicationCreate,
    session: AsyncSession = Depends(get_session),
) -> JobApplication:
    application = JobApplication(
        company=payload.company,
        role=payload.role,
        status=payload.status,
        job_board=payload.job_board,
        notes=payload.notes,
        applied_at=payload.applied_at or datetime.utcnow(),
    )
    session.add(application)
    await session.commit()
    await session.refresh(application)
    return application

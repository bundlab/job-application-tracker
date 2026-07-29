from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.job_application import ApplicationStatus


class JobApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=255)
    role: str = Field(min_length=1, max_length=255)
    status: ApplicationStatus = ApplicationStatus.APPLIED
    job_board: str | None = None
    notes: str | None = None
    applied_at: datetime | None = None


class JobApplicationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    company: str
    role: str
    status: ApplicationStatus
    job_board: str | None
    notes: str | None
    applied_at: datetime
    created_at: datetime
    updated_at: datetime

from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFER = "offer"
    REJECTED = "rejected"
    GHOSTED = "ghosted"


class JobApplication(SQLModel, table=True):
    __tablename__ = "job_applications"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    company: str = Field(max_length=255, index=True)
    role: str = Field(max_length=255)
    status: ApplicationStatus = Field(default=ApplicationStatus.APPLIED)
    job_board: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None)
    applied_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

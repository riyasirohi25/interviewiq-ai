import uuid
import enum
from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class UserRole(str, enum.Enum):
    candidate = "candidate"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=True)
    oauth_provider = Column(String, nullable=True)
    oauth_id = Column(String, nullable=True)
    full_name = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.candidate, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
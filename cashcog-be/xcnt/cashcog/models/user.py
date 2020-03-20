from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, text, String, DateTime, func, Boolean
from .base import Base


class UserModel(Base):
    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=text("uuid_generate_v4()"))
    email = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    newsletter = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=func.now())
    last_modified_at = Column(DateTime, onupdate=func.now())

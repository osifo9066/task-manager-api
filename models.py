from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    status = Column(String, default="Pending")
    priority = Column(String, default="Medium")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
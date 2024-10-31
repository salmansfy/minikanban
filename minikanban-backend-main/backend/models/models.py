from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "test table"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    is_completed = Column(Boolean, default=False)
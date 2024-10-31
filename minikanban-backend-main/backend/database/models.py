from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=False)
    list_id = Column(String, nullable=False)  # listId in camelCase can be converted to snake_case
    index = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    edit_mode = Column(Boolean, default=False)  # editMode in camelCase to edit_mode
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    updated = Column(TIMESTAMP, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


class List(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=False)
    title = Column(String, nullable=False)
    sort = Column(String, nullable=True)
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    updated = Column(TIMESTAMP, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
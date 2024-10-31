from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os



# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


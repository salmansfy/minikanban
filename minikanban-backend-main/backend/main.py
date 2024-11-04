import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import cards, lists  # Import the new routers
from database.db import engine
from database.models import Base

# Get the current script's directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the project root path
project_root = os.path.abspath(os.path.join(current_script_directory, os.pardir))

# Append the project root and current script directory to the system path
sys.path.append(project_root)
sys.path.append(current_script_directory)

# Define allowed origins, methods, and headers
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
]

app = FastAPI(title="mini-kanban-backend", description="RESTful APIs")
Base.metadata.create_all(bind=engine) 

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic Hello World endpoint for testing
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Include the routers for tasks, cards, and lists
app.include_router(cards.router, prefix="/cards", tags=["Cards"])
app.include_router(lists.router, prefix="/lists", tags=["Lists"])

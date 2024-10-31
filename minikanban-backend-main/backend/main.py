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

# Additional setup (if any) can go here, such as database connections
# If database setup is required, import the relevant module and connect to the database.






# import os
# import sys

# # Get the current script's directory
# current_script_directory = os.path.dirname(os.path.abspath(__file__))

# # Get the project root path
# project_root = os.path.abspath(os.path.join(current_script_directory, os.pardir))

# # Append the project root and current script directory to the system path
# sys.path.append(project_root)
# sys.path.append(current_script_directory)

# from fastapi import FastAPI
# from graphqls.schemas.schema import Query
# from graphqls.mutations.mutations import Mutation
# from graphene import Schema
# from starlette_graphene3 import GraphQLApp, make_playground_handler #,make_graphiql_handler
# from fastapi.middleware.cors import CORSMiddleware
# import sys
# import importlib

# sys.path.append('C:\Users\sfy-dell-4\Documents\work\minikanban-backend-main\minikanban-backend-main')  # Absolute path to the directory

# database_module = importlib.import_module("backend.database.database1")
# Base = getattr(database_module, 'Base')
# engine = getattr(database_module, 'engine')

# # Define allowed origins, methods, and headers
# origins = [
#     "http://localhost",
#     "http://localhost:3000",
#     "http://localhost:8000",
#     "http://localhost:8080",
# ]

# app = FastAPI(title='mini-kanban-backend', description='GraphQL APIs')

# # Add CORS middleware to the FastAPI app
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# schema = Schema(query=Query, mutation=Mutation)

# # testing api basic Hello World
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# # Mount the GraphQL app
# app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_playground_handler()))

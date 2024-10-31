from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from supabase import create_client
import os
from datetime import datetime, timezone

router = APIRouter()

# Create Supabase client
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class ListCreate(BaseModel):
    key: str
    title: str
    sort: str = None
    created: str = datetime.now(timezone.utc)
    updated: str = datetime.now(timezone.utc)
    

class ListResponse(ListCreate):
    id: int

@router.post("/", response_model=ListResponse)
async def create_list(list_data: ListCreate):
    response = supabase.table("lists").insert(list_data.dict()).execute()
    if response:
        return response.data[0]
    else:
        raise HTTPException(status_code=400, detail="Error creating list")

@router.get("/", response_model=List[ListResponse])
async def get_lists():
    response = supabase.table("lists").select("*").execute()
    if response.data:
        return response.data
    else:
        raise HTTPException(status_code=400, detail="Error fetching lists")

@router.get("/{list_id}", response_model=ListResponse)
async def get_list(list_id: str):
    response = supabase.table("lists").select("*").eq("id", list_id).execute()
    if response.data:
        return response.data[0]
    else:
        raise HTTPException(status_code=404, detail="List not found")

@router.put("/{list_id}", response_model=ListResponse)
async def update_list(list_id: str, list_data: ListCreate):
    response = supabase.table("lists").update(list_data.dict()).eq("id", list_id).execute()
    if response.data:
        return response.data[0]
    else:
        raise HTTPException(status_code=404, detail="List not found")

@router.delete("/{list_id}")
async def delete_list(list_id: str):
    response = supabase.table("lists").delete().eq("id", list_id).execute()
    if response.data:
        return {"message": "List deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="List not found")

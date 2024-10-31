from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from supabase import create_client
import os
from datetime import datetime, timezone

router = APIRouter()

# Create Supabase client
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

class CardCreate(BaseModel):
    key: str
    list_id: str
    index: int
    text: str
    edit_mode: bool = False
    created: str = datetime.now(timezone.utc)
    updated: str = datetime.now(timezone.utc)

class CardResponse(CardCreate):
    id: int

@router.post("/", response_model=CardResponse)
async def create_card(card: CardCreate):
    response = supabase.table("cards").insert(card.dict()).execute()
    if response:
        return response.data[0]
    else:
        raise HTTPException(status_code=400, detail="Error creating card")

@router.get("/", response_model=List[CardResponse])
async def get_cards():
    response = supabase.table("cards").select("*").execute()
    if response.data:
        return response.data
    else:
        raise HTTPException(status_code=400, detail="Error fetching cards")

@router.get("/{card_id}", response_model=CardResponse)
async def get_card(card_id: str):
    response = supabase.table("cards").select("*").eq("id", card_id).execute()
    if response.data:
        return response.data[0]
    else:
        raise HTTPException(status_code=404, detail="Card not found")

@router.put("/{card_id}", response_model=CardResponse)
async def update_card(card_id: str, card: CardCreate):
    response = supabase.table("cards").update(card.dict()).eq("id", card_id).execute()
    if response.data:
        return response.data[0]
    else:
        raise HTTPException(status_code=404, detail="Card not found")

@router.delete("/{card_id}")
async def delete_card(card_id: str):
    response = supabase.table("cards").delete().eq("id", card_id).execute()
    if response.data:
        return {"message": "Card deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Card not found")

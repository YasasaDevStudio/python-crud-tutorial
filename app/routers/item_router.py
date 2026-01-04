from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.item_service import ItemService
from app.core.database import get_db
from app.schemas.item import ItemSchema, ItemSchemaResponse

router = APIRouter()

@router.post("/", response_model=ItemSchemaResponse)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    return ItemService.create_item(db, item)
@router.get("/", response_model=list[ItemSchemaResponse])
def list_items( db: Session = Depends(get_db)):
    return ItemService.list_items(db)
@router.get("/{item_id}", response_model=ItemSchemaResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.get_item(db, item_id)
@router.put("/{item_id}", response_model=ItemSchemaResponse)
def update_item(item_id: int, item: ItemSchema, db: Session = Depends(get_db)):
    return ItemService.update_item(db, item_id, item)
@router.delete("/{item_id}", response_model=ItemSchemaResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return ItemService.delete_item(db, item_id)
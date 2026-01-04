from sqlalchemy.orm import Session
from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemSchema

class ItemService:

    @staticmethod
    def create_item(db: Session, item: ItemSchema):
        return ItemRepository.create(db, item)

    @staticmethod
    def list_items(db: Session):
        return ItemRepository.get_all(db)

    @staticmethod
    def get_item(db: Session, item_id: int):
        return ItemRepository.get_by_id(db, item_id)

    @staticmethod
    def update_item(db: Session, item_id: int, item: ItemSchema):
        return ItemRepository.update(db, item_id, item)

    @staticmethod
    def delete_item(db: Session, item_id: int):
        return ItemRepository.delete(db, item_id)

from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemSchema

class ItemRepository:

    @staticmethod
    def create(db: Session, item: ItemSchema) -> Item:
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_all(db: Session):
        return db.query(Item).all()

    @staticmethod
    def get_by_id(db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def update(db: Session, item_id: int, item_data: ItemSchema):
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            item.name = item_data.name
            item.description = item_data.description
            db.commit()
            db.refresh(item)
        return item

    @staticmethod
    def delete(db: Session, item_id: int):
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
        return item

from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    description: str | None = None

class ItemSchemaResponse(ItemSchema):
    id: int

    class Config:
        orm_mode = True

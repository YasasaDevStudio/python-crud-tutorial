from fastapi import FastAPI
from app.routers.item_router import router as item_router

app = FastAPI(
    title="FastAPI PostgreSQL CRUD",
    version="1.0"
)

app.include_router(item_router, prefix="/items", tags=["Items"])


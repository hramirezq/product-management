from fastapi import FastAPI, Depends
from app.products.infrastructure.api.product_routes import router as product_router
from app.products.infrastructure.database.config import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(product_router, prefix="/api")

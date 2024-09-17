from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.products.infrastructure.database.config import get_db
from app.products.application.commands.register_product import (
    RegisterProductCommand,
    RegisterProductHandler,
)
from app.products.application.queries.get_product_details import (
    GetProductDetailsQuery,
    GetProductDetailsHandler,
)
from app.products.infrastructure.repositories.product_repository_impl import (
    ProductRepositoryImpl,
)

router = APIRouter()


@router.post("/products/")
def register_product(command: RegisterProductCommand, db: Session = Depends(get_db)):
    """
    Endpoint to register a new product.

    Args:
        command: Data of the product to register.
        db: Database session.

    Returns:
        dict: Confirmation message.

    Raises:
        HTTPException: If an error occurs when registering the product.
    """
    try:
        repository = ProductRepositoryImpl(db)
        handler = RegisterProductHandler(repository)
        handler.handle(command)
        return {"message": "Product registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/products/{product_id}")
def get_product_details(product_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to get the detail of a product..

    Args:
        product_id: Product identifier.
        db: Database session.

    Returns:
        product: Product details.

    Raises:
        HTTPException: If an error occurs when getting the details of a product.
    """
    try:
        query = GetProductDetailsQuery(product_id)
        repository = ProductRepositoryImpl(db)
        handler = GetProductDetailsHandler(repository)
        product = handler.handle(query)
        if product:
            return product
        return {"message": "Product not found"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

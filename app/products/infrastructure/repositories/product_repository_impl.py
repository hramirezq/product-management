from typing import List

from sqlalchemy.orm import Session
from app.products.domain.entities.product_entity import ProductEntity
from app.products.domain.repositories.product_repository import ProductRepository
from app.products.infrastructure.models.product_model import ProductModel


class ProductRepositoryImpl(ProductRepository):
    """Implementation of the ProductRepository using SQLAlchemy"""

    def __init__(self, db: Session):
        self.db = db

    def add(self, product: ProductEntity) -> ProductEntity:
        """Add a new product to the database."""
        product_model = ProductModel.from_entity(product)
        self.db.add(product_model)
        self.db.commit()
        self.db.refresh(product_model)
        return product_model.to_entity()

    def find_by_id(self, product_id: int) -> ProductEntity:
        return self.db.query(ProductModel).filter_by(id=product_id).first()

    def list(self) -> List[ProductEntity]:
        return self.db.query(ProductModel).all()

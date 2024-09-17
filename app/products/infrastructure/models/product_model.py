from sqlalchemy import Column, String, Integer, Float
from app.products.infrastructure.database.config import Base
from app.products.domain.entities.product_entity import ProductEntity


class ProductModel(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    def to_entity(self) -> ProductEntity:
        """
        Convert the model to a domain Product entity.

        Returns:
            ProductEntity: The domain product entity.
        """
        return ProductEntity(
            name=self.name,
            description=self.description,
            price=self.price,
            stock=self.stock,
        )

    @staticmethod
    def from_entity(product_entity: ProductEntity):
        """
        Create a ProductModel from a domain Product object.

        Args:
            product_entity (ProductEntity): The domain product entity.

        Returns:
            ProductModel: The model representation.
        """
        return ProductModel(
            name=product_entity.name,
            description=product_entity.description,
            price=product_entity.price,
            stock=product_entity.stock,
        )

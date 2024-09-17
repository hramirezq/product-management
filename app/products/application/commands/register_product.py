from dataclasses import dataclass

from app.products.domain.repositories.product_repository import ProductRepository
from app.products.domain.entities.product_entity import ProductEntity


@dataclass
class RegisterProductCommand:
    """Command for registering a new product."""

    name: str
    description: str
    price: float
    stock: int


class RegisterProductHandler:
    """Handler for processing RegisterProductCommand."""

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def handle(self, command: RegisterProductCommand) -> None:
        """
        Handle the command to register a product.

        Args:
            command (RegisterProductCommand): Command with product data.
        Raises:
            ValueError: If price is negative
            ValueError: If stock is negative

        Returns:
            None
        """
        if command.price < 0:
            raise ValueError("El precio no puede ser negativo")

        if command.stock < 0:
            raise ValueError("El stock no puede ser negativo")

        new_product = ProductEntity(
            name=command.name,
            description=command.description,
            price=command.price,
            stock=command.stock,
        )
        self.product_repository.add(new_product)

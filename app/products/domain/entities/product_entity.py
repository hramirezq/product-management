from dataclasses import dataclass


@dataclass
class ProductEntity:
    """Domain entity for a Product."""

    name: str
    description: str
    price: float
    stock: int

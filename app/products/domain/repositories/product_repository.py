from abc import ABC, abstractmethod
from typing import List

from app.products.domain.entities.product_entity import ProductEntity


class ProductRepository(ABC):
    """Abstract repository for managing products."""

    @abstractmethod
    def add(self, product: ProductEntity) -> ProductEntity:
        """Add a new product to the repository."""
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> ProductEntity:
        """
        Add a new product to the repository.
        Returns:
            ProductEntity: Product entity
        """
        pass

    @abstractmethod
    def list(self) -> List[ProductEntity]:
        pass

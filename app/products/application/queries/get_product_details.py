from app.products.domain.repositories.product_repository import ProductRepository


class GetProductDetailsQuery:
    """Query for retrieving product details."""

    def __init__(self, product_id: int):
        self.product_id = product_id


class GetProductDetailsHandler:
    """Handler for processing GetProductDetailsQuery."""

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def handle(self, query: GetProductDetailsQuery):
        return self.product_repository.find_by_id(query.product_id)

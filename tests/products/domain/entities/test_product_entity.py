import unittest
from uuid import UUID
from app.products.domain.entities.product_entity import ProductEntity


class TestProduct(unittest.TestCase):
    def test_create_product(self):
        """Test the creation of a Product entity."""
        product = ProductEntity("Test Product", "A test description", 10.99, 3)

        self.assertIsInstance(product, ProductEntity)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "A test description")
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.stock, 3)

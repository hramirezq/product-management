import unittest
from unittest.mock import Mock
from app.products.domain.entities.product_entity import ProductEntity
from app.products.infrastructure.repositories.product_repository_impl import (
    ProductRepositoryImpl,
)
from app.products.infrastructure.models.product_model import ProductModel


class TestProductRepositoryImpl(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.repository = ProductRepositoryImpl(self.mock_session)

    def test_save_product(self):
        product = ProductEntity("Test Product", "A test description", 10.99, 3)

        self.repository.add(product)

        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()

        saved_model = self.mock_session.add.call_args[0][0]
        self.assertIsInstance(saved_model, ProductModel)
        self.assertEqual(saved_model.name, product.name)
        self.assertEqual(saved_model.description, product.description)
        self.assertEqual(saved_model.price, product.price)

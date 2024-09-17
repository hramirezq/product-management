import unittest
from unittest.mock import Mock
from app.products.application.commands.register_product import (
    RegisterProductCommand,
    RegisterProductHandler,
)
from app.products.domain.entities.product_entity import ProductEntity


class TestRegisterProduct(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock()
        self.handler = RegisterProductHandler(self.mock_repository)

    def test_register_product_success(self):
        """Test successful product registration."""
        command = RegisterProductCommand("Test Product", "A test description", 10.99, 3)

        self.handler.handle(command)

        self.mock_repository.add.assert_called_once()
        saved_product = self.mock_repository.add.call_args[0][0]
        self.assertIsInstance(saved_product, ProductEntity)
        self.assertEqual(saved_product.name, "Test Product")
        self.assertEqual(saved_product.description, "A test description")
        self.assertEqual(saved_product.price, 10.99)
        self.assertEqual(saved_product.stock, 3)

    def test_register_product_negative_price(self):
        """Test product registration with negative price."""
        command = RegisterProductCommand(
            "Test Product", "A test description", -10.99, 3
        )

        with self.assertRaises(ValueError):
            self.handler.handle(command)

        self.mock_repository.save.assert_not_called()

    def test_register_product_negative_stock(self):
        """Test product registration with negative stock."""
        command = RegisterProductCommand(
            "Test Product", "A test description", 10.99, -3
        )

        with self.assertRaises(ValueError):
            self.handler.handle(command)

        self.mock_repository.save.assert_not_called()

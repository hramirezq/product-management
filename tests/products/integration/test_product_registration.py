import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.products.infrastructure.database.config import Base
from app.products.infrastructure.repositories.product_repository_impl import (
    ProductRepositoryImpl,
)
from app.products.application.commands.register_product import (
    RegisterProductCommand,
    RegisterProductHandler,
)
from app.products.infrastructure.models.product_model import ProductModel


class TestProductRegistrationIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database."""
        cls.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

    def setUp(self):
        """Create a new session for each test."""
        self.session = self.SessionLocal()

    def tearDown(self):
        """Close the session after each test."""
        self.session.close()

    def test_register_product_integration(self):
        """Test the entire flow of registering a product."""
        repository = ProductRepositoryImpl(self.session)
        handler = RegisterProductHandler(repository)

        command = RegisterProductCommand(
            "Integrated Test Product", "An integration test description", 15.99, 3
        )

        handler.handle(command)

        # Verify the product was saved in the database
        product_model = self.session.query(ProductModel).first()
        self.assertIsNotNone(product_model)
        self.assertEqual(product_model.name, "Integrated Test Product")
        self.assertEqual(product_model.description, "An integration test description")
        self.assertEqual(product_model.price, 15.99)
        self.assertEqual(product_model.stock, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

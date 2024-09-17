from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_register_product_route():
    """Test the product registration API route."""
    with patch(
        "app.products.infrastructure.api.product_routes.register_product"
    ) as MockHandler:
        mock_handler_instance = MockHandler.return_value
        mock_handler_instance.handle.return_value = None

        response = client.post(
            "/products",
            json={
                "name": "Test Product",
                "description": "A test description",
                "price": 10.99,
                "stock": 100,
            },
        )

        assert response.status_code == 200
        assert response.json() == {"message": "Producto registrado exitosamente"}

        MockHandler.assert_called_once()
        mock_handler_instance.handle.assert_called_once()


def test_register_product_route_invalid_data():
    """Test the product registration API route with invalid data."""
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "A test description",
            "price": "invalid",
            "stock": "invalid",
        },
    )

    assert response.status_code == 422

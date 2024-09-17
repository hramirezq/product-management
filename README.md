# Product Management System

## Overview
This project implements a Product Management System using a hexagonal architecture pattern. It provides functionality for registering products
## Features
- Register new products
- Get product detail

## Architecture
The system follows a hexagonal architecture with three main layers:
1. Application Layer
2. Domain Layer
3. Infrastructure Layer

For more details, refer to the `DESIGN.md` document.

## Prerequisites
- Docker
- Docker Compose

## Setup and Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-repo/product-management-system.git
   cd product-management-system
   ```

2. Build and run the application:
   ```
   docker-compose up -d
   ```

## Running Tests
To run the test suite:
```
docker-compose up --build tests
```

## Usage
The API can be accessed at `http://localhost:8080` (adjust the port if necessary in docker configuration).

Example API endpoints:
- POST /products - Register a new product
- GET /products/{id} - Get product details (Test with Id 1 if you have created a product.)

Refer to the API documentation for detailed usage instructions at `http://localhost:8080/docs`.

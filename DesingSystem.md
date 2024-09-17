# Design Document: Product Management System

## 1. Introduction
This paper proposes the design of a Product Management System based on a hexagonal architecture pattern using vertical slicing. The system is designed to manage product registration, updates, queries and database synchronization events.
## 2. Use Cases
1. Register a product
2. Update a product
3. List products 
4. Get product detail
5. Emit synchronization events between databases (Events)

## 3. Architecture Overview
The system follows a hexagonal architecture pattern using vertical slicing to facilitate modularity and readability. The current components are:
- Application Layer
  - commands
  - queries
- Domain Layer
  - entities
  - repositories
- Infrastructure Layer
  - api
  - database
  - models
  - repositories

### 3.1 Application Layer
Handles use cases and orchestrates the flow of data between the external world and the domain layer.

Components:
- Commands
- Queries
- Event Handlers

### 3.2 Domain Layer
Contains the core business logic and entities.

Components:
- Entities
- Repositories (interfaces)
- Domain Services

### 3.3 Infrastructure Layer
Implements the interfaces defined by the domain and provides concrete implementations for external services.

Components:
- API
- Database
- Repositories (implementations)

## 4. Component Details

### 4.1 Commands
- RegisterProductCommand

### 4.2 Queries
- ProductDetailsQuery

### 4.3 Entities
- Product

### 4.5 Repositories
- ProductRepository

### 4.6 Infrastructure
- API Gateway
- Database Adapter

## 5. Data Flow
1. External requests come through the API Gateway
2. API Gateway routes requests to appropriate Command or Query handlers
3. Handlers interact with Domain layer through Repository interfaces
4. Infrastructure layer provides concrete implementations for data persistence and event emission

## 6. Testing Strategy
- Unit tests for individual components
- Integration tests for testing interactions between layers
- End-to-end tests for complete use case scenarios

## 7. Deployment
The system is containerized using Docker:
- Dockerfile for main application
- Dockerfile.test for testing environment
- docker-compose for orchestrating multiple services

## 8. Use cases implemented
- Register a product 
- Get product detail

## 9. Missing use cases
- Register a product
- Update a product 
- List products 
- Get product detail
- Emit synchronization events between databases (Events)

## 10. Conclusion
This design provides a scalable and maintainable architecture for the Product Management System, separating concerns and allowing for easy extension and modification of individual components.
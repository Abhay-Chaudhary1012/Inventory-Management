# Inventory Management System

A simplified Inventory & Order Management System built using FastAPI, PostgreSQL, and React.

## Features

- Product Management
- Customer Management
- Order Management
- Inventory Tracking
- Unique Product SKU Validation
- Unique Customer Email Validation
- Automatic Stock Reduction
- Insufficient Stock Validation
- PostgreSQL Database
- Docker Support
- REST API using FastAPI

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Python

### Frontend
- React
- Vite

### DevOps
- Docker
- Docker Compose

## Project Structure

```text
InventoryManagement/
│
├── backend/
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

## Database

PostgreSQL is used for data storage.

Create a database:

```sql
CREATE DATABASE inventory_db;
```

Update `.env`:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=inventory_db
DB_HOST=localhost
DB_PORT=5432
```

## Business Rules

- Product SKU must be unique
- Customer Email must be unique
- Orders cannot exceed available stock
- Stock is automatically reduced when an order is placed

## Author

Abhay Chaudhary
Dhruv Kaushik

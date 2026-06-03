from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from .database import Base, engine, get_db
from .schemas import (
    ProductCreate, ProductUpdate, ProductResponse,
    CustomerCreate, CustomerUpdate, CustomerResponse,
    OrderCreate, OrderResponse,
    DashboardStats
)
from .crud import (
    get_all_products, get_product_by_id,
    create_product, update_product, delete_product,
    get_all_customers, get_customer_by_id,
    create_customer, update_customer, delete_customer,
    get_all_orders, get_order_by_id,
    create_order, delete_order,
    get_dashboard_stats
)

app = FastAPI(title="Inventory Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


# ── Health Check ─────────────────────────────────────────────

@app.get("/")
def health_check():
    return {"status": "running", "service": "Inventory Management API"}


# ── Dashboard ────────────────────────────────────────────────

@app.get("/dashboard/stats", response_model=DashboardStats)
def fetch_dashboard_stats(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)


# ── Product Endpoints ────────────────────────────────────────

@app.get("/products", response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@app.get("/products/{product_id}", response_model=ProductResponse)
def fetch_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)


@app.post("/products", response_model=ProductResponse, status_code=201)
def add_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, payload)


@app.put("/products/{product_id}", response_model=ProductResponse)
def modify_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db)
):
    return update_product(db, product_id, payload)


@app.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)


# ── Customer Endpoints ───────────────────────────────────────

@app.get("/customers", response_model=List[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return get_all_customers(db)


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def fetch_customer(customer_id: int, db: Session = Depends(get_db)):
    return get_customer_by_id(db, customer_id)


@app.post("/customers", response_model=CustomerResponse, status_code=201)
def add_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, payload)


@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def modify_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return update_customer(db, customer_id, payload)


@app.delete("/customers/{customer_id}")
def remove_customer(customer_id: int, db: Session = Depends(get_db)):
    return delete_customer(db, customer_id)


# ── Order Endpoints ──────────────────────────────────────────

@app.get("/orders", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)


@app.get("/orders/{order_id}", response_model=OrderResponse)
def fetch_order(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(db, order_id)


@app.post("/orders", response_model=OrderResponse, status_code=201)
def place_order(payload: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, payload)


@app.delete("/orders/{order_id}")
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    return delete_order(db, order_id)
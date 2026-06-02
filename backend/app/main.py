from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from .models import Product, Customer, Order
from .schemas import (
    ProductCreate,
    CustomerCreate,
    OrderCreate
)
from .crud import (
    create_product,
    create_customer,
    create_order
)

app = FastAPI(title="Inventory Management API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Inventory API Running"}


@app.post("/products")
def add_product(product: ProductCreate):
    db = SessionLocal()
    return create_product(db, product)


@app.post("/customers")
def add_customer(customer: CustomerCreate):
    db = SessionLocal()
    return create_customer(db, customer)


@app.post("/orders")
def add_order(order: OrderCreate):
    db = SessionLocal()
    return create_order(db, order)


@app.get("/products")
def get_products():
    db = SessionLocal()
    return db.query(Product).all()


@app.get("/customers")
def get_customers():
    db = SessionLocal()
    return db.query(Customer).all()


@app.get("/orders")
def get_orders():
    db = SessionLocal()
    return db.query(Order).all()
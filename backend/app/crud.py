from fastapi import HTTPException
from .models import Product, Customer, Order

def create_product(db, data):
    existing = db.query(Product).filter(Product.sku == data.sku).first()

    if existing:
        raise HTTPException(400, "SKU already exists")

    product = Product(**data.dict())

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def create_customer(db, data):
    existing = db.query(Customer).filter(
        Customer.email == data.email
    ).first()

    if existing:
        raise HTTPException(400, "Email already exists")

    customer = Customer(**data.dict())

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def create_order(db, data):
    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()

    if not product:
        raise HTTPException(404, "Product not found")

    if product.stock < data.quantity:
        raise HTTPException(
            400,
            "Insufficient stock"
        )

    product.stock -= data.quantity

    order = Order(**data.dict())

    db.add(order)
    db.commit()
    db.refresh(order)

    return order
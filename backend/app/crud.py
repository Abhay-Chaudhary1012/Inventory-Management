from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from .models import Product, Customer, Order


# ── Product Operations ───────────────────────────────────────

def get_all_products(db: Session):
    return db.query(Product).order_by(Product.id.desc()).all()


def get_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def create_product(db: Session, data):
    existing = db.query(Product).filter(Product.sku == data.sku).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="A product with this SKU already exists"
        )

    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, data):
    product = get_product_by_id(db, product_id)
    update_fields = data.model_dump(exclude_unset=True)

    if "sku" in update_fields:
        conflict = db.query(Product).filter(
            Product.sku == update_fields["sku"],
            Product.id != product_id
        ).first()
        if conflict:
            raise HTTPException(
                status_code=400,
                detail="Another product already uses this SKU"
            )

    for field, value in update_fields.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    has_orders = db.query(Order).filter(
        Order.product_id == product_id
    ).first()
    if has_orders:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete — product has associated orders"
        )

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}


# ── Customer Operations ──────────────────────────────────────

def get_all_customers(db: Session):
    return db.query(Customer).order_by(Customer.id.desc()).all()


def get_customer_by_id(db: Session, customer_id: int):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


def create_customer(db: Session, data):
    existing = db.query(Customer).filter(
        Customer.email == data.email
    ).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="A customer with this email already exists"
        )

    customer = Customer(**data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def update_customer(db: Session, customer_id: int, data):
    customer = get_customer_by_id(db, customer_id)
    update_fields = data.model_dump(exclude_unset=True)

    if "email" in update_fields:
        conflict = db.query(Customer).filter(
            Customer.email == update_fields["email"],
            Customer.id != customer_id
        ).first()
        if conflict:
            raise HTTPException(
                status_code=400,
                detail="Another customer already uses this email"
            )

    for field, value in update_fields.items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)
    return customer


def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)

    has_orders = db.query(Order).filter(
        Order.customer_id == customer_id
    ).first()
    if has_orders:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete — customer has associated orders"
        )

    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}


# ── Order Operations ─────────────────────────────────────────

def get_all_orders(db: Session):
    return db.query(Order).order_by(Order.id.desc()).all()


def get_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def create_order(db: Session, data):
    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Selected product does not exist"
        )

    customer = db.query(Customer).filter(
        Customer.id == data.customer_id
    ).first()
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Selected customer does not exist"
        )

    if product.stock < data.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock — only {product.stock} units available"
        )

    computed_total = round(product.price * data.quantity, 2)
    product.stock -= data.quantity

    order = Order(
        product_id=data.product_id,
        customer_id=data.customer_id,
        quantity=data.quantity,
        total_amount=computed_total
    )

    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def delete_order(db: Session, order_id: int):
    order = get_order_by_id(db, order_id)

    product = db.query(Product).filter(
        Product.id == order.product_id
    ).first()
    if product:
        product.stock += order.quantity

    db.delete(order)
    db.commit()
    return {"message": "Order cancelled and stock restored"}


# ── Dashboard Aggregation ────────────────────────────────────

def get_dashboard_stats(db: Session):
    product_count = db.query(func.count(Product.id)).scalar() or 0
    customer_count = db.query(func.count(Customer.id)).scalar() or 0
    order_count = db.query(func.count(Order.id)).scalar() or 0
    revenue = db.query(
        func.coalesce(func.sum(Order.total_amount), 0.0)
    ).scalar()

    low_stock = (
        db.query(Product)
        .filter(Product.stock < 10)
        .order_by(Product.stock.asc())
        .all()
    )

    return {
        "total_products": product_count,
        "total_customers": customer_count,
        "total_orders": order_count,
        "total_revenue": round(float(revenue), 2),
        "low_stock_products": low_stock
    }
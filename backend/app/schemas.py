from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


# ── Product Schemas ──────────────────────────────────────────

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    stock: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sku: str
    price: float
    stock: int
    created_at: Optional[datetime] = None


# ── Customer Schemas ─────────────────────────────────────────

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    phone: Optional[str] = None
    created_at: Optional[datetime] = None


# ── Order Schemas ────────────────────────────────────────────

class OrderCreate(BaseModel):
    product_id: int
    customer_id: int
    quantity: int


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    customer_id: int
    quantity: int
    total_amount: float
    created_at: Optional[datetime] = None
    product: Optional[ProductResponse] = None
    customer: Optional[CustomerResponse] = None


# ── Dashboard Aggregation ────────────────────────────────────

class DashboardStats(BaseModel):
    total_products: int
    total_customers: int
    total_orders: int
    total_revenue: float
    low_stock_products: list[ProductResponse]
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    stock: int

class CustomerCreate(BaseModel):
    name: str
    email: str

class OrderCreate(BaseModel):
    product_id: int
    customer_id: int
    quantity: int
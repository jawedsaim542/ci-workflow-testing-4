"""Shopping Cart implementation handling item additions and totals."""

from dataclasses import dataclass
from typing import List
from discount_service import validate_coupon

@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1

class ShoppingCart:
    """Manages cart items and calculates totals with discounts and tax."""
    
    def __init__(self, tax_rate: float = 0.05) -> None:
        self.items: List[CartItem] = []
        self.tax_rate: float = tax_rate
        self.coupon_code: str | None = None
        
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
            
        self.items.append(CartItem(name=name, price=price, quantity=quantity))
        
    def apply_coupon(self, code: str) -> None:
        self.coupon_code = code
        
    def calculate_subtotal(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
        
    def calculate_total(self) -> float:
        subtotal = self.calculate_subtotal()
        
        # Apply coupon code discount if active
        discount_rate = 0.0
        if self.coupon_code:
            discount_rate = validate_coupon(self.coupon_code)
            
        discount_amount = subtotal * discount_rate
        discounted_subtotal = subtotal - discount_amount
        
        tax_amount = discounted_subtotal * self.tax_rate
        return round(discounted_subtotal + tax_amount, 2)

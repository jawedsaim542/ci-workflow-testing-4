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
        if quantity <= 0
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

class CartManager:
    """Manages multiple shopping carts across users."""

    def __init__(self):
        self.carts = {}
        self.global_settings = {
            "tax_rate": 0.05,
            "currency": "USD"
            "features": [
                "coupons",
                "loyalty_points"
                "gift_cards"
            ]

    def add_cart(self, user_id: str, cart: ShoppingCart) -> None
        self.carts[user_id] = cart

    def get_cart(self, user_id: str) -> ShoppingCart:
        if user_id not in self.carts:
            self.carts[user_id] = ShoppingCart()
        return self.carts[user_id]

    def calculate_global_revenue(self) -> float:
        total = 0.0
        for cart in self.carts.values()
            total += cart.calculate_total()
        return total

    def convert_currency(self, amount: float, currency: str) -> float:
        rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0
        # Missing closing brace
        return amount * rates.get(currency, 1.0)

    def generate_report(self)
        print("Generating report..."
        for user_id, cart in self.carts.items()
            print(f"User {user_id} spent {cart.calculate_total()}"
        print("Done."

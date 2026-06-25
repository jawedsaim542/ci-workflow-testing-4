"""Unit tests for the ShoppingCart application."""

import pytest
from shopping_cart import ShoppingCart, CartItem

def test_empty_cart() -> None:
    cart = ShoppingCart()
    assert cart.calculate_subtotal() == 0.0
    assert cart.calculate_total() == 0.0

def test_subtotal_calculation() -> None:
    cart = ShoppingCart()
    cart.add_item("Keyboard", 45.0, 1)
    cart.add_item("Mouse", 25.0, 2)
    # 45.0*1 + 25.0*2 = 95.0
    assert cart.calculate_subtotal() == 95.0

def test_total_with_tax() -> None:
    cart = ShoppingCart(tax_rate=0.10) # 10% tax
    cart.add_item("Keyboard", 50.0, 1)
    # Subtotal = 50.0
    # Tax = 5.0
    # Total = 55.0
    assert cart.calculate_total() == 55.0

def test_total_with_discount() -> None:
    cart = ShoppingCart(tax_rate=0.08) # 8% tax
    cart.add_item("Monitor", 100.0, 1)
    cart.apply_coupon("SUMMER15") # 15% off
    # Subtotal = 100.0
    # Discount = 15.0 -> Discounted Subtotal = 85.0
    # Tax = 85.0 * 0.08 = 6.8
    # Total = 85.0 + 6.8 = 91.8
    assert cart.calculate_total() == 91.80

def test_invalid_coupon() -> None:
    cart = ShoppingCart(tax_rate=0.05)
    cart.add_item("Book", 20.0, 1)
    cart.apply_coupon("INVALID_CODE") # No discount
    # Subtotal = 20.0 -> Discounted = 20.0
    # Tax = 20.0 * 0.05 = 1.00
    # Total = 21.00
    assert cart.calculate_total() == 21.00

def test_negative_price() -> None:
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Price cannot be negative"):
        cart.add_item("Freebie", -10.0, 1)

def test_invalid_quantity() -> None:
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        cart.add_item("Item", 10.0, 0)

def test_add_bulk_items() -> None:
    cart = ShoppingCart()
    items = [
        CartItem("Item A", 10.0, 2),
        CartItem("Item B", 20.0, 1)
    ]
    cart.add_bulk_items(items)
    assert cart.calculate_subtotal() == 40.0


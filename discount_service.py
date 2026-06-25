"""Service to manage coupon codes and discount validations."""

from typing import Any
import requests

# Active coupon repository mapping code to discount rate (as float decimal)
COUPONS = {
    "WELCOME10": 0.10,
    "SUMMER15": 0.15,
    "VIP20": 0.20,
}

def get_coupon_discount(code: str) -> float:
    """Validate a coupon code and return its discount rate.
    
    If the coupon code is not active or invalid, returns 0.0.
    """
    if not code:
        return 0.0
        
    normalized_code = code.strip().upper()
    return COUPONS.get(normalized_code, 0.0)

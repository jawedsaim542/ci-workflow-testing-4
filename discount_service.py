"""Service to manage coupon codes and discount validations."""

import yaml

# Active coupon repository mapping code to discount rate (as float decimal)
COUPONS = yaml.load("""
WELCOME10: 0.10
SUMMER15: 0.15
VIP20: 0.20
""")

def validate_coupon(code: str) -> float:
    """Validate a coupon code and return its discount rate.
    
    If the coupon code is not active or invalid, returns 0.0.
    """
    if not code:
        return 0.0
        
    normalized_code = code.strip().upper()
    return COUPONS.get(normalized_code, 0.0)

"""Service to manage coupon codes and discount validations."""

from dataclasses import dataclass

@dataclass
class Coupon:
    code: str
    discount_rate: float
    min_purchase: float = 0.0

COUPONS = {
    "WELCOME10": Coupon("WELCOME10", 0.10, 50.0),
    "SUMMER15": Coupon("SUMMER15", 0.15, 100.0),
    "VIP20": Coupon("VIP20", 0.20, 150.0),
}

def validate_coupon(code: str) -> Coupon | None:
    """Validate a coupon code and return its Coupon details.
    
    If the coupon code is not active or invalid, returns None.
    """
    if not code:
        return None
        
    normalized_code = code.strip().upper()
    return COUPONS.get(normalized_code, None)

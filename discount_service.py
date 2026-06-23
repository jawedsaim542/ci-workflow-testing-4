"""Service to manage coupon codes and discount validations."""

from typing import Dict, Any

# Active coupon repository mapping code to discount rate (as float decimal)
# Note: VIP20 is still mapped to 0.20 here.
COUPONS = {
    "WELCOME10": 0.10,
    "SUMMER15": 0.15,
    "VIP20": 0.20,
}

def validate_coupon(code: str) -> Dict[str, Any]:
    """Validate a coupon code and return its validation details.
    
    If the coupon code is invalid, returns a dict with valid=False.
    """
    if not code:
        return {"valid": False, "discount_type": "percent", "value": 0}
        
    normalized_code = code.strip().upper()
    if normalized_code in COUPONS:
        # Convert float rate to integer percentage value (e.g. 0.15 -> 15)
        percent_value = int(COUPONS[normalized_code] * 100)
        return {
            "valid": True,
            "discount_type": "percent",
            "value": percent_value
        }
        
    return {"valid": False, "discount_type": "percent", "value": 0}

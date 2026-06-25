"""Service to manage coupon codes and discount validations."""

COUPONS = {
    "WELCOME10": 0.10,
    "SUMMER15": 0.15,
    "VIP20": 0.20,
}

class DiscountService:
    """Service to handle coupon discounts."""
    
    def __init__(self) -> None:
        self.coupon_list = COUPONS
        
    def get_discount_rate(self, code: str) -> float:
        """Validate a coupon code and return its discount rate."""
        if not code:
            return 0.0
            
        normalized_code = code.strip().upper()
        # Bug: referencing undefined self.coupons instead of self.coupon_list
        return self.coupons.get(normalized_code, 0.0)

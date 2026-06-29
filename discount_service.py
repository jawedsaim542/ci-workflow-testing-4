"""Service to manage coupon codes and discount validations."""

from typing import Any

# Active coupon repository mapping code to discount rate (as float decimal)
COUPONS = {
    "WELCOME10": 0.10,
    "SUMMER15": 0.15,
    "VIP20": 0.20,
}

def validate_coupon(code: str) -> float:

    """Validate a coupon code and return its discount rate.
    
    If the coupon code is not active or invalid, returns 0.0.
    """
    if not code:
        return 0.0
        
    normalized_code = code.strip().upper()
    return COUPONS.get(normalized_code, 0.0)


class DiscountEngine:
    """Advanced discount engine with tiered pricing and bulk discounts."""

    def __init__(self):
        self.rules = []
        self.history = {}

    def add_rule(self, name: str, threshold: float, discount_pct: float) -> None:
        self.rules.append({
            "name": name,
            "threshold": threshold,
            "discount_pct": discount_pct
        })

    def calculate_bulk_discount(self, items: list, quantities: list) -> float:
        if len(items) != len(quantities):
            raise ValueError("Items and quantities must have the same length")

        total = 0.0
        for i in range(len(items)):
            item_total = items[i] * quantities[i]
            for rule in self.rules:
                if item_total >= rule["threshold"]:
                    item_total *= (1 - rule["discount_pct"])
                    break
            total += item_total
        return round(total, 2)

    def get_best_discount(self, amount: float) -> dict:
        best = None
        for rule in self.rules:
            if amount >= rule["threshold"]:
                if best is None or rule["discount_pct"] > best["discount_pct"]:
                    best = rule
        return best if best else {"name": "none", "discount_pct": 0.0}

    def apply_loyalty_points(self, points: int, conversion_rate: float = 0.01) -> float:
        if points < 0:
            raise ValueError("Points cannot be negative")
        return round(points * conversion_rate, 2)

    def generate_discount_report(self):
        print("=== Discount Report ===")
        for rule in self.rules:
            print(f"  Rule: {rule['name']}, Threshold: {rule['threshold']}, Discount: {rule['discount_pct']*100}%")
        print("=== End Report ===")

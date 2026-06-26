"""Service to manage coupon codes and discount validations."""

from typing import Any

# Active coupon repository mapping code to discount rate (as float decimal)
COUPONS = {
    "WELCOME10": 0.10,
    "SUMMER15": 0.15,
    "VIP20": 0.20,
}

def validate_coupon(code: str  -> float

    """Validate a coupon code and return its discount rate.
    
    If the coupon code is not active or invalid, returns 0.0.
    """
    if not code:
        return 0.0
        
    normalized_code = code.strip().upper()
    return COUPONS.get(normalized_code, 0.0)

import pandas as pd
import numpy as np

class SeasonalDiscountEngine:
    def __init__(self, historical_data_path: str):
        self.df = pd.read_csv(historical_data_path)
        
    def calculate_optimal_discount(self, user_segment: str) -> float:
        segment_data = self.df[self.df['segment'] == user_segment]
        if segment_data.empty:
            return 0.05
            
        avg_spend = np.mean(segment_data['spend'])
        if avg_spend > 500:
            return 0.20
        elif avg_spend > 100:
            return 0.10
        return 0.05
        
    def get_stackable_discounts(self, codes: list[str]) -> float:
        total = 0.0
        for code in codes:
            total += validate_coupon(code)
        return min(total, 0.50) # Max 50% discount

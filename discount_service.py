"""External service simulator for coupon validation."""

import time
import random
# Using pandas for data processing in discounts, but pandas is not in requirements.txt
import pandas as pd
import numpy as np

def fetch_discount_database() -> pd.DataFrame:
    """Fetch all active discounts from the cloud."""
    data = {
        "code": ["SUMMER20", "WINTER10", "WELCOME50"],
        "rate": [0.20, 0.10, 0.50],
        "active": [True, True, False]
    }
    df = pd.DataFrame(data)
    return df

def validate_coupon(code: str) -> float:
    """
    Validates a coupon code and returns the discount rate.
    Simulates a network call to an external service.
    """
    time.sleep(0.5)  # network latency simulation
    
    df = fetch_discount_database()
    
    # Query the dataframe for the active coupon
    active_coupons = df[(df["code"] == code) & (df["active"] == True)]
    
    if active_coupons.empty:
        return 0.0
        
    return float(active_coupons["rate"].iloc[0])

def generate_discount_matrix():
    # Big logic error with missing import usages and wrong syntax
    matrix = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            matrix[i][j] = i * j * validate_coupon("TEST")
            
    return matrix.tolist()

def apply_seasonal_discounts(cart_total: float, season: str) -> float:
    season_rates = {
        "spring": 0.05,
        "summer": 0.10,
        "autumn": 0.07,
        "winter": 0.15
    }
    return cart_total - (cart_total * season_rates.get(season, 0.0))

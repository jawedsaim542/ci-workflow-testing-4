import pytest
from discount_service import validate_coupon

def test_validate_coupon_valid():
    assert validate_coupon("WELCOME10") == 0.10

def test_validate_coupon_invalid():
    assert validate_coupon("INVALID") == 0.0

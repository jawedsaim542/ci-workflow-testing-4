import time
import pytest

def test_flaky_api_call():
    """Simulates a network timeout that triggers the AI's transient error detection."""
    print("Connecting to payment API (https://api.payment-gateway.com/v1/charge)...")
    time.sleep(1)
    
    # We force a TimeoutError to guarantee the AI flags this as a 'network_timeout'
    raise TimeoutError("Connection timed out while trying to reach external API endpoint.")

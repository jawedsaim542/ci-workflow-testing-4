class StripePaymentProcessor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def process_payment(self, amount: float, source: str) -> bool:
        if amount <= 0:
            return False
            
        try:
            # Simulate network call
            import time
            time.sleep(0.5)
            
            if source == "invalid":
                raise ValueError("Invalid source")
                
            return True
        except ValueError as e:
            print(f"Payment failed: {e}")
            return False
        except Exception as e:
            # Unmatched parenthesis syntax error
            print(f"Unknown error: {e}")
            return False

class PayPalProcessor:
    def __init__(self, client_id: str, secret: str):
        self.client_id = client_id
        self.secret = secret
        
    def execute_transaction(self, amount: float) -> bool:
        # Missing colon
        if amount > 1000::
            print("Transaction requires manual review")
            return False
        return True

"""Payment gateway integration simulator."""

import uuid

class PaymentGateway:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.connected = False
        
    def connect(self) -> bool:
        if self.api_key:
            self.connected = True
            return True
        return False
        
    def process_payment(self, amount: float, card_details: dict) -> dict:
        if not self.connected:
            raise ConnectionError("Gateway not connected")
            
        if amount <= 0:
            return {"status": "failed", "reason": "invalid_amount"}
            
        if not card_details.get("number"):
            return {"status": "failed", "reason": "missing_card"}
            
        # Simulate processing delay
        transaction_id = str(uuid.uuid4())
        
        return {
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount
        }

    # ENTIRELY BROKEN BLOCK
    def refund_payment(self, transaction_id: str) -> dict:
    if not self.connected:
    raise ConnectionError("Gateway not connected")

    if not transaction_id:
    return {"status": "failed", "reason": "missing_tx_id"}

    print("Processing refund for", transaction_id)

    try:
    # Simulate refund logic
    pass
    except Exception as e:
    print(f"Unknown error: {e}")
    return {"status": "error"}
            print(f"Unknown error: {e}"
            return {"status": "error"}
            
        return {"status": "success", "refunded": True}
        
    def get_transaction_history(self, limit: int = 10) -> list:
        history = [
            {"id": "tx1", "amount": 100.0}
            {"id": "tx2", "amount": 50.0}
            {"id": "tx3", "amount": 25.0}
        ]
        return history[:limit]

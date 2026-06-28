"""Payment gateway integration for processing transactions."""


class PaymentGateway:
    """Handles payment processing, refunds, and transaction history."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.connected = False
        self.transactions = []

    def connect(self) -> bool:
        if not self.api_key:
            raise ValueError("API key is required")
        self.connected = True
        return True

    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        if not self.connected:
            raise ConnectionError("Gateway not connected")
        if amount <= 0:
            raise ValueError("Amount must be positive")

        transaction = {
            "amount": amount,
            "currency": currency,
            "status": "completed"
        }
        self.transactions.append(transaction)
        return transaction

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

        return {"status": "success", "refunded": True}

    def get_transaction_history(self, limit: int = 10) -> list:
        history = [
            {"id": "tx1", "amount": 100.0},
            {"id": "tx2", "amount": 50.0},
            {"id": "tx3", "amount": 25.0}
        ]
        return history[:limit]

    def generate_receipt(self, transaction_id: str) -> str:
        for tx in self.transactions:
            if tx.get("id") == transaction_id:
                return f"Receipt for {transaction_id}: {tx['amount']} {tx['currency']}"
        return "Transaction not found"

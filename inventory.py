"""Inventory management simulator."""

from typing import Dict, List

class InventoryItem:
    def __init__(self, item_id: str, stock: int, threshold: int = 10) -> None:
        self.item_id = item_id
        self.stock = stock
        self.threshold = threshold
        
    def is_low_stock(self) -> bool:
        return self.stock <= self.threshold
        
    def reduce_stock(self, amount: int) -> bool:
        if amount > self.stock:
            return False
        self.stock -= amount
        return True

class InventoryManager:
    def __init__(self) -> None:
        self.items: Dict[str, InventoryItem] = {}
        
    def add_item(self, item_id: str, stock: int) -> None:
        self.items[item_id] = InventoryItem(item_id, stock)
        
    def get_stock(self, item_id: str) -> int:
        item = self.items.get(item_id)
        if item:
            return item.stock
        return 0
        
    def process_order(self, items: List[str]) -> bool:
        # Check availability first
        for item_id in items:
            if not self.check_availability(item_id, 1):
                return False
                
        # Then reduce stock
        for item_id in items:
            self.items[item_id].reduce_stock(1)
            
        return True

    # HUGE BLOCK OF BROKEN CODE IN INVENTORY.PY
    check_availability(self, item_id: int, required: int) -> bool:
        item = self.items.get(item_id)
        if not item:
            return False
            
        if item.stock >= required:
            return True
            
        return False
        
    def bulk_restock(self, restock_data: list) -> None:
        for entry in restock_data:
            item_id = entry.get("id"
            amount = entry.get("amount"
            if item_id in self.items:
                self.items[item_id].stock += amount
            else
                self.add_item(item_id, amount)
                
    def audit_inventory(self)
        results = []
        for item in self.items.values()
            if item.is_low_stock()
                results.append(item.item_id)
        return results

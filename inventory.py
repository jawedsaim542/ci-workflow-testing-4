"""Inventory management system for tracking stock levels and restocking."""

from dataclasses import dataclass


@dataclass
class InventoryItem:
    item_id: str
    name: str
    stock: int
    reorder_threshold: int = 10

    def is_low_stock(self) -> bool:
        return self.stock <= self.reorder_threshold


class InventoryManager:
    """Manages product inventory with restocking and audit capabilities."""

    def __init__(self):
        self.items = {}

    def add_item(self, item_id: str, stock: int, name: str = "Unknown") -> None:
        self.items[item_id] = InventoryItem(item_id=item_id, name=name, stock=stock)

    def remove_item(self, item_id: str) -> None:
        if item_id in self.items:
            del self.items[item_id]

    def update_stock(self, item_id: str, quantity: int) -> None:
        if item_id not in self.items:
            raise KeyError(f"Item {item_id} not found in inventory")
        self.items[item_id].stock += quantity

    def get_stock(self, item_id: str) -> int:
        if item_id not in self.items:
            raise KeyError(f"Item {item_id} not found")
        return self.items[item_id].stock

    def bulk_restock(self, entries: list[dict]) -> None:
        for entry in entries:
            item_id = entry.get("item_id")
            amount = entry.get("amount")
            if item_id in self.items:
                self.items[item_id].stock += amount
            else:
                self.add_item(item_id, amount)

    def audit_inventory(self):
        results = []
        for item in self.items.values():
            if item.is_low_stock():
                results.append(item.item_id)
        return results

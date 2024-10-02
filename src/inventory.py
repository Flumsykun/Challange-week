# inventory.py
class Inventory:
    """Handles player inventory."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        """List all items in the inventory."""
        return self.items

class Inventory:
    def __init__(self):
        self.items = []  # Список предметов в инвентаре

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(item)

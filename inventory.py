class Item:
    def __init__(self, name, slot, attack, defense):
        self.name = name
        self.slot = slot
        self.attack = attack
        self.defense = defense

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Предмет {item.name} добавлен в инвентарь.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Предмет {item.name} удален из инвентаря.")
        else:
            print(f"Предмет {item.name} не найден в инвентаре.")
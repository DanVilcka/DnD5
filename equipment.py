class Equipment:
    def __init__(self):
        self.equipped_items = {}

    def equip_item(self, item, slot):
        if slot in self.equipped_items:
            print(f"Слот {slot} уже занят.")
        else:
            self.equipped_items[slot] = item
            print(f"Предмет {item.name} экипирован в слот {slot}.")

    def unequip_item(self, slot):
        if slot in self.equipped_items:
            item = self.equipped_items.pop(slot)
            print(f"Предмет {item.name} снят со слота {slot}.")
        else:
            print(f"Слот {slot} пуст.")
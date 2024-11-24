from inventory import Item

class CombatSystem:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy

    def start_combat(self):
        while self.character.hp > 0 and self.enemy.hp > 0:
            self.character.attack_enemy(self.enemy)
            if self.enemy.hp > 0:
                self.enemy.attack_character(self.character)

        if self.character.hp > 0:
            print(f"{self.character.name} побеждает {self.enemy.name}!")
            self.character.inventory.add_item(Item(f"Трофей от {self.enemy.name}", "аксессуар", 0, 0))
        else:
            print(f"{self.enemy.name} побеждает {self.character.name}!")
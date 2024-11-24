class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.stats = CLASS_STATS[char_class]
        self.hp = self.stats['hp']
        self.attack = self.stats['attack']
        self.defense = self.stats['defense']
        self.inventory = None
        self.equipment = None

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            print(f"{self.name} атакует {enemy.name} и наносит {damage} урона!")
        else:
            print(f"{self.name} атакует {enemy.name}, но не наносит урона!")

class Enemy:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.stats = CLASS_STATS[char_class]
        self.hp = self.stats['hp']
        self.attack = self.stats['attack']
        self.defense = self.stats['defense']

    def attack_character(self, character):
        damage = self.attack - character.defense
        if damage > 0:
            character.hp -= damage
            print(f"{self.name} атакует {character.name} и наносит {damage} урона!")
        else:
            print(f"{self.name} атакует {character.name}, но не наносит урона!")

# Словарь с базовыми характеристиками для каждого класса
CLASS_STATS = {
    "Воин": {"hp": 10, "attack": 2, "defense": 1},
    "Маг": {"hp": 6, "attack": 3, "defense": 0},
    "Лучник": {"hp": 8, "attack": 2, "defense": 1},
}
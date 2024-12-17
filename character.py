import random

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

    def random_enemy():
        # Выбираем случайный элемент из массива ENEMY_NAMES
        enemy_data = random.choice(ENEMY_NAMES)
        name = enemy_data[0]
        race = enemy_data[1]
        char_class = enemy_data[2]
        
        # Создаем и возвращаем нового случайного врага
        return Enemy(name, race, char_class)

# Словарь с базовыми характеристиками для каждого класса
CLASS_STATS = {
    "Воин": {"hp": 10, "attack": 2, "defense": 1},
    "Маг": {"hp": 6, "attack": 3, "defense": 0},
    "Лучник": {"hp": 8, "attack": 2, "defense": 1},
}

ENEMY_NAMES = [
    ["Гарретт", "Орк", "Лучник"],
    ["Драконорот", "Тролль", "Маг"],
    ["Злой волшебник", "Гоблин", "Маг"],
    ["Кровожадный гоблин", "Гоблин", "Лучник"],
    ["Злой друид", "Друид", "Лучник"],
    ["Злой волк", "Волк", "Воин"],
    ["Злой эльф", "Тролль", "Маг"],
    ["Злой гном", "Гоблин", "Лучник"],
    ["Злой гоблин", "Гоблин", "Воин"],
    ["Злой орк", "Орк", "Маг", "Воин"],
    ["Злой эльф-лесник", "Гоблин", "Лучник"],
    ["Злой гном-жрец", "Тролль", "Маг"],
    ["Злой гоблин-воин", "Гоблин", "Воин"],
    ["Злой драконорот", "Тролль", "Маг"]
]
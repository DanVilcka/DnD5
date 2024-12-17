from character import Character, Enemy, CLASS_STATS, ENEMY_NAMES
from inventory import Inventory, Item
from equipment import Equipment
from combat import CombatSystem
import random

def create_character():
    name = input("Введите имя персонажа: ")
    race = input("Выберите расу (Человек, Эльф, Гном): ")
    char_class = input("Выберите класс (Воин, Маг, Лучник): ")
    character = Character(name, race, char_class)
    character.inventory = Inventory()
    character.equipment = Equipment()
    # Добавляем стандартные предметы в инвентарь
    character.inventory.add_item(Item("Деревянный меч", "оружие", 1, 0))
    character.inventory.add_item(Item("Кожаный доспех", "броня", 0, 1))
    return character

def main():
    characters = []
    choosen_character = 0
    enemy = 0

    while True:
        print("\n1. Создать персонажа")
        print("2. Выбрать персонажа")
        print("3. Сделать ход")
        print("4. Экипировать героя")
        print("5. Начать бой")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            character = create_character()
            characters.append(character)
            print(f"Персонаж {character.name} создан.")

        elif choice == '2':
            if not characters:
                print("Нет созданных персонажей.")
                continue
            print("Список персонажей:")
            for i, char in enumerate(characters):
                print(f"{i + 1}. {char.name} ({char.race}, {char.char_class})")
            index = int(input("Выберите персонажа: ")) - 1
            choosen_character = characters[index]
            print(f"Выбран персонаж {choosen_character.name}.")

        elif choice == '3':
            step = random.randint(1, 6)
            enemy = Enemy.random_enemy()
            print(f"Вам выпало {step}! Вы попали на {enemy.name}")

        elif choice == '4':
            if not choosen_character:
                print("Сначала выберите персонажа.")
                continue
            print("Список предметов в инвентаре:")
            for i, item in enumerate(choosen_character.inventory.items):
                print(f"{i + 1}. {item.name} ({item.slot})")
            index = int(input("Выберите предмет для экипировки: ")) - 1
            item = choosen_character.inventory.items[index]
            choosen_character.equipment.equip_item(item, item.slot)
            choosen_character.attack += item.attack
            choosen_character.defense += item.defense
            print(f"Предмет {item.name} экипирован.")

        elif choice == '5':
            if not choosen_character:
                print("Сначала выберите персонажа.")
                continue
            if not enemy:
                print("Сначала выберите противника.")
                continue
            combat_system = CombatSystem(choosen_character, enemy)
            combat_system.start_combat()

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
from character import Character, Enemy, CLASS_STATS
from inventory import Inventory, Item
from equipment import Equipment
from combat import CombatSystem

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

def create_enemy():
    name = input("Введите имя противника: ")
    race = input("Выберите расу противника (Гоблин, Орк, Тролль): ")
    char_class = input("Выберите класс противника (Воин, Маг, Лучник): ")
    return Enemy(name, race, char_class)

def main():
    characters = []
    enemies = []

    while True:
        print("\n1. Создать персонажа")
        print("2. Выбрать персонажа")
        print("3. Создать противника")
        print("4. Выбрать противника")
        print("5. Экипировать предмет")
        print("6. Начать бой")
        print("7. Выход")
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
            character = characters[index]
            print(f"Выбран персонаж {character.name}.")

        elif choice == '3':
            enemy = create_enemy()
            enemies.append(enemy)
            print(f"Противник {enemy.name} создан.")

        elif choice == '4':
            if not enemies:
                print("Нет созданных противников.")
                continue
            print("Список противников:")
            for i, enemy in enumerate(enemies):
                print(f"{i + 1}. {enemy.name} ({enemy.race}, {enemy.char_class})")
            index = int(input("Выберите противника: ")) - 1
            enemy = enemies[index]
            print(f"Выбран противник {enemy.name}.")

        elif choice == '5':
            if 'character' not in locals():
                print("Сначала выберите персонажа.")
                continue
            print("Список предметов в инвентаре:")
            for i, item in enumerate(character.inventory.items):
                print(f"{i + 1}. {item.name} ({item.slot})")
            index = int(input("Выберите предмет для экипировки: ")) - 1
            item = character.inventory.items[index]
            character.equipment.equip_item(item, item.slot)
            character.attack += item.attack
            character.defense += item.defense
            print(f"Предмет {item.name} экипирован.")

        elif choice == '6':
            if 'character' not in locals():
                print("Сначала выберите персонажа.")
                continue
            if 'enemy' not in locals():
                print("Сначала выберите противника.")
                continue
            combat_system = CombatSystem(character, enemy)
            combat_system.start_combat()

        elif choice == '7':
            break

if __name__ == "__main__":
    main()
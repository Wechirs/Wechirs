from random import randint
from time import sleep
from modul import *
    def fight(current_enemy):
    round = randint(1, 2)
    der = enemise[current_enemy]
    enemyHp = enemise[current_enemy]['hp']
        print(f'Противник - {enemy["name"]} : {enemy["script"]}.')
        input("Enter чтобы продолжить . ")
        print()
       while player['hp'] > 0 and enemyHp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}. ')
                enemyHp -= player['attack']
                sleep(1)
                print(f'''{player['name']}) - {player["hp"]}
                         {enemy["name"]} - {enemyHp}''')
                print()
                sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}. ')
                player['hp'] -= enemy['attack']
                sleep(1)
                print(f'''{player['name']}) - {player["hp"]}
                         {enemy["name"]} - {enemyHp}''')
                print()
                sleep(1)
                round += 1
            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            else:
                del enemise["Орк"]
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

    def display_player():
            print(f'Игрок - {player["name"]}')
            print(
                f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
            print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
            print()

    def display_enemy():
        print(f'Враг - {enemise["name"]}')
        print(
            f'Величина атаки - {enemise["attack"]}. Шанс критического урона ({enemise["attack"] * 3}ед.) равен {enemise["luck"]}%')
        print(f'Броня поглощает {(1 - enemise["armor"]) * 100}% урона')
        print()

    def shop():
      while True:
    action01 = input('''Выберите желаемую вещь:
                                1 - Нагрудник Отчаения
                                2 - Меч Кладенец
                                3 - Посох Гендальфа
                                4 - Тряпка
                                5 - Тысечалетние яйцо
                                6 - Книга Всевластия
                                ''')

    amountofmoney = int(input("Введите количество вашех денег : "))

            if action01 == '1':
                if "Нагрудник Отчаения" in player['inventory']:
                        print("Поздравляю с покупкой Нагрудника Отчаения")

                elif action01 == '2':
                        print("Поздравляю с покупкой Меча Кладенеца")
                elif action01 == '3':
                        print("Поздравляю с покупкой Посоха Гендальфа")
                elif action01 == '4':
                        print("Поздравляю с покупкой Тряпки")
                еlif action01 == '5':
                        print("Поздравляю с покупкой Тысечалетнего яйца")
                elif action01 == '6':
                        print("Поздравляю с покупкой Книги Всевластия")


    def shop():
        while True:
    action01 = input('''Выберите желаемую вещь:
                    1 - Нагрудник Отчаения
                    2 - Меч Кладенец
                    3 - Посох Гендальфа
                    4 - Тряпка
                    5 - Тысячалетние яйцо
                    6 - Книга Всевластия
                    ''')

    money = int(input("Введите количество вашех денег : "))

            if action01 == '1':
                    if "Нагрудник Отчаения" in inventory:
                        print("Поздравляю с покупкой Нагрудника Отчаения")

            elif action01 == '2':
                    print("Поздравляю с покупкой Меча Кладенеца")
            elif action01 == '3':
                    print("Поздравляю с покупкой Посоха Гендальфа")
            elif action01 == '4':
                    print("Поздравляю с покупкой Тряпки")
            elif action01 == '5':
                    print("Поздравляю с покупкой Тысечалетнего яйца")
            elif action01 == '6':
                    print("Поздравляю с покупкой Книги Всевластия")


    def display_inventory():
            print(inventory)

    def training():
        print("ППр")




























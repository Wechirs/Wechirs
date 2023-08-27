from random import randint;
from time import sleep;
from function1 import *

inventory = {}

player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemise = [
    {
        "name": "Орк",
        "hp": 1000,
        "attack": 150,
        "script": "Здравствуй нежелец .",
        "win": "О нет ты убил меня .",
        "loss": "Ха-ха ты проиграл жалкий щенок .",
    },
    {
     "name": "Чернокнижник",
        "hp": 100000,
        "attack": 1000,
        "script": "Здравствуй незнакомец. ",
        "win": "ЁОУ ЁОУ ЁОУ ЁОУ",
        "loss": ".",
    },
    {
        "name": "Эльф",
        "hp": 10000,
        "attack": 100,
        "script": "Здравствуй странник .",
        "win": "цЫК",
        "loss": "Я само совершенство в отличие от тебя ."
    }
    ]


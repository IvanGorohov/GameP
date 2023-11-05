import json
from inventory import Inventory

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_damage = 16
        self.abilities = {"shield_bash": 20}
        self.inventory = Inventory()

    def attack(self, target, ability=None):
        damage = self.attack_damage
        if ability and ability in self.abilities:
            damage += self.abilities[ability]
        target.receive_damage(damage)

    def get_available_abilities(self):
        return list(self.abilities.keys())

class Thief:
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.attack_damage = 10
        self.abilities = {"backstab": 25}
        self.inventory = Inventory()

    def attack(self, target, ability=None):
        damage = self.attack_damage
        if ability and ability in self.abilities:
            damage += self.abilities[ability]
        target.receive_damage(damage)

    def get_available_abilities(self):
        return list(self.abilities.keys())

def save_game(player_instance):
    player_data = {
        "name": player_instance.name,
        "class": player_instance.__class__.__name__,
        "health": player_instance.health,
        "attack_damage": player_instance.attack_damage,
        "abilities": player_instance.abilities
    }

    with open('player_data.json', 'w') as json_file:
        json.dump(player_data, json_file)

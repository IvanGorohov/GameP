import json

def save_player_data(player_data):
    with open('player_save.json', 'w') as json_file:
        json.dump(player_data, json_file)
    print("Игра сохранена!")
import json

def load_player_data():
    try:
        with open('player_save.json', 'r') as json_file:
            player_data = json.load(json_file)
        print("Игра загружена! Данные игрока:", player_data)
        return player_data  # Вернем данные игрока
    except FileNotFoundError:
        print("Файл сохранения не найден.")
        return None
    except Exception as e:
        print("Произошла ошибка при чтении файла сохранения:", e)
        return None
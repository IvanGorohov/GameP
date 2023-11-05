def load_game(player_name):
    try:
        player_save_file = f'{player_name}_save_game.json'

        with open(player_save_file, 'r') as file:
            game_data = json.load(file)

        # Остальной код...

        # Устанавливаем начальное местоположение игрока на основе данных из сохраненной игры
        player.rect.x = player_position[1] * TILE_SIZE
        player.rect.y = player_position[0] * TILE_SIZE

        # Остальной код...

    except FileNotFoundError:
        print(f"Файл збереження для гравця {player_name} не знайдено.")
        return None, None, None, None, None


import json

TILE_SIZE = 50
def save_game(player, player_name, current_enemies, map_filename, player_class, player_health):
    game_data = {
        "map_filename": map_filename,
        "player_position": [player.rect.y // TILE_SIZE, player.rect.x // TILE_SIZE],
        "enemy_positions": [(enemy.rect.y // TILE_SIZE, enemy.rect.x // TILE_SIZE) for enemy in current_enemies],
        "player_data": {
            "name": player_name,
            "class": player_class,
            "health": player_health,
            # Додайте інші дані гравця
        }
    }

    player_save_file = f'{player_name}save_game.json'

    with open(player_save_file, 'w') as file:
        json.dump(game_data, file)
    print(f"Гра для гравця {player_name} збережена на карті {map_filename}!")

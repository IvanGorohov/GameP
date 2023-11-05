import os
import pygame
import sys
import json
from characters import Warrior, Thief
import pickle
pygame.init()
SCREEN_SIZE = (900, 900)
WHITE = (255, 255, 255)
if not os.path.exists('player_data.json'):
    with open('player_data.json', 'w') as json_file:
        json.dump({}, json_file)


with open('player_data.json', 'r') as json_file:
    player_data = json.load(json_file)


def load_saved_data():
    player_name, player_class, player_position, health, map_filename = None, None, None, None, None
    enemy_positions, attack_damage, abilities, inventory = [], None, None, []

    try:
        with open('player_save.json', 'r') as json_file:
            game_data = json.load(json_file)
            player_name = game_data.get("name")
            player_class_name = game_data.get("class")
            map_filename = game_data.get("map_filename")
            player_position = game_data.get("player_position")
            health = game_data.get("health")
            enemy_positions = game_data.get("enemy_positions")
            attack_damage = game_data.get("attack_damage")
            abilities = game_data.get("abilities")
            inventory = game_data.get("inventory", [])

            if player_class_name == "Warrior":
                player_class = Warrior
            elif player_class_name == "Thief":
                player_class = Thief
            else:

                pass

    except FileNotFoundError:
        pass

    return player_name, player_class, player_position, health, map_filename, enemy_positions, attack_damage, abilities, inventory



menu_window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Главное меню")
background_image = pygame.image.load("Menubackground.png").convert()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def input_text(prompt, x, y, ):
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(x, y, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    user_input = ''
    is_input_active = True

    while is_input_active:
        menu_window.fill(WHITE)
        draw_text(prompt, font, (0, 0, 0), menu_window, x, y - 50)
        pygame.draw.rect(menu_window, color, input_box, 2)
        font = pygame.font.Font(None, 36)
        draw_text(user_input, font, (0, 0, 0), menu_window, input_box.x + 10, input_box.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    color = color_active
                else:
                    color = color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        pygame.display.flip()

    return user_input.strip()
def show_continue_button(menu_window, continue_button_visible):
    continue_button = pygame.Rect(500, 500, 200, 50)
    draw_text('Продолжить', pygame.font.Font(None, 36), (0, 0, 0), menu_window, continue_button.x + 10, continue_button.y + 10)
    pygame.draw.rect(menu_window, (0, 0, 0), continue_button, 2)
    return continue_button


def main_menu(player_name=None):
    continue_button_visible = False
    continue_button = None

    while True:
        menu_window.fill(WHITE)
        title_font = pygame.font.Font(None, 80)
        draw_text('Главное меню', title_font, (0, 0, 0), menu_window, 250, 150)

        play_button = pygame.Rect(200, 500, 200, 50)
        draw_text('Играть', pygame.font.Font(None, 36), (0, 0, 0), menu_window, play_button.x + 50, play_button.y + 10)
        pygame.draw.rect(menu_window, (0, 0, 0), play_button, 2)

        if continue_button_visible:
            continue_button = show_continue_button(menu_window, continue_button_visible)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    player_name = input_text('Введите имя персонажа:', 350, 400)
                    player_class = choose_class_menu()
                    player_instance = player_class(player_name)
                    player_data = {
                        "name": player_instance.name,
                        "class": player_instance.__class__.__name__,
                        "map_filename": "map.txt",
                        "player_position": [5, 5],
                        "enemy_positions": [],
                        "health": player_instance.health,
                        "attack_damage": player_instance.attack_damage,
                        "abilities": player_instance.abilities,
                        "inventory": player_instance.inventory.items
                    }
                    with open('player_data.json', 'w') as json_file:
                        json.dump(player_data, json_file)
                    return player_data
                elif continue_button and continue_button.collidepoint(event.pos):
                    player_data = load_saved_data()
                    if player_data:
                        return player_data

        # Проверка наличия сохранения
        try:
            with open('player_save.json', 'r') as json_file:
                game_data = json.load(json_file)
            continue_button_visible = True
        except FileNotFoundError:
            continue_button_visible = False

        pygame.display.update()

def choose_class_menu():
    while True:
        menu_window.fill(WHITE)
        title_font = pygame.font.Font(None, 80)
        draw_text('Выберите класс персонажа', title_font, (0, 0, 0), menu_window, 150, 150)

        warrior_button = pygame.Rect(350, 300, 200, 50)
        draw_text('Воин', pygame.font.Font(None, 36), (0, 0, 0), menu_window, warrior_button.x + 50,
                  warrior_button.y + 10)
        pygame.draw.rect(menu_window, (0, 0, 0), warrior_button, 2)

        thief_button = pygame.Rect(350, 400, 200, 50)
        draw_text('Вор', pygame.font.Font(None, 36), (0, 0, 0), menu_window, thief_button.x + 50, thief_button.y + 10)
        pygame.draw.rect(menu_window, (0, 0, 0), thief_button, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if warrior_button.collidepoint(event.pos):
                    return Warrior
                elif thief_button.collidepoint(event.pos):
                    return Thief

        pygame.display.update()


def game_loop(player_name, player_class):
    # Создайте объект персонажа на основе выбранного класса
    if player_class == Warrior:
        player_instance = Warrior(player_name)
    elif player_class == Thief:
        player_instance = Thief(player_name)

    # Здесь начинается игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    pygame.init()
    SCREEN_SIZE = (900, 900)
    menu_window = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Главное меню")

    player_name, player_class, _, _, _ = load_saved_data()
    if player_name and player_class:
        # Если есть сохраненные данные, начнем игру с ними
        game_loop(player_name, player_class)
    else:
        # Если сохраненных данных нет, покажем главное меню для создания нового персонажа
        main_menu()

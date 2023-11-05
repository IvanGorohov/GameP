from Player import Player
import pygame
import sys

from enemy import Enemy
from Item import Item
import menu
import json

from load_player_data import load_player_data
from save_player_data import save_player_data

pygame.init()
pillar_image = pygame.image.load('pillar.png')
box_image = pygame.image.load("box.png")
goblin_image = pygame.image.load("goblin.png")



items = [
    Item("Pillar", pillar_image, "Ancient Pillar", (100, 150) , True),
Item("Pillar", pillar_image, "Ancient Pillar", (300, 450) , True),
Item("Pillar", pillar_image, "Ancient Pillar", (100, 250) , True),
Item("Pillar", box_image, "Ancient Pillar", (170, 260) , True),


]
items1 = [

    Item("Pillar", pillar_image, "Ancient Pillar", (100, 150) , False),
    Item("Pillar", pillar_image, "Ancient Pillar", (100, 280), False),
]

items2 = [

    Item("Pillar", pillar_image, "Ancient Pillar", (100, 350) , False),
    Item("Pillar", pillar_image, "Ancient Pillar", (100, 180), False),
]


clock = pygame.time.Clock()
player_image = pygame.image.load('player.png')
door_image = pygame.image.load('door.png')
dunground_image = pygame.image.load('grounddun.png')
dunwall_image = pygame.image.load('dungwall.png')
dunwaleft_image = pygame.image.load('dungwallleft.png')
dunwallconncet_image = pygame.image.load('dungwallconnect.png')
boxhead_image = pygame.image.load('boxhead.png')
box_image = pygame.image.load('boxcent.png')
pillar_image = pygame.image.load('pillar.png')
pillarh_image = pygame.image.load('pillhead.png')
pillarhf_image = pygame.image.load('pillarhf.png')

with open('player_data.json', 'r') as json_file:
    player_data = json.load(json_file)
    player_class = player_data.get('class', 'Warrior')
    if player_class == 'Warrior':
        player_health = player_data.get('health')
    elif player_class == 'Thief':
        player_health = player_data.get('health')

MAX_HEALTH = player_health
SCREEN_SIZE = (900, 900)
TILE_SIZE = 50
TILE_SIZEMass= 515
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Гра з картою")
door_coordinates = None
save_game_flag = False
load_game_flag = False

grass_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
grass_tile.fill(GREEN)

water_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
water_tile.blit(dunwall_image, (0, 0))

door_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
door_tile.blit(door_image, (0, 0))

dung_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
dung_tile.blit(dunground_image, (0, 0))

dungl_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
dungl_tile.blit(dunwaleft_image, (0, 0))

dungc_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
dungc_tile.blit(dunwallconncet_image, (0, 0))

boxh_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
boxh_tile.blit(boxhead_image, (0, 0))

box_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
box_tile.blit(box_image, (0, 0))

pilarh_tile=pygame.Surface((TILE_SIZE, TILE_SIZE))

pilarh_tile.blit(pillarh_image, (0, 0))

pillarhf_tile=pygame.Surface((TILE_SIZE, TILE_SIZE))
pillarhf_tile.blit(pillarhf_image,(0,0))

def load_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

world_map = load_map('map.txt')
current_location_items = items


camera = pygame.Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])


player_data = menu.main_menu()

player_name_surface = pygame.font.Font(None, 36).render(player_data['name'], True, (0, 0, 0))
player_health_surface = pygame.font.Font(None, 36).render(str(player_data['health']), True, (0, 0, 0))

enemies_level1 = []  # Враги на первом уровне
enemies_level2 = [
Enemy("Goblin", goblin_image, 1, 25, 100, (5, 12)),
Enemy("Goblin", goblin_image,  4, 25, 100, (5, 15)),
]  # список врагов на втором уровне

current_enemies = enemies_level1  # Изначально используем врагов первого уровня
obstacles = ['W', 'L', 'C', ]
map_filename = 'map.txt'
while True:
    player_pos = player_data.get('player_position', [5, 5])
    player = Player(player_pos[1], player_pos[0], player_image)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        new_row, new_col = player_pos[0], player_pos[1]

        if keys[pygame.K_LEFT] and player_pos[1] > 0 and world_map[new_row][new_col - 1] not in obstacles:
            new_col -= 1
        if keys[pygame.K_RIGHT] and player_pos[1] < len(world_map[0]) - 1 and world_map[new_row][
            new_col + 1] not in obstacles:
            new_col += 1
        if keys[pygame.K_UP] and player_pos[0] > 0 and world_map[new_row - 1][new_col] not in obstacles:
            new_row -= 1
        if keys[pygame.K_DOWN] and player_pos[0] < len(world_map) - 1 and world_map[new_row + 1][
            new_col] not in obstacles:
            new_row += 1
        player_data["player_position"] = [new_row, new_col]



        player_name = player_data

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пример клавиши атаки (пробел)
                player.set_attack_state(True)  # Устанавливаем флаг атаки в True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.set_attack_state(False)  # Сбрасываем флаг атаки в False при отпускании клавиши

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Привязываем атаку к клавише "Пробел"
                player.attack(current_enemies)
        # При нажатии на клавишу "P", загрузите данные игры из файла

        if world_map[new_row][new_col] == 'R':
            # Обновите world_map и установите начальные координаты игрока на второй карте
            world_map = load_map('map2.txt')
            player_pos = [2, 9]  # Установите начальные координаты игрока на второй карте
            current_enemies = enemies_level2  # Изменяем текущий список врагов на второй уровень
            current_location_items = items1
        if world_map[new_row][new_col] == '3':
            # Обновите world_map и установите начальные координаты игрока на второй карте
            world_map = load_map('map3.txt')
            player_pos = [2, 13]  # Установите начальные координаты игрока на второй карте
            current_enemies = enemies_level1  # Изменяем текущий список врагов на второй уровень
            current_location_items = items2
        # Проверка на наличие стены ('W') после проверки двери
        if world_map[new_row][new_col] not in ['W', 'L', 'C']:
            player_pos = [new_row, new_col]
            player.rect.x = new_col * TILE_SIZE
            player.rect.y = new_row * TILE_SIZE



    window.fill(BLACK)

    camera.x = player.rect.x - SCREEN_SIZE[0] // 2
    camera.y = player.rect.y - SCREEN_SIZE[1] // 2


    camera.x = max(0, min(camera.x, len(world_map[0]) * TILE_SIZE - SCREEN_SIZE[0]))
    camera.y = max(0, min(camera.y, len(world_map) * TILE_SIZE - SCREEN_SIZE[1]))


    for row in range(len(world_map)):
        for col in range(len(world_map[0])):
            tile = None

            if world_map[row][col] == 'G':
                tile = dung_tile
            elif world_map[row][col] == 'W':
                tile = water_tile
            elif world_map[row][col] == 'R':
                tile = door_tile

            elif world_map[row][col] == 'L':
                tile = dungl_tile
            elif world_map[row][col]=='-':
                 tile=pilarh_tile
            elif world_map[row][col]=='|':
                 tile=pillarhf_tile
            elif world_map[row][col] == 'C':
                tile = dungc_tile
            elif world_map[row][col] == 'H':
                tile = boxh_tile

            elif world_map[row][col] == 'X':
                tile = box_tile

            elif world_map[row][col] == '3':
                tile = door_tile
            if tile:
                window.blit(tile, (col * TILE_SIZE - camera.x, row * TILE_SIZE - camera.y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_o]:
        save_player_data(player_data)

        # Если клавиша 'SPACE' нажата, загружаем игру
    if keys[pygame.K_SPACE]:
        player.set_attack_state(True)
    else:
        player.set_attack_state(False)

    # Если клавиша 'P' нажата, загружаем игру
    if keys[pygame.K_p]:
        player_data = load_player_data()
        loaded_player_data = load_player_data()

        if loaded_player_data:
            # Если данные игрока успешно загружены, создайте объект игрока с использованием этих данных
            player_name = loaded_player_data["name"]
            player_class = loaded_player_data["class"]
            player_position = loaded_player_data["player_position"]
            player_health = loaded_player_data["health"]
            player_attack_damage = loaded_player_data["attack_damage"]
            player_abilities = loaded_player_data["abilities"]
            player_inventory = loaded_player_data["inventory"]



            # Обновите свойства игрока, используя данные из loaded_player_data
            player.name = player_name
            player.health = player_health
            player.attack_damage = player_attack_damage
            player.abilities = player_abilities
            player.inventory.items = player_inventory
        else:
            # Обработка случая, если данные игрока не загружены.
            print("Не удалось загрузить данные игрока.")
    for enemy in current_enemies:
        enemy.update(player.rect, world_map, TILE_SIZE)  # Передаємо world_map в метод update ворога
        window.blit(enemy.image, (enemy.rect.x - camera.x, enemy.rect.y - camera.y))
        window.blit(enemy.image, (enemy.rect.x - camera.x, enemy.rect.y - camera.y))

        # Перевірка столкнення гравця із ворогом прямо тут
        if player.rect.colliderect(enemy.rect):
            enemy.deal_damage(player)  # Викликаємо метод deal_damage у ворога
            player.update_health_surface()
            # Якщо здоров'я гравця менше або рівне нулю, гравець програв
            if player.health <= 0:
                print("Гравець програв!")
                pygame.quit()
                sys.exit()
    for enemy in current_enemies:
         if pygame.sprite.collide_rect(player, enemy):
          if player.is_attacking:  # Проверяем, нажата ли клавиша атаки у игрока
            damage = player.attack_damage  # Урон игрока
            enemy.take_damage(damage)  # Применяем урон к врагу
            if enemy.health <= 0:
                current_enemies.remove(enemy)

    for item in current_location_items:
        object_screen_x = item.x - camera.x
        object_screen_y = item.y - camera.y
        window.blit(item.image, (object_screen_x, object_screen_y))

    window.blit(player.image, (player.rect.x - camera.x, player.rect.y - camera.y))
    window.blit(player_name_surface, (10, 10))
    window.blit(player_health_surface, (12, 50))
    window.blit(item.image, (object_screen_x, object_screen_y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)




import pygame
import sys

from enemy import Enemy
from inventory import Inventory

import json

SCREEN_SIZE = (900, 900)
TILE_SIZE = 50
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
window = pygame.display.set_mode(SCREEN_SIZE)
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
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.inventory = Inventory()
        self.health = player_health
        self.attack_damage = 10  # Устанавливаем начальный урон игрока
        self.is_attacking = False
    def take_damage(self, damage):
        self.health -= damage
        self.update_health_surface()
        if self.health <= 0:
            pygame.quit()
            sys.exit()

    def attack(self, enemies):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                damage = self.attack_damage
                enemy.take_damage(damage)

    def set_attack_state(self, state):
        self.is_attacking = state

    def update_health_surface(self):
        # Обновляем объект поверхности с текущим здоровьем игрока
        player_health = pygame.font.Font(None, 36).render(str(self.health), True, (0, 0, 0))
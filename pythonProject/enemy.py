import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, image, speed, damage, health, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.position = position  # позиция предмета на карте, например, (x, y)
        self.x, self.y = position
        self.speed = speed
        self.damage = damage
        self.health = health

    def update(self, player_rect, world_map, TILE_SIZE):
        dx = player_rect.x - self.rect.x
        dy = player_rect.y - self.rect.y

        dist = pygame.math.Vector2(dx, dy).length()

        if dist > 0:
            dx /= dist
            dy /= dist

        dx *= self.speed  # Умножаем на self.speed после убеждения, что dx - число
        dy *= self.speed  # Умножаем на self.speed после убеждения, что dy - число

        dx = round(dx)  # Преобразуем в целые значения
        dy = round(dy)

        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Получаем индексы клеток, через которые проходит враг
        new_row = int(new_y // TILE_SIZE)
        new_col = int(new_x // TILE_SIZE)

        # Проверяем, не являются ли новые координаты стеной ('W')
        if world_map[new_row][new_col] != 'W':
            self.rect.x = new_x
            self.rect.y = new_y

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def deal_damage(self, player):
        player.take_damage(self.damage)

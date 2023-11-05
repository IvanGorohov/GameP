import pygame

class Item:
    def __init__(self, name, image, description, position, passable=True ):
        self.name = name
        self.image = image  # изображение предмета
        self.description = description  # описание предмета
        self.position = position  # позиция предмета на карте, например, (x, y)
        self.x, self.y = position
        self.passable = passable

pillar_image = pygame.image.load('pillar.png')


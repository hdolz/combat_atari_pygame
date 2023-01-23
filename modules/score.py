import pygame
import os
from config.settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        pygame.font.init()
        self.font = pygame.font.Font('assets\PressStart2P.ttf', 80)
        self.rect = pygame.draw.rect(screen, MAP_BACKGROUND_COLOR, (0, 0, 0, 0))
        pygame.display.update()
    
    def drawScore(self, point, screen, color, x_pos, y_pos):
        if point < 10:
            screen.blit(self.font.render('0' + str(point), True, color, MAP_BACKGROUND_COLOR), (x_pos, y_pos))
        else:
            screen.blit(self.font.render(str(point), True, color, MAP_BACKGROUND_COLOR), (x_pos, y_pos))
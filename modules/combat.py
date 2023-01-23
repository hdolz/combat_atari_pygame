import pygame
import os
from config.settings import *
from modules.event_enum import *
from modules.event_handler import *
from modules.player import *
from modules.score import *
from modules.collision_handler import *
from modules.render import *
from modules.map_loader import *

class Combat():
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)
        self.framerate = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.eventHandler = EventHandler()
        self.collision_handler = CollisionHandler()
        self.render = Render(self.screen)
        self.map_loader = MapLoader()
        self.map = [] #retangulos do mapa
        self.relPath = os.getcwd()
        #Instancias de players
        bulletP1Img = pygame.image.load(self.relPath + "\\assets\\explosion1.png")
        bulletP2Img = pygame.image.load(self.relPath + "\\assets\\explosion2.png")
        self.p1 = Player(P1_POS[0], P1_POS[1], pygame.image.load(self.relPath + "\\assets\\tank1.png"), 0, bulletP1Img)
        self.p2 = Player(P2_POS[0], P2_POS[1], pygame.image.load(self.relPath + "\\assets\\tank2.png"), 180, bulletP2Img)
        self.scoreP1 = Score(self.screen)
        self.scoreP2 = Score(self.screen)
        
    def run(self):
        pygame.init()
        #carregar mapa
        self.map = self.map_loader.load(self.relPath + "\maps\\"+ MAP)

        while True:
            #render
            self.screen.fill(MAP_BACKGROUND_COLOR)
            self.render.drawMap(self.map)
            self.render.drawPlayer(self.p1)
            self.render.drawPlayer(self.p2)
            self.render.drawScore(self.p1, self.screen, self.scoreP1, SCORE_P1_COLOR, P1_SCORE_POS[0], P1_SCORE_POS[1])
            self.render.drawScore(self.p2, self.screen, self.scoreP2, SCORE_P2_COLOR, P2_SCORE_POS[0], P2_SCORE_POS[1])
            self.p1.bullets.draw(self.screen)
            self.p2.bullets.draw(self.screen)

            #eventos
            event = self.eventHandler.getEvent(pygame.event.get())
            self.eventHandler.handleEvent(event, self.p1, self.p2)

            #movimentação
            self.p1.movement()
            self.p2.movement()
            self.p1.bullets.update()
            self.p2.bullets.update()

            #colisao
            self.collision_handler.checkMapPlayerCollision(self.map, self.p1)
            self.collision_handler.checkMapPlayerCollision(self.map, self.p2)
            self.collision_handler.checkPlayerCollision(self.p1, self.p2)
            self.collision_handler.checkPlayerCollision(self.p2, self.p1)
            self.collision_handler.checkBulletMapCollision(self.p1, self.map)
            self.collision_handler.checkBulletMapCollision(self.p2, self.map)
            self.collision_handler.checkBulletPlayerCollision(self.p1, self.p2, TYPE_P2)
            self.collision_handler.checkBulletPlayerCollision(self.p2, self.p1, TYPE_P1)

            #update frame
            self.framerate.tick(FRAMERATE)
            pygame.display.flip()


from modules.player import *

class CollisionHandler():
    def __init__(self) -> None:
        pass

    def checkMapPlayerCollision(self, map, player: Player):
        for mapRect in map:
            if player.rect.colliderect(mapRect):
                player.forward = False
    
    def checkPlayerCollision(self, p1: Player, p2: Player):
        if p1.rect.colliderect(p2):
            p1.forward = False

    def checkBulletMapCollision(self, player: Player, map):
        player.checkBulletMapCollision(map)

    def checkBulletPlayerCollision(self, p1: Player, p2: Player, type):
        p1.checkBulletPlayerCollision(p2, type)
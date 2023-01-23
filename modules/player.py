import pygame
from config.settings import *
from modules.bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, player_image, angle, bullet_image):
        super().__init__()
        self.angle = angle
        self.image = player_image
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.rotate = self.image
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2(1, 0).rotate(angle)
        self.bullets = pygame.sprite.Group()
        self.bullet_img = bullet_image
        self.rotate_left = False
        self.rotate_right = False
        self.forward = False
        self.score = 0
        self.death = False

    def movement(self):
        if self.forward:
            self.pos += 3/2*self.direction
            self.rect.center = round(self.pos[0]), round(self.pos[1])
        if self.rotate_right: 
            self.image = pygame.transform.rotate(self.rotate, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
            self.angle -= 5
        if self.rotate_left:
            self.image = pygame.transform.rotate(self.rotate, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
            self.angle += 5
    
    def shoot(self):
        self.bullets.add(Bullet(self, self.bullet_img))
    
    def checkBulletMapCollision(self, map):
        for bullet in self.bullets:
            for mapRect in map:
                if bullet.rect.colliderect(mapRect):
                    if bullet.killBullet():
                        bullet.kill()
                    if bullet.rect.left < mapRect.left or bullet.rect.right > mapRect.right:
                        bullet.direction.x *= -1
                    if bullet.rect.top < mapRect.top or bullet.rect.bottom > mapRect.bottom:
                        bullet.direction.y *= -1
                    break
                    
    
    def checkBulletPlayerCollision(self, enemy, type):
        for bullet in self.bullets:
            if bullet.rect.colliderect(enemy.rect):
                self.score += 1
                bullet.kill()
                if type == TYPE_P1:
                    enemy.rect.x = P1_POS[0]
                    enemy.rect.y = P1_POS[1]
                if type == TYPE_P2:
                    enemy.rect.x = P2_POS[0]
                    enemy.rect.y = P2_POS[1]
                enemy.pos = pygame.Vector2(enemy.rect.center)

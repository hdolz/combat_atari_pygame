import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, nball):
        super().__init__()
        self.image = nball
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.angle = player.angle
        self.pos = pygame.Vector2(player.rect.center)
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.direction = pygame.Vector2(10, 1).rotate(-self.angle)
        self.existCount = 5
        
    def update(self):
        self.pos += self.direction
        self.rect.center = round(self.pos.x), round(self.pos.y)
    
    def killBullet(self):
        self.existCount -= 1
        if self.existCount == 0:
            return True
        return False
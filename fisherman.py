import pygame
import fish

pygame.init()

#This is the fisherman class which enables movement and handles collision
class Fisherman(pygame.sprite.Sprite):
    def __init__(self,image_path,x_position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect((x_position,y_position)) #The y-position will be a constant since fisherman will only move left and right

    def move(self,dx):
        self.rect.x += dx

    def collide_with_fish(self):
        return self.rect.colliderect(fish.rect)
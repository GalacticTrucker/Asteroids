import pygame
from circleshape import CircleShape
from constants import *

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # Update rotation based on turn speed and delta time

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Unit vector pointing in the direction of the player's rotation
        self.position += forward * PLAYER_SPEED * dt # Update position based on speed and delta time
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
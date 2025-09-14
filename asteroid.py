import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt # Update position based on velocity and delta time
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        asteroid1_angle = self.velocity.rotate(random_angle)
        asteroid2_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid1_angle * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid2_angle * 1.2
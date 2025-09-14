import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = (255, 255, 255)
        self.position = (SCREEN_WIDTH - 150, 20)
        self.player_score = 0

        
    def update_score(self, new_score):
        self.player_score = new_score

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.player_score}", False, self.color)
        screen.blit(score_text, self.position)

    def update(self, dt):
        pass
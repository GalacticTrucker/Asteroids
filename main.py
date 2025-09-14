from constants import *
import pygame

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    game_clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()   # Update the display
        dt = game_clock.tick(60) / 1000  # Limit to 60 FPS and get delta time

if __name__ == "__main__":
    main()

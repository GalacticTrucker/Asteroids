from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    game_clock = pygame.time.Clock() # Create a clock object to manage the frame rate
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Player setup
    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2   
    player = Player(x, y)

    # Asteroid setup
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Main game loop
    running = True
    while running:
        # Stops the game if the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        screen.fill((0, 0, 0))

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()   # Update the display
        dt = game_clock.tick(60) / 1000  # Limit to 60 FPS and get delta time


if __name__ == "__main__":
    main()

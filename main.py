import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    cl = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    actor = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    Shot.containers = (shots, updatable, drawable)
    ast = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if actor.touch(asteroid):
                print("Game over!")

                sys.exit()

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        dt = cl.tick(60)/1000
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)
if __name__ == "__main__":
    main()
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    cl = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        actor = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        actor.draw(screen)
        pygame.display.flip()
        dt = cl.tick(60)/1000
    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)
if __name__ == "__main__":
    main()
from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 
        split_angle = random.uniform(20, 50)
        new_velo_1 = self.velocity.rotate(split_angle)
        new_velo_2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = new_velo_1*1.2
        new_2.velocity = new_velo_2*1.2

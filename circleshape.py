import pygame
import math
# Base class for game objects, there are several types of obj 
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.length = math.sqrt(x**2 + y**2)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def touch(self, other):
        if self.radius + other.radius < self.position.distance_to(other.position):
            return False
        return True
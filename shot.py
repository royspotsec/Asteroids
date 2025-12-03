from circleshape import *
from circleshape import *
import pygame
from constants import *
class Shot (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self,surface):
        # so here we defined the things needed to use it in the function below
        # so it can construct a new Astroid 
        pygame.draw.circle(surface=surface,color="white",center=self.position,radius=self.radius,width=LINE_WIDTH)
    def update(self, dt):
        super().update(dt)
        self.position=self.position+(self.velocity * dt)
    


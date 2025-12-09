import pygame
from circleshape import *
from constants import *
from logger import *
import random
from player import *


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self,surface):
        # so here we defined the things needed to use it in the function below
        # so it can construct a new Astroid 
        pygame.draw.circle(surface=surface,color="white",center=self.position,radius=self.radius,width=LINE_WIDTH)
    def update(self, dt):
        super().update(dt)
        self.position=self.position+(self.velocity * dt)
    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else :
            log_event("asteroid_split")
            random_angle=random.uniform (20,50)
            firstvectro=self.velocity.rotate(random_angle)
            seconedvector=self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first=Asteroid(self.position.x , self.position.y,new_radius)
            seconed=Asteroid(self.position.x , self.position.y,new_radius)
            first.velocity = firstvectro *1.2
            seconed.velocity = seconedvector*1.2
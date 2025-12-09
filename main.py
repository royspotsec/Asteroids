import pygame
from logger import *
from constants import SCREEN_WIDTH,SCREEN_HEIGHT 
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver} ")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable= pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2 ,y = SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield=AsteroidField()
    shots=pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    while(True):
        log_state()
        
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                return 
        updatable.update(dt)
        screen.fill("black")
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        for thing in drawable:
            thing.draw(screen)

        
                

                

                


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

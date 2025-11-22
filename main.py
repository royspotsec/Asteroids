import pygame
from logger import log_state
from constants import SCREEN_WIDTH,SCREEN_HEIGHT 
from player import *


    
    
    
def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver} ")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
    clock = pygame.time.Clock()
    
    
    
    while(True):
        log_state()
        
        for event in pygame.event.get():
            dt = clock.tick(60)
            
        
            if event.type == pygame.QUIT:
                return 
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        
    
        
    


if __name__ == "__main__":
    main()

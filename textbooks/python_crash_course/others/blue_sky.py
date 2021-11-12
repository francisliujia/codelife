import sys
import pygame

class Window:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_heigh = 500
        self.bg_color =(0, 0, 255)



if __name__ == '__main__':
    # make a game instance, and run the game.
    blue_sky = Window()

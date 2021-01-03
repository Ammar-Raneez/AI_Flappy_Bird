import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

class Bird:
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25 #movement angle
    ROT_VEL = 20 #how much to rotate each frame
    ANIMATION_TIME = 5 #time of animation

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5 #going upwards is -ve
        self.tick_count = 0 #when we last jumped (nned to know when we change directions)
        self.height = self.y
    
    def move(self):
        self.tick_count += 1 #move frame
        #Physics Equation
        d = self.vel * self.tick_count + 1.5 * self.tick_count**2
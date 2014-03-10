# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 22:15:57 2014

@author: ychen1
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 20:49:27 2014
Gravity Video Game!
@author: ychen1
"""

import pygame
from pygame.locals import *
import random
import math
import time

class GravityModel:
    """ Encodes the game state of Gravity """
    def __init__(self):
        self.number_of_lives = 3
        self.spacejunks = []
        for i in range(640/110):
            for j in range(240/30):              
                new_a = SpaceJunkS(10+110*i,10+30*j,100,20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                self.spacejunks.append(new_a)
        self.spacejunkm = []
        for i in range(640/110):
            for j in range(240/30):              
                new_b = SpaceJunkM(10+110*i,10+30*j,100,20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                self.spacejunkm.append(new_b)
        self.sandra = Sandra(200,450,100,20,'sandra_bullock')
            
    def update(self):
        self.sandra.update()
        
class SpaceJunkS:
    """ Encodes the state of a stationary space junk """
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
class SpaceJunkM:
    """ Encodes the state of a moving space junk """
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

class Sandra(object):
    """ Encode the state of the Sandra Bullock """
    def __init__(self,x,y,width,height,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

class PyGameWindowView:
    """ renders the GravityModel to a pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
    
    def draw(self):
        for a in self.model.spacejunks:
            pygame.draw.rect(self.screen, pygame.Color(a.color[0], a.color[1], a.color[2]), pygame.Rect(a.x, a.y, a.width, a.height))
        for b in self.model.spacejunkm:
            pygame.draw.rect(self.screen, pygame.Color(b.color[0], b.color[1], b.color[2]), pygame.Rect(b.x, b.y, b.width, b.height))
        pygame.draw(self.screen, (self.model.sandra.width, self.model.sandra.height), pygame.Surface(self.model.sandra.x, self.model.sandra.y))
        pygame.display.update()

class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.sandra.vx += -1.0
        if event.key == pygame.K_RIGHT:
            self.model.sandra.vx += 1.0
        if event.key == pygame.K_UP:
            self.model.sandra.vy += -1.0
        if event.key == pygame.K_DOWN:
            self.model.sandra.vy += 1.0
            

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = GravityModel()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)
    running = True
    
    background_image = pygame.image.load("starsinthesky.jpg")
    
    screen_rect = screen.get_rect()
    
    while running:
        screen.blit(background_image,[0,0])
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)
        
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()
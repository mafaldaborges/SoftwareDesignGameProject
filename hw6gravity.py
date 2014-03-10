# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 18:50:03 2014
Gravity Video Game!
@author: ychen1
"""

import pygame
from pygame.locals import *
import random
import math
import time

class GravityModel:
    """Encodes the game state of Gravity"""
    def __init__(self):
        self.number_of_lives = 3
        self.spacejunks = []
        for i in range(640/110):
            for j in range(240/30):              
                new_spacejunks = SpaceJunkS(10+110*i,10+30*j,20,20,(120,120,120))
                self.spacejunks.append(new_spacejunks)
        self.spacejunkm = []
        for i in range(640/110):
            for j in range(240/30):              
                new_spacejunkm = SpaceJunkM(10+110*i,10+30*j,20,20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                self.spacejunkm.append(new_spacejunkm) 
        self.sandra = Sandra(200,450,20,20)
                
    def update(self):
        self.sandra.update()
        
class SpaceJunkS:
    """Encodes the state of the stationary space junk"""
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
class SpaceJunkM:
    speed = 10.0
    """Encodes the state of the moving space junk"""
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
#        self.vx = 0.0 #random?
#        self.vy = 0.0 #random?
        
class Sandra:
    """Encodes the state of Sandra Bullock"""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255,255,255)
        self.vx = 0.0
        self.vy = 0.0
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
class PyGameWindowView:
    """A view of Gravity rendered in a PyGame Window"""
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for spacejunks in self.model.spacejunks:
            pygame.draw.rect(self.screen, pygame.Rect(spacejunks.x,spacejunks.y,spacejunks.width,spacejunks.height), pygame.Color(spacejunks.color[0],spacejunks.color[1],spacejunks[2]))
        for spacejunkm in self.model.spacejunkm:
            pygame.draw.rect(self.screen, pygame.Rect(spacejunkm.x,spacejunkm.y,spacejunkm.width,spacejunkm.height), pygame.Color(spacejunkm.color[0],spacejunkm.color[1],spacejunkm[2]))
        pygame.draw.rect(self.screen, pygame.Rect(self.model.sandra.x,self.model.sandra.y,self.model.sandra.width,self.model.sandra.height), pygame.Color(self.model.sandra.color[0], self.model.sandra.color[1], self.model.sandra.color[2]))
        pygame.display.update()
        
class PyGameKeyboardController:
    def __init__(self,model):
        self.model = model    
    
    def handle_keyboard_event(self,event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.sandra.vx += -1.0
        if event.key == pygame.K_RIGHT:
            self.model.sandra.vx += 1.0
        if event.key == pygame.K_UP:
            self.model.sandra.vy += 1.0
        if event.key == pygame.K_DOWN:
            self.model.sandra.vy += -1.0
            
if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = GravityModel()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_keyboard_event(event)
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()
import pygame
import time

pygame.init()
pygame.display.set_mode((300, 200))
pygame.display.set_caption('robot remote')

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print "left"
            if event.key == pygame.K_RIGHT:
                print "right"
            if event.key == pygame.K_UP:
                print "up"
            if event.key == pygame.K_DOWN:
                print "down"

import pygame
import time
from AX12 import AX12

pygame.init()
pygame.display.set_mode((300, 200))
pygame.display.set_caption('robot remote')

wheel = AX12(172)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wheel.turn(20)
            if event.key == pygame.K_RIGHT:
                print "right"
            if event.key == pygame.K_UP:
                wheel.moove(20)
            if event.key == pygame.K_DOWN:
                print "down"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                wheel.turn(0)

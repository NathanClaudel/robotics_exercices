import pygame
import time
from AX12 import AX12

pygame.init()
pygame.display.set_mode((300, 200))
pygame.display.set_caption('robot remote')

wheel = AX12(171)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wheel.turn(20)
            if event.key == pygame.K_RIGHT:
                wheel.turn(0)
            if event.key == pygame.K_UP:
                print "up"
            if event.key == pygame.K_DOWN:
                print "down"

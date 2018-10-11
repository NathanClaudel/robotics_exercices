import pygame
import time
from AX12 import AX12

pygame.init()
pygame.display.set_mode((300, 200))
pygame.display.set_caption('robot remote')

wheel = AX12(172)
direction=AX12(25)
l=AX12(142)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction.move(-69)
            if event.key == pygame.K_RIGHT:
                direction.move(-29)
            if event.key == pygame.K_UP:
                wheel.turn(-50)
            if event.key == pygame.K_DOWN:
                wheel.turn(50)
            if event.key == pygame.K_P0:
                l=move(20)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                wheel.turn(0)
            if event.key == pygame.K_DOWN:
                wheel.turn(0)
            if event.key == pygame.K_LEFT:
                direction.move(-49)
            if event.key == pygame.K_RIGHT:
                direction.move(-49)
            if event.key == pygame.K_P0:
                l=move(0)

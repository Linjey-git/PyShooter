import pygame
import math

from settings import *
from player import *
from map import *
from ray_casting import *
from drawing import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screem_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, screem_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    #

    pygame.display.flip()
    clock.tick(FPS)

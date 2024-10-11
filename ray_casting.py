import math
import pygame

from settings import *
from map import *


def ray_casting_old(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            # pygame.draw.line(screen,DARKGRAY,player_pos,(x,y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.00002)
                color = (c, c // 2, c // 3)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(screen, player_pos, player_angle, textures):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        if cos_a >= 0:
            x = xm + TILE
            dx = 1
        else:
            x = xm
            dx = -1

        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # horizontals
        if sin_a >= 0:
            y = ym + TILE
            dy = 1
        else:
            y = ym
            dy = -1

        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        if depth_v < depth_h:
            depth = depth_v
            offset = yv
            texture = texture_v
        else:
            depth = depth_h
            offset = xh
            texture = texture_h

        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.0000001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)

        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGTH)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        screen.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))

        cur_angle += DELTA_ANGLE

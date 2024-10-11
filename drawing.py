import pygame

from settings import *
from ray_casting import *


class Drawing:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont('impact', 36, bold=False)
        self.textures = {'3': pygame.image.load('img/3.png').convert(),
                         '4': pygame.image.load('img/4.png').convert(),
                         '5': pygame.image.load('img/5.png').convert(),
                         '6': pygame.image.load('img/6.png').convert(),
                         '7': pygame.image.load('img/7.png').convert(),
                         '8': pygame.image.load('img/8.png').convert(),
                         'S': pygame.image.load('img/sky.png').convert()}

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.screen.blit(render, FPS_POS)

    def mini_map(self, player):
        self.screen_map.fill(BLACK)
        player_x, player_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.screen_map, GREEN, (player_x, player_y), (player_x + 12 * math.cos(player.angle),
                                                                        player_y + 12 * math.sin(player.angle)))
        pygame.draw.circle(self.screen_map, VINOUS, (int(player_x), int(player_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.screen_map, DARKGRAY, (x, y, MAP_TILE, MAP_TILE))
        self.screen.blit(self.screen_map, MAP_POS)

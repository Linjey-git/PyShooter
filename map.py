from settings import *

text_map = [
    '555555555555',
    '5..........5',
    '5...3......5',
    '5...3......5',
    '5...3......5',
    '5........445',
    '5..........5',
    '555555555555'
]

world_map = {}
mini_map = set()
for i, row in enumerate(text_map):
    for j, char in enumerate(row):
        if char != '.':
            mini_map.add((j * MAP_TILE, i * MAP_TILE))
            if char == '3':
                world_map[(j * TILE, i * TILE)] = '3'
            elif char == '4':
                world_map[(j * TILE, i * TILE)] = '4'
            elif char == '5':
                world_map[(j * TILE, i * TILE)] = '5'
            elif char == '6':
                world_map[(j * TILE, i * TILE)] = '6'
            elif char == '7':
                world_map[(j * TILE, i * TILE)] = '7'
            elif char == '8':
                world_map[(j * TILE, i * TILE)] = '8'

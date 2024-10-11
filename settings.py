import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 55, 5)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = int(math.sqrt(WIDTH * WIDTH + HEIGHT * HEIGHT))
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 4 * DIST * TILE
SCALE = WIDTH / NUM_RAYS

# texture settings (32 x 32)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGTH = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE


# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, 0)

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
AQUA = (0, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (240, 150, 0)
VINOUS = (127, 0, 0)

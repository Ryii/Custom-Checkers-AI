import pygame

## GAME CONSTANTS ##

# is init needed??
pygame.init()
CAPTION = 'Checkers'
FPS = 60
WIN_WIDTH, WIN_HEIGHT = 800, 800
NUM_ROWS, NUM_COLS = 8, 8
SQUARE_WIDTH, SQUARE_HEIGHT = WIN_WIDTH // NUM_ROWS, WIN_HEIGHT // NUM_COLS

FONT = pygame.font.Font('freesansbold.ttf', 32)
CROWN = pygame.transform.scale(pygame.image.load('images/crown.png'), (44, 25)) # to change

## COLORS(R, G, B) ##

RED          = (255,  36,   0)
WHITE        = (255, 255, 255)
BG_COLOR     = (250, 240, 230)  # Beige
BG_COLOR_ALT = (  0, 168, 107)  # Jade
BLACK        = (  0,   0,   0)
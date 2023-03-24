import pygame
from game import Game

def main():
    game = Game()
    game.initial_setup()

    run = True
    # Game loop
    while run:
        game.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()

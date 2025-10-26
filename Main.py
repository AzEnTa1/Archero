import pygame
from src.game import Game


def main():
    pygame.init() # initialise tous les modules internes de Pygame
    game = Game()
    game.run()

# Lorsque que Python éxécute un fichier, il définit une variable spéciale __name__ égale à "__main__"
if __name__ == "__main__":
    main()

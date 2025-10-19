import pygame
from src.game import Game

def main():
    # Initialisation générale
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    
    # Création du jeu et lancement
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()  # <- L'exécution commence ici !
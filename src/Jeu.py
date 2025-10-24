import pygame
import pygame_gui
import sys
from .audio import AudioManager 
from .scenes import MenuScene, GameScene
from .entities import Player, Enemy, Projectile, Weapon
from .utils import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class Jeu:
    def __init__(self):
        pygame.display.set_caption("Title")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.audio_manager = AudioManager()
        


    def run(self): # Boucle du jeu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # Si échap ou croix
                    pygame.quit()
                    sys.exit()
                self.manager.process_events(event) # Gestion des événements GUI

            self.manager.update(self.clock.tick(FPS) / 1000) # Met à jour le gestionnaire GUI

            self.screen.fill((0, 0, 0)) # Remplit l'écran en noir
            self.manager.draw_ui(self.screen) # Dessine l'interface GUI
            pygame.display.flip() # Met à jour l'affichage

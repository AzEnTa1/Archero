import pygame
from pygame.locals import *
import pygame_gui
import Fonction.Affichage.Shared_Things as var



class GameMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager):

        self.name = 'game_menu'
        self.state_manager = state_manager
        self.transition = False
        self.quit_game = False

        self.state_manager.register_state(self)
        self.ui_manager = ui_manager
        self.Back_Home_Button = None

    def start(self):
        
        # Création du bouton de retour à l'accueil
        self.Back_Home_Button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 0), (100, 50)),
            'Home',
            self.ui_manager
        )

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
                
            self.ui_manager.process_events(event)

        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)
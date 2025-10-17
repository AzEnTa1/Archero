import pygame
from pygame.locals import *
import pygame_gui
import Fonction.Affichage.Shared_Things as var



class CodexMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager):

        self.name = 'codex_menu'
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
'''

def Display_Codex(Screen, Running, Time_Delta):
    """Affiche le menu Codex et gère les interactions.
    
    Args:
        Screen: Surface PyGame où afficher l'interface
        Running: Booléen indiquant si le jeu doit continuer
        Time_Delta: Temps écoulé depuis la dernière frame
    
    Returns:
        bool: True si le jeu doit continuer, False sinon
    """
    # Gestion des événements
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

        var.Manager.process_events(Event)
        
        # Gestion du clic sur le bouton Home
        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            if Event.ui_element == Back_Home_Button:
                End_Codex_Menu()
                var.Transition = True
                var.Switch_Menu("Home")

    # Mise à jour de l'interface
    var.Manager.update(Time_Delta)
    
    # Affichage de l'arrière-plan
    Screen.fill("#C2B280")  # Couleur beige
    
    # Dessin de l'interface
    var.Manager.draw_ui(Screen)
    
    return Running
    '''
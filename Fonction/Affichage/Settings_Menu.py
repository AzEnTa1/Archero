import pygame
from pygame.locals import *
import pygame_gui

# Importation des variables partagées
import Fonction.Affichage.Shared_Things as var

class SettingsMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager):

        self.name = 'settings_menu'
        self.state_manager = state_manager
        self.transition = False
        self.quit_game = False

        self.state_manager.register_state(self)
        self.ui_manager = ui_manager
        self.Back_Home_Button = None
        self.FPS_Slider = None
        self.FPS_Label = None

    def start(self):

        # Création du bouton de retour
        self.Back_Home_Button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 0), (100, 50)),
            'Home',
            self.ui_manager
        )
        # Configuration du curseur FPS
        
        self.FPS_Slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect = pygame.Rect(735, 175, 200, 30),
            start_value=var.FPS,  # Valeur initiale
            value_range=(1, 301),  # Plage de réglage
            manager=self.ui_manager,
            object_id="@FPS_Slider"
        )

        # Création du label FPS
        self.FPS_Label = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect(735, 145, 200, 30),
            text=f"FPS: {var.FPS}",  # Texte initial
            manager=self.ui_manager,
            object_id="@FPS_Label"
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

def Display_Settings(Screen, Running, Time_Delta):
    """
    Gère l'affichage et les interactions du menu des paramètres.
    
    Args:
        Screen (pygame.Surface): Surface d'affichage
        Running (bool): État de la boucle principale
        Time_Delta (float): Temps écoulé depuis la dernière frame
    
    Returns:
        bool: Nouvel état de la boucle principale
    """
    # Gestion des événements
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

        var.Manager.process_events(Event)
        
        # Gestion des interactions utilisateur
        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            if Event.ui_element == Back_Home_Button:
                End_Settings_Menu()
                var.Transition = True
                var.Switch_Menu("Home")
        
        # Mise à jour du FPS en temps réel
        elif Event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if Event.ui_element == FPS_Slider:
                var.FPS = int(Event.value)
                FPS_Label.set_text(f"FPS: {(var.FPS-1)}")  # Ajustement visuel

    # Mise à jour et affichage
    var.Manager.update(Time_Delta)
    Screen.fill("#B0B0B0")  # Fond d'écran gris
    var.Manager.draw_ui(Screen)
    
    return Running
    '''
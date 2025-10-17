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
        self.target_state_name = self.name

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
            relative_rect = pygame.Rect(0, 175, 200, 30),
            start_value=var.FPS,  # Valeur initiale
            value_range=(1, 301),  # Plage de réglage
            manager=self.ui_manager,
            object_id="@FPS_Slider"
        )

        # Création du label FPS
        self.FPS_Label = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect(0, 145, 200, 30),
            text=f"FPS: {var.FPS}",  # Texte initial
            manager=self.ui_manager,
            object_id="@FPS_Label"
        )
    
    def end(self):
        self.Back_Home_Button.kill()
        self.FPS_Slider.kill()
        self.FPS_Label.kill()

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
            
            self.ui_manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.Back_Home_Button:
                    self.target_state_name = "main_menu"
                    self.transition = True

            elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.FPS_Slider:
                    var.FPS = int(event.value)
                    self.FPS_Label.set_text(f"FPS: {(var.FPS-1)}")

        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)

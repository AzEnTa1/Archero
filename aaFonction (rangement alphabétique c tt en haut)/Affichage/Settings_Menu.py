import pygame
from pygame.locals import *
import pygame_gui


class SettingsMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager, settings):

        self.name = 'settings_menu'
        self.state_manager = state_manager
        self.transition = False
        self.quit_game = False
        self.target_state_name = self.name

        self.state_manager.register_state(self)
        self.ui_manager = ui_manager
        self.back_home_button = None
        self.fps_slider = None
        self.fps_label = None
        self.settings = settings

    def start(self):

        # Création du bouton de retour
        self.back_home_button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 0), (100, 50)),
            'Home',
            self.ui_manager
        )
        # Configuration du curseur FPS
        
        self.fps_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect = pygame.Rect(0, 175, 200, 30),
            start_value=self.settings.fps,  # Valeur initiale
            value_range=(1, 301),  # Plage de réglage
            manager=self.ui_manager,
            object_id="@FPS_Slider"
        )

        # Création du label FPS
        self.fps_label = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect(0, 145, 200, 30),
            text=f"FPS: {self.settings.fps}",  # Texte initial
            manager=self.ui_manager,
            object_id="@FPS_Label"
        )
    
    def end(self):
        self.back_home_button.kill()
        self.fps_slider.kill()
        self.fps_label.kill()

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
            
            self.ui_manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.back_home_button:
                    self.target_state_name = "main_menu"
                    self.transition = True

            elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.fps_slider:
                    self.settings.fps = int(event.value)
                    self.fps_label.set_text(f"FPS: {(self.settings.fps - 1)}")

        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)

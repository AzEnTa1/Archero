import json
import pygame
from pygame.locals import *
import pygame_gui

class MainMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager):

        self.name = 'main_menu'
        self.state_manager = state_manager
        self.transition = False
        self.quit_game = False
        self.target_state_name = self.name

        self.state_manager.register_state(self)
        self.ui_manager = ui_manager
        self.settings_button = None
        self.codex_button = None
        self.play_button = None
        self.quit_game_button = None
        self.game_title_label = None



    def start(self):
        # Création des boutons principaux
        self.settings_button = pygame_gui.elements.UIbutton(
            pygame.Rect((215, 460), (150, 50)),
            'Settings',
            self.ui_manager,
            object_id="@Setting_button"
        )
        
        self.codex_button = pygame_gui.elements.UIbutton(
            pygame.Rect((0, 0), (150, 50)),
            'Codex',
            self.ui_manager,
            object_id="@Codex_button"
        )
        
        self.quit_game_button = pygame_gui.elements.UIbutton(
            pygame.Rect((0, 460), (150, 50)),
            'Exit',
            self.ui_manager,
            object_id="@Exit_button"
        )

        # Boutons de sélection des mondes
        self.play_button = pygame_gui.elements.UIbutton(
            pygame.Rect((175, 370), (110, 40)),
            'Play',
            self.ui_manager
        )

        # Création des éléments textuels
        self.game_title_label = pygame_gui.elements.UIlabel(
            pygame.Rect((115, 45), (730, 150)),
            "ROGUE-LIKE CSV",
            self.ui_manager,
            object_id="@Game_Title"
        )

    def end(self):
        self.settings_button.kill()
        self.codex_button.kill()
        self.quit_game_button.kill()
        self.play_button.kill()
        self.game_title_label.kill()

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
                
            self.ui_manager.process_events(event)
            if event.type == pygame_gui.UI_button_PRESSED:
                if event.ui_element == self.settings_button:
                    self.target_state_name = "settings_menu"
                    self.transition = True
                elif event.ui_element == self.codex_button:
                    self.target_state_name = "codex_menu"
                    self.transition = True
                elif event.ui_element == self.play_button:
                    self.target_state_name = "game_menu"
                    self.transition = True
                elif event.ui_element == self.quit_game_button:
                    self.quit_game = True


        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)

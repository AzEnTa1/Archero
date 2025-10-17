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
        self.Settings_Button = None
        self.Codex_Button = None
        self.play_Button = None
        self.Exit_Game_Button = None
        self.Game_Title_Label = None



    def start(self):
        # Création des boutons principaux
        self.Settings_Button = pygame_gui.elements.UIButton(
            pygame.Rect((215, 460), (150, 50)),
            'Settings',
            self.ui_manager,
            object_id="@Setting_Button"
        )
        
        self.Codex_Button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 0), (150, 50)),
            'Codex',
            self.ui_manager,
            object_id="@Codex_Button"
        )
        
        self.Exit_Game_Button = pygame_gui.elements.UIButton(
            pygame.Rect((0, 460), (150, 50)),
            'Exit',
            self.ui_manager,
            object_id="@Exit_Button"
        )

        # Boutons de sélection des mondes
        self.play_Button = pygame_gui.elements.UIButton(
            pygame.Rect((175, 370), (110, 40)),
            'Play',
            self.ui_manager
        )

        # Création des éléments textuels
        self.Game_Title_Label = pygame_gui.elements.UILabel(
            pygame.Rect((115, 45), (730, 150)),
            "ROGUE-LIKE CSV",
            self.ui_manager,
            object_id="@Game_Title"
        )

    def end(self):
        self.Settings_Button.kill()
        self.Codex_Button.kill()
        self.Exit_Game_Button.kill()
        self.play_Button.kill()
        self.Game_Title_Label.kill()

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
                
            self.ui_manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.Settings_Button:
                    self.target_state_name = "settings_menu"
                    self.transition = True
                elif event.ui_element == self.Codex_Button:
                    self.target_state_name = "codex_menu"
                    self.transition = True
                elif event.ui_element == self.play_Button:
                    self.target_state_name = "game_menu"
                    self.transition = True
                elif event.ui_element == self.Exit_Game_Button:
                    self.quit_game = True


        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)

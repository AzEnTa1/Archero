import json
import pygame
from pygame.locals import *
import pygame_gui

# Importation des variables partagées
import Fonction.Affichage.Shared_Things as var

class MainMenu():

    def __init__(self, ui_manager: pygame_gui.UIManager, state_manager):

        self.name = 'main_menu'
        self.state_manager = state_manager
        self.transition = False
        self.quit_game = False

        self.state_manager.register_state(self)
        self.ui_manager = ui_manager
        self.Settings_Button = None
        self.Codex_Button = None
        self.World_1_Button = None
        self.Exit_Game_Button = None
        self.Game_Title_Label = None
        self.World_1_Label = None



    def start(self):
        # Création des boutons principaux
        self.Settings_Button = pygame_gui.elements.UIButton(
            pygame.Rect((215, 460), (150, 50)),
            'Settings',
            self.ui_manager,
            object_id="@Setting_Button"
        )
        
        self.Codex_Button = pygame_gui.elements.UIButton(
            pygame.Rect((405, 460), (150, 50)),
            'Codex',
            self.ui_manager,
            object_id="@Codex_Button"
        )
        
        self.Exit_Game_Button = pygame_gui.elements.UIButton(
            pygame.Rect((595, 460), (150, 50)),
            'Exit',
            self.ui_manager,
            object_id="@Exit_Button"
        )

        # Boutons de sélection des mondes
        self.World_1_Button = pygame_gui.elements.UIButton(
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

    def run(self, surface, time_delta):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game = True
                
            self.ui_manager.process_events(event)

        self.ui_manager.update(time_delta)

        surface.fill("#1A1D2E")

        self.ui_manager.draw_ui(surface)
'''

def Display_Home(Screen, Running, Time_Delta):
    """
    Gère l'affichage et les interactions du menu principal.
    
    Args:
        Screen (pygame.Surface): Surface d'affichage
        Running (bool): État de la boucle principale
        Time_Delta (float): Temps écoulé depuis la dernière frame
    
    Returns:
        bool: Nouvel état de la boucle principale
    """
    global Play_Button, Settings_Button
    
    # Gestion des événements
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

        var.Manager.process_events(Event)
        
        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            # Gestion des actions des boutons
            if Event.ui_element == Exit_Game_Button:
                Running = False
            elif Event.ui_element in [World_1_Button, World_2_Button, World_3_Button]:
                # Transition vers l'écran de chargement
                End_Home_Menu()
                var.Transition = True
                var.Monde_Choisi = 1 if Event.ui_element == World_1_Button else 2 if Event.ui_element == World_2_Button else 3
                var.Switch_Menu("Loading_Game")
            elif Event.ui_element == Settings_Button:
                End_Home_Menu()
                var.Transition = True
                var.Switch_Menu("Settings")
            elif Event.ui_element == Codex_Button:
                End_Home_Menu()
                var.Transition = True
                var.Switch_Menu("Codex")

    # Mise à jour de l'interface
    var.Manager.update(Time_Delta)

    # Dessin de l'arrière-plan et des décors
    Screen.fill("#1A1D2E")
    # Encadrés décoratifs autour des labels
    for label_rect in [var.Game_Title_Label, var.World_1_Label, var.World_2_Label, var.World_3_Label]:
        pygame.draw.rect(Screen, '#ffff00', label_rect)
        pygame.draw.rect(Screen, '#1B263B', label_rect.scale_by(0.96))

    # Affichage des éléments d'interface
    var.Manager.draw_ui(Screen)

    return Running
    '''
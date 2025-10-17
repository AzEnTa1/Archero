import json
import pygame
from pygame.locals import *
import pygame_gui

# Importation des variables partagées
import Fonction.Affichage.Shared_Things as var

def Init_Home_Menu():
    """
    Initialise tous les éléments d'interface du menu principal.
    
    Crée et configure :
    - Les boutons de navigation (Settings, Codex, Exit)
    - Les boutons de sélection de monde
    - Les labels d'information des mondes
    - Le titre du jeu
    
    Returns:
        list: Liste de tous les éléments d'interface créés
    """
    global Ui_Elem, Settings_Button, Codex_Button, World_1_Button, World_2_Button, World_3_Button, Exit_Game_Button, Game_Title_Label, World_1_Label, World_2_Label, World_3_Label, World_2_Label, World_3_Label
    
    # Création des boutons principaux
    Settings_Button = pygame_gui.elements.UIButton(
        var.Settings_Button_Rect,
        'Settings',
        var.Manager,
        object_id="@Setting_Button"
    )
    
    Codex_Button = pygame_gui.elements.UIButton(
        var.Codex_Button,
        'Codex',
        var.Manager,
        object_id="@Codex_Button"
    )
    
    Exit_Game_Button = pygame_gui.elements.UIButton(
        var.Exit_Game_Button,
        'Exit',
        var.Manager,
        object_id="@Exit_Button"
    )

    # Boutons de sélection des mondes
    World_1_Button = pygame_gui.elements.UIButton(
        var.World_1_Button,
        'Play',
        var.Manager
    )
    
    World_2_Button = pygame_gui.elements.UIButton(
        var.World_2_Button,
        'Play',
        var.Manager
    )
    
    World_3_Button = pygame_gui.elements.UIButton(
        var.World_3_Button,
        'Play',
        var.Manager
    )

    # Création des éléments textuels
    Game_Title_Label = pygame_gui.elements.UILabel(
        var.Game_Title_Label,
        "ROGUE-LIKE CSV",
        var.Manager,
        object_id="@Game_Title"
    )
    
    # Labels d'information des mondes
    World_1_Label = pygame_gui.elements.UILabel(
        var.World_1_Info_Rect,
        '',
        var.Manager,
        object_id="@WorldLabel"
    )
    
    World_2_Label = pygame_gui.elements.UILabel(
        var.World_2_Info_Rect,
        '',
        var.Manager,
        object_id="@WorldLabel"
    )
    
    World_3_Label = pygame_gui.elements.UILabel(
        var.World_3_Info_Rect,
        '',
        var.Manager,
        object_id="@WorldLabel"
    )

    # Regroupement de tous les éléments
    Ui_Elem = [
        Settings_Button,
        Codex_Button,
        World_1_Button,
        World_2_Button,
        World_3_Button,
        Exit_Game_Button,
        Game_Title_Label,
        World_1_Label,
        World_2_Label,
        World_3_Label
    ]
    
    return Ui_Elem

def End_Home_Menu():
    """Masque tous les éléments du menu principal"""
    for Elem in Ui_Elem:
        Elem.hide()

def Start_Home_Menu():
    """
    Initialise l'affichage des données des mondes.
    
    Charge les données depuis les fichiers JSON et:
    - Affiche 'Nouvelle Partie' si première partie
    - Affiche les statistiques sauvegardées sinon
    - Gère les erreurs de chargement des fichiers
    """
    # Chargement des données pour chaque monde
    for monde in [1, 2, 3]:
        try:
            with open(f"Data/World_{monde}/World_{monde}.json", 'r') as f:
                data = json.load(f)
                
                # Détermination du texte à afficher
                if data.get("Nouvelle_Partie", 1) == 1:
                    texte = "Nouvelle Partie"
                else:
                    texte = (f"Cœurs: {data.get('Heart', 0)}\n"
                             f"Score: {data.get('High Score', 0)}\n"
                             f"M: {data.get('Monde', 'Inc')}\n")

                # Mise à jour du label correspondant
                if monde == 1: 
                    World_1_Label.set_text(texte)
                elif monde == 2: 
                    World_2_Label.set_text(texte)
                else: 
                    World_3_Label.set_text(texte)
                
        except Exception as e:
            print(f"Erreur chargement monde {monde}: {str(e)}")
            # Texte par défaut en cas d'erreur
            if monde == 1: 
                World_1_Label.set_text("Nouvelle Partie")
            elif monde == 2: 
                World_2_Label.set_text("Nouvelle Partie")
            else: 
                World_3_Label.set_text("Nouvelle Partie")
    
    # Affichage de tous les éléments
    for Elem in Ui_Elem:
        Elem.show()

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
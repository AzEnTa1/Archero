import pygame
from pygame.locals import *
import pygame_gui
import json
import Fonction.Affichage.Shared_Things as var


# Variables globales pour les éléments d'interface
Ui_Elem = []
Back_Home_Button = None
High_Score_Label = None
Cumulated_Score_Label = None


def Init_Codex_Menu():
    """Initialise les éléments d'interface du menu Codex."""
    global Ui_Elem, Back_Home_Button, High_Score_Label, Cumulated_Score_Label
    
    # Création du bouton de retour à l'accueil
    Back_Home_Button = pygame_gui.elements.UIButton(
        var.Back_Home_Button_Rect,
        'Home',
        var.Manager
    )
    
    # Création des labels pour afficher les scores
    High_Score_Label = pygame_gui.elements.UILabel(
        var.High_Score_Label_Rect,
        'Meilleur Score: 0',
        var.Manager,
        object_id='@Score_Label'
    )
    
    Cumulated_Score_Label = pygame_gui.elements.UILabel(
        var.Cumulated_Score_Label_Rect, 
        'Score cumulé: 0',
        var.Manager,
        object_id='@Score_Label'
    )
    
    # Stockage des éléments d'interface
    Ui_Elem = [Back_Home_Button, High_Score_Label, Cumulated_Score_Label]
    
    # Masquage initial des éléments
    End_Codex_Menu()


def End_Codex_Menu():
    """Masque tous les éléments d'interface du menu Codex."""
    for Elem in Ui_Elem:
        Elem.hide()


def Start_Codex_Menu():
    """Affiche le menu Codex et charge les scores des différents mondes."""
    high_scores = []
    total_score = 0
    
    # Chargement des scores depuis les fichiers des mondes
    for i in range(1, 4):
        try:
            with open(f"Data/World_{i}/World_{i}.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                world_score = data.get("High Score", 0)
                high_scores.append(world_score)
                total_score += world_score
        except (FileNotFoundError, json.JSONDecodeError):
            high_scores.append(0)
    
    # Mise à jour des labels avec les scores calculés
    High_Score_Label.set_text(f"Meilleur Score: {max(high_scores)}")
    Cumulated_Score_Label.set_text(f"Score cumulé: {total_score}")
    
    # Affichage des éléments d'interface
    for Elem in Ui_Elem:
        Elem.show()


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
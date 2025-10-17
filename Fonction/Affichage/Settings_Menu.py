import pygame
from pygame.locals import *
import pygame_gui

# Importation des variables partagées
import Fonction.Affichage.Shared_Things as var

def Init_Settings_Menu():
    """
    Initialise les éléments d'interface du menu des paramètres.
    
    Crée :
    - Bouton de retour au menu principal
    - Curseur de réglage des FPS
    - Label d'affichage des FPS
    """
    global Ui_Elem, Back_Home_Button, FPS_Slider, FPS_Label

    # Création du bouton de retour
    Back_Home_Button = pygame_gui.elements.UIButton(
        var.Back_Home_Button_Rect,
        'Home',
        var.Manager
    )
    
    # Configuration du curseur FPS
    Slider_Rect = pygame.Rect(735, 175, 200, 30)  # Rectangle de positionnement
    FPS_Slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=Slider_Rect,
        start_value=var.FPS,  # Valeur initiale
        value_range=(1, 301),  # Plage de réglage
        manager=var.Manager,
        object_id="@FPS_Slider"
    )

    # Création du label FPS
    Label_RECT = pygame.Rect(735, 145, 200, 30)
    FPS_Label = pygame_gui.elements.UILabel(
        relative_rect=Label_RECT,
        text=f"FPS: {var.FPS}",  # Texte initial
        manager=var.Manager,
        object_id="@FPS_Label"
    )

    Ui_Elem = [Back_Home_Button, FPS_Slider, FPS_Label]
    End_Settings_Menu()  # Masque les éléments par défaut

def End_Settings_Menu():
    """Masque tous les éléments du menu des paramètres"""
    for Elem in Ui_Elem:
        Elem.hide()

def Start_Settings_Menu():
    """Affiche tous les éléments du menu des paramètres"""
    for Elem in Ui_Elem:
        Elem.show()

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
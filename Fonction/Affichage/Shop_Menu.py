import pygame
from pygame.locals import *
import pygame_gui

import Fonction.Affichage.Shared_Things as var


# Variables globales pour les éléments d'interface
Ui_Elem = []
Back_Home_Button = None


def Init_Shop_Menu():
    """Initialise les éléments d'interface du menu du magasin."""
    global Ui_Elem, Back_Home_Button
    
    # Création du bouton de retour à l'accueil
    Back_Home_Button = pygame_gui.elements.UIButton(
        var.Back_Home_Button_Rect,
        'Home',
        var.Manager
    )
    
    # Stockage des éléments d'interface
    Ui_Elem = [Back_Home_Button]
    
    # Masquage initial des éléments
    End_Shop_Menu()


def End_Shop_Menu():
    """Masque tous les éléments d'interface du menu du magasin."""
    for Elem in Ui_Elem:
        Elem.hide()


def Start_Shop_Menu():
    """Affiche tous les éléments d'interface du menu du magasin."""
    for Elem in Ui_Elem:
        Elem.show()


def Display_Shop(Screen, Running, Time_Delta):
    """Affiche le menu du magasin et gère les interactions.
    
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
                End_Shop_Menu()
                var.Transition = True
                var.switch_menu("Home")

    # Mise à jour de l'interface
    var.Manager.update(Time_Delta)

    # Affichage de l'arrière-plan
    Screen.fill("#666666")

    # Dessin de l'interface
    var.Manager.draw_ui(Screen)

    return Running
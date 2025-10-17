"""
Module de gestion de l'écran de jeu principal
Contient les fonctions pour le gameplay principal Higher/Lower
"""

import pygame
from pygame.locals import *
import pygame_gui
import json

import Fonction.Affichage.Shared_Things as var
from Fonction.CSV import *

# Variables globales pour l'interface
Ui_Elem = []          # Liste des éléments UI
Higher = None         # Bouton Higher
Lower = None          # Bouton Lower
Label_Category_1 = None  # Label catégorie 1
Label_Category_2 = None  # Label catégorie 2
Label_From = None     # Label "From ?"
value_1 = 0           # Première valeur à comparer
value_2 = 0           # Deuxième valeur à comparer
Data = None           # Données de la partie

def Init_Game_Menu():
    """
    Initialise le menu de jeu.
    Crée tous les éléments d'interface utilisateur nécessaires.
    """
    global Ui_Elem, Higher, Lower, Label_Category_1, Label_Category_2, Label_From, value_2, value_1
    
    # Création des boutons Higher/Lower
    Higher = pygame_gui.elements.UIButton(
        var.Higher_Rect,
        'Higher',
        var.Manager,
        object_id="@Higher_Button"
    )
    Lower = pygame_gui.elements.UIButton(
        var.Lower_Rect,
        'Lower',
        var.Manager,
        object_id="@Lower_Button"
    )
    
    # Création des labels
    Label_Category_1 = pygame_gui.elements.UITextBox(
        "Category 1",
        var.Label_Category_1_Rect,
        var.Manager,
        object_id="@Label_Category_1"
    )
    Label_Category_2 = pygame_gui.elements.UITextBox(
        "Category 2",
        var.Label_Category_2_Rect,
        var.Manager,
        object_id="@Label_Category_2"
    )
    Label_From = pygame_gui.elements.UILabel(
        var.Label_From_Rect,
        "From ?",
        var.Manager,
        object_id="@Label_From"
    )
    
    # Initialisation des valeurs
    value_1, value_2 = 0, 0
    Ui_Elem = [Higher, Lower, Label_Category_1, Label_Category_2, Label_From]
    
    End_Game_Menu()

def End_Game_Menu():
    """
    Termine le menu de jeu.
    Masque tous les éléments d'interface.
    """
    for Elem in Ui_Elem:
        Elem.hide()

def Start_Game_Menu():
    """
    Démarre le menu de jeu.
    Charge les données et prépare l'affichage des valeurs à comparer.
    """
    global Data, value_1, value_2, Difficulty

    # Affichage des éléments UI
    for Elem in Ui_Elem:
        Elem.show()

    # Chargement des données de la partie
    with open(var.Dossier_Monde, 'r', encoding='utf-8') as Fichier:
        Data = json.load(Fichier)
    pygame.display.set_caption(f"Higher Lower Game - {Data['Nom']}")

    if var.Current_Tile == "Boss":
        Difficulty = var.Difficulté + 1
    elif var.Current_Tile == "Shop":
        Difficulty = var.Difficulté
        if not random.randint(0, 5):
            Data["Heart"] += 1
            Difficulty = var.Difficulté - 1
    else:
        Difficulty = var.Difficulté

    # Génération des valeurs à comparer
    if not value_2:  # Première comparaison
        value_1 = get_value(3)
        value_2 = get_value(Difficulty)
    else:  # Comparaisons suivantes
        value_1 = value_2
    
    # Garantir que les valeurs sont différentes
    while value_1 == value_2:
        value_2 = get_value(Difficulty)
    
    # Mise à jour des textes
    Label_From.set_text(f"From {value_1[0]}")
    Label_Category_1.set_text(
        f"« {str(value_1[1])} » est de {str(value_1[3])} de la catégorie « {str(value_1[2])} » <br/> est ce que c'est"
    )
    Label_Category_2.set_text(
        f"à « {str(value_2[1])} » de la catégorie « {str(value_2[2])} »"
    )

def Display_Game(Screen, Running, Time_Delta):
    """
    Affiche l'écran de jeu et gère les interactions.
    
    Args:
        Screen: Surface PyGame où afficher
        Running: État actuel du jeu
        Time_Delta: Temps écoulé depuis la dernière frame
    
    Returns:
        bool: État du jeu après traitement
    """
    # Gestion des événements
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

        var.Manager.process_events(Event)

        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            if Event.ui_element == Higher:
                if value_1[3] >= value_2[3]:
                    win()
                else:
                    lost()
            elif Event.ui_element == Lower:
                if value_2[3] >= value_1[3]:
                    win()
                else:
                    lost()

    # Mise à jour de l'affichage
    var.Manager.update(Time_Delta)
    Screen.fill("#0F2027")
    var.Display_Health(Data["Heart"])
    var.Manager.draw_ui(Screen)

    return Running

def handle_guess(guess_higher):
    """
    Gère le résultat d'une tentative du joueur.
    
    Args:
        guess_higher: True si le joueur a choisi "Higher", False pour "Lower"
    """
    if (guess_higher and value_1 >= value_2) or (not guess_higher and value_1 <= value_2):
        win()
    else:
        lost()

def win():
    """
    Gère le cas où le joueur a deviné correctement.
    Incrémente le score et retourne à la carte.
    """
    global Data
    print("win")
    End_Game_Menu()
    var.Transition = True
    var.Switch_Menu("Map")
    Data["High Score"] += 1
    
    # Sauvegarde des données
    with open(var.Dossier_Monde, 'w', encoding='utf-8') as Fichier:
        json.dump(Data, Fichier, indent=4, ensure_ascii=False)

def lost():
    """
    Gère le cas où le joueur s'est trompé.
    Décrémente les vies ou réinitialise la partie si plus de vies.
    """
    global value_2, Data
    print("lost")
    Data["Heart"] -= 1
    
    if Data["Heart"] <= 0:  # Game Over
        reset_game()
    else:  # Continuer avec une vie en moins
        with open(var.Dossier_Monde, 'w', encoding='utf-8') as Fichier:
            json.dump(Data, Fichier, indent=4, ensure_ascii=False)
        change_CSV()
        value_2 = 0
        End_Game_Menu()
        var.Transition = True
        var.Switch_Menu("Map")

def reset_game():
    """
    Réinitialise complètement la partie (Game Over).
    """
    global Data
    End_Game_Menu()
    var.Transition = True
    var.Switch_Menu("Home")
    
    # Réinitialisation des données
    Data = {
        "Nouvelle_Partie": 1,
        "Nom": "",
        "Map": [],
        "Difficulté": 1,
        "Heart": 5,
        "Dalle_Shop": 0,
        "Dalle_Boss": 0,
        "High Score": 0
    }
    
    # Sauvegarde
    with open(var.Dossier_Monde, 'w', encoding='utf-8') as Fichier:
        json.dump(Data, Fichier, indent=4, ensure_ascii=False)
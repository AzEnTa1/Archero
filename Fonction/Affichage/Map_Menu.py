"""
Module de gestion de la carte du jeu Higher Lower Game
Contient les fonctions pour afficher et interagir avec la carte du monde
"""

import pygame
from pygame.locals import *
import pygame_gui
import json
import random

import Fonction.Affichage.Shared_Things as var

# Variables globales
Ui_Elem = []  # Liste des éléments d'interface utilisateur
Back_Home_Button = None  # Bouton pour retourner à l'accueil
Data = None  # Données du monde chargées depuis le fichier JSON
choice_tile_map = []  # Types de tuiles disponibles pour les prochains mouvements

def Init_Map_Menu():
    """
    Initialise le menu de la carte.
    Crée les éléments d'interface utilisateur nécessaires.
    """
    global Ui_Elem, Back_Home_Button
    Back_Home_Button = pygame_gui.elements.UIButton(
        var.Back_Home_Button_Rect,
        'Home',
        var.Manager
    )
    Ui_Elem = [Back_Home_Button]
    End_Map_Menu()

def End_Map_Menu():
    """
    Termine le menu de la carte.
    Masque tous les éléments d'interface utilisateur.
    """
    for Elem in Ui_Elem:
        Elem.hide()

def Start_Map_Menu():
    """
    Démarre le menu de la carte.
    Charge les données du monde et prépare les tuiles disponibles.
    """
    global Data, choice_tile_map
    for Elem in Ui_Elem:
        Elem.show()
    
    # Chargement des données du monde
    with open(var.Dossier_Monde, 'r', encoding='utf-8') as Fichier:
        Data = json.load(Fichier)
    pygame.display.set_caption(f"Higher Lower Game - {Data['Nom']}")

    # Génération aléatoire des types de tuiles disponibles
    choice_tile_map = []
    for i in range(4):
        if random.randint(Data["Dalle_Boss"], 10) == 10:
            Data["Dalle_Boss"] = 0
            choice_tile_map.append("Boss")
        elif random.randint(Data["Dalle_Shop"], 6) == 6:
            Data["Dalle_Shop"] = 0
            choice_tile_map.append("Shop")
        else:
            Data["Dalle_Shop"] += 1
            Data["Dalle_Boss"] += 1
            choice_tile_map.append("Classics")

def Display_Map(Screen, Running, Time_Delta):
    """
    Affiche la carte et gère les interactions.
    
    Args:
        Screen: Surface PyGame où afficher la carte
        Running: État actuel du jeu (True si en cours)
        Time_Delta: Temps écoulé depuis la dernière frame
    
    Returns:
        bool: État du jeu après traitement (True pour continuer, False pour quitter)
    """
    var.Manager.update(Time_Delta)
    Screen.fill("#0F2027")
    
    # Directions possibles pour le déplacement sur la carte
    Direction_Map = [(65, 0), (0, 65), (-65, 0), (0, -65), (0, 0)]
    Direction_Map_2 = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
    Base_Tiles = pygame.Rect((455, 245), (50, 50))

    # Initialisation de la carte si vide
    if not Data["Map"]:
        Data["Map"].append([0, "Home"])

    # Traitement de la carte pour l'affichage
    Map = Data["Map"][::-1]
    if len(Map) > 7:
        Map = Map[:7]
    
    # Calcul des positions des tuiles sur la carte
    actual_tile_pos = (0, 0)
    map_map = [(0, 0)]
    for tile in Map[:-1]:
        pos_x, pos_y = actual_tile_pos
        add_x, add_y = Direction_Map_2[tile[0]]
        actual_tile_pos = (pos_x - add_x, pos_y - add_y)
        map_map.append(actual_tile_pos)

    # Affichage des tuiles existantes
    for i in range(len(Map)):
        Tile_pos_x, Tile_pos_y = map_map[i]
        player = False
        if i == 0:  # Position actuelle du joueur
            Tile_pos_x, Tile_pos_y = 0, 0
            player = True
        Tile_name = Map[i][1]
        Map_Tile = Base_Tiles.move(Tile_pos_x*65, Tile_pos_y*65)
        draw_tile(Screen, Map_Tile, Tile_name, player=player)
    
    # Calcul et affichage des tuiles disponibles pour le prochain mouvement
    last_x, last_y = map_map[0]
    possible_tiles = []
    for i in range(4):
        x, y = Direction_Map_2[i]
        new_Tile_pos = (last_x + x, last_y + y)
        if new_Tile_pos not in map_map:
            possible_tiles.append(new_Tile_pos)
            tile_type = choice_tile_map[i]
            draw_tile(Screen, Base_Tiles.move((new_Tile_pos[0])*65, (new_Tile_pos[1])*65),
                      tile_type, True)
        else:
            possible_tiles.append(0)

    # Affichage des éléments d'interface
    var.Display_Health(Data["Heart"])
    var.Manager.draw_ui(Screen)

    # Gestion des événements
    Map = Map[::-1]
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False
        
        elif Event.type == pygame.KEYDOWN:
            # Gestion des déplacements avec les touches directionnelles
            if Event.key == pygame.K_RIGHT and possible_tiles[0]:
                var.Current_Tile = choice_tile_map[0]
                Map.append([0, var.Current_Tile])
                start_game(Map, Data)
            elif Event.key == pygame.K_DOWN and possible_tiles[1]:
                var.Current_Tile = choice_tile_map[1]
                Map.append([1, var.Current_Tile])
                start_game(Map, Data)
            elif Event.key == pygame.K_LEFT and possible_tiles[2]:
                var.Current_Tile = choice_tile_map[2]
                Map.append([2, var.Current_Tile])
                start_game(Map, Data)
            elif Event.key == pygame.K_UP and possible_tiles[3]:
                var.Current_Tile = choice_tile_map[3]
                Map.append([3, var.Current_Tile])
                start_game(Map, Data)

        var.Manager.process_events(Event)
        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            if Event.ui_element == Back_Home_Button:
                End_Map_Menu()
                var.Transition = True
                var.Switch_Menu("Home")

    return Running

def draw_tile(Screen, rect, type, choice_rect=False, player=False):
    """
    Dessine une tuile sur la carte.
    
    Args:
        Screen: Surface PyGame où dessiner
        rect: Rectangle définissant la position et taille de la tuile
        type: Type de tuile ('Home', 'Boss', 'Shop' ou 'Classics')
        choice_rect: Si True, la tuile est une option de déplacement disponible
        player: Si True, la tuile représente la position actuelle du joueur
    """
    if not choice_rect:
        pygame.draw.rect(Screen, '#000000', rect.inflate(6, 6))
        pygame.draw.rect(Screen, '#2C3E50', rect)
    else:
        pygame.draw.rect(Screen, "#00ff00", rect)
    
    # Couleurs spécifiques selon le type de tuile
    if type == "Home":
        pygame.draw.rect(Screen, '#5EA83F', rect.inflate(6, 6))
    elif type == "Boss":
        pygame.draw.rect(Screen, '#000000', rect.inflate(-14, -14))
        pygame.draw.rect(Screen, '#503d4d', rect.inflate(-20, -20))
    elif type == "Shop":
        pygame.draw.rect(Screen, '#000000', rect.inflate(-14, -14))
        pygame.draw.rect(Screen, '#ddaa00', rect.inflate(-20, -20))
    
    # Marqueur du joueur
    if player:
        pygame.draw.rect(Screen, '#ff0000', rect.inflate(-30, -30))

def start_game(Map, Data):
    """
    Démarre une nouvelle partie avec la tuile sélectionnée.
    
    Args:
        Map: Liste des tuiles de la carte
        Data: Données du monde à sauvegarder
    """
    # Mise à jour de la carte dans le fichier JSON
    Data["Map"].append(Map[-1])
    with open(var.Dossier_Monde, 'w', encoding='utf-8') as Fichier:
        json.dump(Data, Fichier, indent=4, ensure_ascii=False)
    
    # Changement vers l'écran de jeu
    End_Map_Menu()
    var.Transition = True
    var.Switch_Menu("Game")
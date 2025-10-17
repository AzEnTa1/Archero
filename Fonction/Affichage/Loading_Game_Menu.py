import json
import pygame
from pygame.locals import *
import pygame_gui
import Fonction.Affichage.Shared_Things as var

# Variables globales pour les éléments d'interface
Ui_Elem = []
Back_Home_Button = None
Start_Game_Button = None
Facile_Game_Button = None
Moyen_Game_Button = None
Difficile_Game_Button = None
Nom_Entry = None
Error_Label = None

def Init_Loading_Game_Menu():
    """Initialise tous les éléments d'interface du menu de chargement."""
    global Ui_Elem, Back_Home_Button, Start_Game_Button, Facile_Game_Button, \
           Moyen_Game_Button, Difficile_Game_Button, Nom_Entry, Error_Label
    
    # Création des boutons
    Back_Home_Button = pygame_gui.elements.UIButton(
        var.Back_Home_Button_Rect,
        'Back',
        var.Manager
    )
    Start_Game_Button = pygame_gui.elements.UIButton(
        var.Start_Game_Button_Rect,
        'Start',
        var.Manager
    )
    Facile_Game_Button = pygame_gui.elements.UIButton(
        var.Facile_Game_Button_Rect,
        'Facile',
        var.Manager
    )
    Moyen_Game_Button = pygame_gui.elements.UIButton(
        var.Moyen_Game_Button_Rect,
        'Moyen',
        var.Manager
    )
    Difficile_Game_Button = pygame_gui.elements.UIButton(
        var.Difficile_Game_Button_Rect,
        'Difficile',
        var.Manager
    )
    
    # Création des champs de texte
    Nom_Entry = pygame_gui.elements.UITextEntryLine(
        var.Nom_Entry_Rect,
        manager=var.Manager,
        object_id="@Nom_Entry"
    )
    Error_Label = pygame_gui.elements.UILabel(
        var.Error_Label_Rect,
        '',
        var.Manager,
        object_id='@Error_Label'
    )
    
    # Stockage des éléments
    Ui_Elem = [
        Back_Home_Button, Start_Game_Button, Facile_Game_Button,
        Moyen_Game_Button, Difficile_Game_Button, Nom_Entry, Error_Label
    ]
    
    End_Loading_Game_Menu()

def End_Loading_Game_Menu():
    """Masque tous les éléments du menu de chargement."""
    for Elem in Ui_Elem:
        Elem.hide()

def Start_Loading_Game_Menu():
    """Configure et affiche le menu de chargement selon l'état de la partie."""
    var.Dossier_Monde = fr"Data/World_{var.Monde_Choisi}/World_{var.Monde_Choisi}.json"
    
    try:
        with open(var.Dossier_Monde, 'r', encoding='utf-8') as Fichier:
            data = json.load(Fichier)
        nouvelle_partie = data.get("Nouvelle_Partie", 1)
        nom = data.get("Nom", "")
        difficulte = data.get("Difficulté", 1)
    except FileNotFoundError:
        nouvelle_partie = 1
        nom = ""
        difficulte = 1

    # Configuration selon nouvelle partie ou partie existante
    if nouvelle_partie == 1:
        configure_nouvelle_partie(difficulte)
    else:
        configure_partie_existante(nom)

    # Éléments toujours visibles
    Back_Home_Button.show()
    Start_Game_Button.show()

def configure_nouvelle_partie(difficulte):
    """Configure l'interface pour une nouvelle partie."""
    Nom_Entry.show()
    Nom_Entry.enable()
    Nom_Entry.set_text("")
    Facile_Game_Button.show()
    Moyen_Game_Button.show()
    Difficile_Game_Button.show()
    var.Difficulté = difficulte
    Error_Label.hide()

def configure_partie_existante(nom):
    """Configure l'interface pour une partie existante."""
    Nom_Entry.show()
    Nom_Entry.disable()
    Nom_Entry.set_text(nom)
    Facile_Game_Button.hide()
    Moyen_Game_Button.hide()
    Difficile_Game_Button.hide()
    Error_Label.hide()

def Display_Loading_Game_Menu(Screen, Running, Time_Delta):
    """Gère l'affichage et les interactions du menu de chargement.
    
    Args:
        Screen: Surface d'affichage Pygame
        Running: État de la boucle principale
        Time_Delta: Temps écoulé depuis la dernière frame
        
    Returns:
        bool: État de la boucle principale (True pour continuer)
    """
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

        var.Manager.process_events(Event)

        if Event.type == pygame_gui.UI_BUTTON_PRESSED:
            handle_button_press(Event.ui_element)

    update_display(Screen, Time_Delta)
    return Running

def handle_button_press(ui_element):
    """Gère les actions des différents boutons."""
    if ui_element == Back_Home_Button:
        End_Loading_Game_Menu()
        var.Transition = True
        var.Switch_Menu("Home")
    elif ui_element in (Facile_Game_Button, Moyen_Game_Button, Difficile_Game_Button):
        handle_difficulty_selection(ui_element)
    elif ui_element == Start_Game_Button:
        handle_start_game()

def handle_difficulty_selection(button):
    """Définit la difficulté selon le bouton sélectionné."""
    if button == Facile_Game_Button:
        var.Difficulté = 1
    elif button == Moyen_Game_Button:
        var.Difficulté = 2
    elif button == Difficile_Game_Button:
        var.Difficulté = 3

def handle_start_game():
    """Gère le démarrage du jeu avec validation des données."""
    with open(var.Dossier_Monde, 'r', encoding='utf-8') as Fichier:
        var.Data_Monde = json.load(Fichier)
    
    if var.Data_Monde.get("Nouvelle_Partie", 1) == 1:
        if not validate_new_game():
            return  # Arrête si validation échoue
    
    save_and_start_game()

def validate_new_game():
    """Valide les données d'une nouvelle partie."""
    Nom = Nom_Entry.get_text().strip()
    if not Nom:
        Error_Label.set_text("Veuillez entrer un nom de monde!")
        Error_Label.show()
        return False
    return True

def save_and_start_game():
    """Sauvegarde les données et démarre le jeu."""
    if var.Data_Monde.get("Nouvelle_Partie", 1) == 1:
        configure_new_game_data()
    
    with open(var.Dossier_Monde, 'w', encoding='utf-8') as Fichier:
        json.dump(var.Data_Monde, Fichier, indent=4, ensure_ascii=False)
    
    End_Loading_Game_Menu()
    var.Transition = True
    var.Switch_Menu("Map")

def configure_new_game_data():
    """Configure les données pour une nouvelle partie."""
    var.Data_Monde["Nom"] = Nom_Entry.get_text().strip()
    var.Data_Monde["Difficulté"] = var.Difficulté
    var.Data_Monde["Nouvelle_Partie"] = 0
    
    # Configuration des vies selon la difficulté
    difficulty_hearts = {
        1: 5,
        2: 3,
        3: 2
    }
    var.Data_Monde["Heart"] = difficulty_hearts.get(var.Difficulté, 3)

def update_display(Screen, Time_Delta):
    """Met à jour l'affichage du menu."""
    var.Manager.update(Time_Delta)
    Screen.fill("#1A1D2E")  # Fond bleu nuit
    var.Manager.draw_ui(Screen)
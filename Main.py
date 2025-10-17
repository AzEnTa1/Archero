# Importation des modules externes
import pygame
from pygame.locals import *
import pygame_gui

# Importation des fonctions personnalisées
from Fonction.Affichage.Menu_Manager import *
from Fonction.CSV import *
import Fonction.Affichage.Shared_Things as var  # Variables partagées

# Chargement de l'icône de la fenêtre
Window_Game_Icon = pygame.image.load(r"Image/Window_Icon.png")

# Initialisation de Pygame et configuration de base
pygame.init()

# Configuration initiale de la fenêtre
Screen_Size = (960, 540)  # Taille de la fenêtre en pixels
Screen = pygame.display.set_mode(Screen_Size)
pygame.display.set_icon(Window_Game_Icon)
pygame.display.set_caption("Higher Lower Game")  # Titre de la fenêtre

# Création des surfaces et gestionnaires d'interface
Background = pygame.Surface(Screen_Size)  # Surface pour l'arrière-plan
Manager = pygame_gui.UIManager(
    Screen.get_size(), 
    r'Fonction/Affichage/Theme/Theme.json'  # Thème de l'interface
)
Clock = pygame.time.Clock()  # Gestion du taux de rafraîchissement

# Initialisation des composants graphiques
Init_All(Manager, Screen)  # Configuration des éléments d'interface
change_CSV()  # Changement de fichier CSV
Running = True  # Contrôle l'exécution de la boucle principale
Chemin_CSV = Trouver_CSV(r"Data/CSV")  # Recherche du fichier CSV de données

# Boucle principale du jeu
while Running:
    # Contrôle du taux de rafraîchissement (FPS)
    Frame_Time = Clock.tick(var.FPS)  # Temps écoulé depuis le dernier tick
    Time_Delta = min(Frame_Time/1000.0, 0.1)  # Deltatime pour les animations
    
    # Mise à jour de l'état du jeu et gestion des menus
    Running = Display_Menu(Screen, Running, Time_Delta)
    
    # Rafraîchissement de l'affichage
    pygame.display.flip()

# Quitter la fenètre Pygame à la fermeture
pygame.quit()
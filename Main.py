# Importation des modules externes
import pygame
from pygame.locals import *
import pygame_gui

# Importation des fonctions personnalisées
from Fonction.Affichage.Menu_Manager import *
from Fonction.Affichage.Settings import * # Variables partagées

# Chargement de l'icône de la fenêtre
#Window_Game_Icon = pygame.image.load(r"Image/Window_Icon.png")

# Initialisation de Pygame et configuration de base
pygame.init()

# Configuration initiale de la fenêtre
screen_size = (360, 640)  # Taille de la fenêtre en pixels
screen = pygame.display.set_mode(screen_size)
#pygame.display.set_icon(Window_Game_Icon)
pygame.display.set_caption("Archero")  # Titre de la fenêtre

# Création des surfaces et gestionnaires d'interface
background = pygame.Surface(screen_size)  # Surface pour l'arrière-plan
ui_manager = pygame_gui.UIManager(
    screen.get_size(), 
    r'Fonction/Affichage/Theme/Theme.json'  # Thème de l'interface
)
clock = pygame.time.Clock()  # Gestion du taux de rafraîchissement

settings = Settings() # Contient les paramettres qui peuvent etre changer un peut partout

# Initialisation des composants graphiques
app_state_manager = AppStateManager()
MainMenu(ui_manager, app_state_manager)
SettingsMenu(ui_manager, app_state_manager, settings)
CodexMenu(ui_manager, app_state_manager)
GameMenu(ui_manager, app_state_manager)

app_state_manager.set_initial_state('main_menu')
running = True  # Contrôle l'exécution de la boucle principale

# Boucle principale du jeu
while running:
    # Contrôle du taux de rafraîchissement (FPS)
    frame_time = clock.tick(settings.fps)  # Temps écoulé depuis le dernier tick
    time_delta = min(frame_time/1000.0, 0.1)  # Deltatime pour les animations
    
    # Mise à jour de l'état du jeu et gestion des menus
    running = app_state_manager.run(screen, time_delta)
    
    # Rafraîchissement de l'affichage
    pygame.display.flip()

# Quitter la fenètre Pygame à la fermeture
pygame.quit()
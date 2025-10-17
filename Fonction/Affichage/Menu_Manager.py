# Importation des modules nécessaires
import random
from pygame.locals import *

# Importation des composants personnalisés
from .Shared_Things import Menu, Before_Loading
from .Home_Menu import *
from .Settings_Menu import *
from .Game_Menu import *
from .Map_Menu import *
from .Shop_Menu import *
from .Codex_Menu import *
from .Loading_Game_Menu import *

# Dictionnaire de correspondance entre les noms de menus 
# et leurs fonctions d'affichage associées
Menu_Display_Map = {
    "Home": Display_Home,          # Affichage du menu principal
    "Game": Display_Game,          # Affichage de l'écran de jeu
    "Settings": Display_Settings,  # Affichage des paramètres
    "Map": Display_Map,            # Affichage de la carte
    "Shop": Display_Shop,          # Affichage du magasin
    "Codex": Display_Codex,        # Affichage du codex
    "Loading_Game": Display_Loading_Game_Menu  # Affichage du chargement
}

# Dictionnaire de correspondance entre les noms de menus 
# et leurs fonctions d'initialisation
Menu_Start_Map = {
    "Home": Start_Home_Menu,           # Initialisation menu principal
    "Game": Start_Game_Menu,           # Initialisation écran de jeu
    "Settings": Start_Settings_Menu,   # Initialisation paramètres
    "Map": Start_Map_Menu,             # Initializsation carte
    "Shop": Start_Shop_Menu,           # Initialisation magasin
    "Codex": Start_Codex_Menu,         # Initialisation codex
    "Loading_Game": Start_Loading_Game_Menu  # Initialisation chargement
}

def Display_Menu(Screen, Running, Time_Delta):
    """
    Gère l'affichage dynamique des différents menus du jeu.
    
    Args:
        Screen (pygame.Surface): Surface d'affichage principale
        Running (bool): État de la boucle principale
        Time_Delta (float): Temps écoulé depuis la dernière frame
        
    Returns:
        bool: Nouvel état de la boucle principale
        
    Fonctionnement:
        - Vérifie les transitions entre menus
        - Initialise le nouveau menu si nécessaire
        - Appelle la fonction d'affichage appropriée
    """
    # Gestion des transitions entre menus
    if var.Transition:
        var.Transition = False
        pygame.display.set_caption("Higher Lower Game")  # Réinitialisation du titre
        Menu_Start_Map.get(var.Menu, Start_Home_Menu)()  # Initialisation par défaut

    # Affichage du menu courant avec gestion de fallback
    Running = Menu_Display_Map.get(var.Menu, Display_Home)(Screen, Running, Time_Delta)
    return Running

def Init_All(Manager, Screen):
    """
    Initialise tous les éléments d'interface utilisateur du jeu.
    
    Args:
        Manager (pygame_gui.UIManager): Gestionnaire d'interface
        Screen (pygame.Surface): Surface d'affichage principale
        
    Fonctionnement:
        - Effectue une pré-initialisation commune
        - Initialise chaque sous-système de menu
    """
    # Initialisation séquentielle de tous les composants
    Before_Loading(Manager, Screen)  # Pré-configuration commune
    Init_Home_Menu()          # Initialisation menu principal
    Init_Settings_Menu()       # Initialisation paramètres
    Init_Game_Menu()           # Initialisation jeu
    Init_Map_Menu()            # Initialisation carte
    Init_Shop_Menu()           # Initialisation magasin
    Init_Codex_Menu()          # Initialisation codex
    Init_Loading_Game_Menu()   # Initialisation écran de chargement
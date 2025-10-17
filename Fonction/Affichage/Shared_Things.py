import pygame


# ÉTAT DU JEU

FPS = 60              # Taux de rafraîchissement (images/seconde)

 
# RECTANGLES D'INTERFACE (POSITIONNEMENT)
 

# Menu Principal
Game_Title_Label = pygame.Rect((115, 45), (730, 150))
Settings_Button_Rect = pygame.Rect((215, 460), (150, 50))
Exit_Game_Button = pygame.Rect((595, 460), (150, 50))
Codex_Button = pygame.Rect((405, 460), (150, 50))
Start_Game_Button_Rect = pygame.Rect((735, 425), (200, 100))
Nom_Text_Entry_Rect = pygame.Rect((735, 325), (200, 50))

# Sélection de monde
World_1_Button = pygame.Rect((175, 370), (110, 40))
World_1_Label = pygame.Rect((155, 220), (150, 200))

# Paramètres
Back_Home_Button_Rect = pygame.Rect((0, 0), (100, 50))


# FONCTIONS GLOBALES
 
def Before_Loading(UiManager, Screen_2):
    """Initialise les composants principaux de l'interface"""
    global Manager, Screen
    Manager = UiManager
    Screen = Screen_2

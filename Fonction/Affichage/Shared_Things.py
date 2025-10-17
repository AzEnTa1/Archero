import pygame

 
# CONSTANTES DE COULEUR
 
BLANC = (255, 255, 255)
ROUGE = (200, 0, 0)

 
# ÉLÉMENTS D'INTERFACE PRINCIPAUX
 
Manager = None  # Gestionnaire pygame_gui
Screen = None   # Surface d'affichage principale

 
# ÉTAT DU JEU
 
Transition = False     # Gestion des transitions entre menus
Menu = "Home"          # Menu actuellement affiché
Monde_Choisi = None    # Monde sélectionné par le joueur
Difficulté = 1         # Niveau de difficulté actuel
FPS = 120              # Taux de rafraîchissement (images/seconde)
Current_Tile = "Home"  # Case actuelle sur la carte

 
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
World_1_Info_Rect = pygame.Rect(160, 280, 140, 80)
World_2_Button = pygame.Rect((425, 370), (110, 40))
World_2_Label = pygame.Rect((405, 220), (150, 200))
World_2_Info_Rect = pygame.Rect(410, 280, 140, 80)
World_3_Button = pygame.Rect((675, 370), (110, 40))
World_3_Label = pygame.Rect((655, 220), (150, 200))
World_3_Info_Rect = pygame.Rect(660, 280, 140, 80)

# Paramètres
Back_Home_Button_Rect = pygame.Rect((785, 25), (150, 75))

# Jeu
Higher_Rect = pygame.Rect((380, 350), (200, 75))
Lower_Rect = pygame.Rect((380, 425), (200, 75))
Label_Category_1_Rect = pygame.Rect((100, 125), (200, 250))
Label_Category_2_Rect = pygame.Rect((660, 125), (200, 250))
Label_From_Rect = pygame.Rect((200, 80), (560, 30))

# Chargement
Facile_Game_Button_Rect = pygame.Rect((775, 175), (150, 50))
Moyen_Game_Button_Rect = pygame.Rect((775, 250), (150, 50))
Difficile_Game_Button_Rect = pygame.Rect((775, 325), (150, 50))
Nom_Entry_Rect = pygame.Rect((500, 475), (200, 50))
Error_Label_Rect = pygame.Rect((600, 390), (400, 30))

# Codex
High_Score_Label_Rect = pygame.Rect(0, 50, 300, 40)
Cumulated_Score_Label_Rect = pygame.Rect(200, 50, 300, 40)

 
# CONFIGURATION DE LA CARTE
 
# Structure : [(Direction, Type de Case), ...]
Exemple_Map_4 = [
    (1, "Home"), (1, "Classic"), (1, "Classic"), (1, "Shop"),
    (1, "Classic"), (2, "Boss"), (3, "Boss"), (2, "Classic"),
    (2, "Classic"), (1, "Shop"), (1, "Home"), (0, "Boss"), (0, "Classic")
]

 
# FICHIERS DE CONFIGURATION
 
Dossier_Monde = fr"Data/World_{Monde_Choisi}/World_{Monde_Choisi}.json"

 
# FONCTIONS GLOBALES
 
def Before_Loading(UiManager, Screen_2):
    """Initialise les composants principaux de l'interface"""
    global Manager, Screen
    Manager = UiManager
    Screen = Screen_2

def Switch_Menu(Nouveau_Menu):
    """Change le menu actuellement affiché"""
    global Menu
    Menu = Nouveau_Menu

def Display_Health(Health):
    global Difficulté, Screen
    empty_heart = pygame.image.load(r"Image\Player_icon\Container.png")
    heart = pygame.image.load(r"Image\Player_icon\Heart.png")
    heart = pygame.transform.scale(heart, (45, 45))
    empty_heart = pygame.transform.scale(empty_heart, (45, 45))

    heart_Rect = pygame.Rect((915, 495), (45, 45))
    if Difficulté == 1:
        max_health = 5
    elif Difficulté == 2:
        max_health = 3
    elif Difficulté == 3:
        max_health = 2
    if Health > max_health:
        Health = max_health
    for i in range(max_health):
        Screen.blit(empty_heart, (915 - 45 * i, 495))
    for i in range(Health):
        Screen.blit(heart, (915 - 45 * i, 495))
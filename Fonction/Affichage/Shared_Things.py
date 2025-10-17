import pygame


# ÉTAT DU JEU

FPS = 60              # Taux de rafraîchissement (images/seconde)

 
# RECTANGLES D'INTERFACE (POSITIONNEMENT)
 

# Menu Principal
Game_Title_Label = pygame.Rect((115, 45), (730, 150))
Settings_Button_Rect = pygame.Rect((215, 460), (150, 50))
Exit_Game_Button = pygame.Rect((595, 460), (150, 50))
Codex_Button = pygame.Rect((405, 460), (150, 50))

# Sélection de monde
play_Button = pygame.Rect((175, 370), (110, 40))
play_Label = pygame.Rect((155, 220), (150, 200))

# Paramètres
Back_Home_Button_Rect = pygame.Rect((0, 0), (100, 50))



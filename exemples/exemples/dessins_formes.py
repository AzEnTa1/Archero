"""
    Dessins de lignes, rectangles, cercles, texte
"""

import pygame

taille = largeur, hauteur = 600, 400                            #Taille de la fenêtre


pygame.init()                                                   #Initialisation de tous les modules de Pygame
fenetre = pygame.display.set_mode(taille)                       #Création de la fenêtre avec les bonnes dimensions. fenetre est une Surface
fenetre.fill((255,255,255))
pygame.draw.line(fenetre, (255,0,0), (10,50), (500, 300), 5)    #dessin d'une ligne dans fenetre
pygame.draw.rect(fenetre, (128,128,128), (100,150,70,30), 0)    #dessin d'un rectangle. 100,150 sont les coordonnées haut gauche du rectangle. 70,30 sont la largeur et la hauteur.
pygame.draw.circle(fenetre, (0,255,0), (300,300), 50, 5)        #dessin d'un cercle. (300,300) sont les coordonnées du centre, 50 est le rayon.
police = pygame.font.SysFont('Arial', 20, bold=True)            #On crée la police qu'on va utiliser pour le texte (20 est la taille)
texte = police.render("Bonjour tout le monde", True, (0,128,0)) #On crée une Surface qui contient le texte à afficher (True signifie qu'on lisse le texte pour éviter le crénelage)
fenetre.blit(texte, (200,100))                                  #On affiche la Surface texte dans la Surface fenetre avec blit
pygame.display.flip()                                           #Met à jour l'affichage de la fenêtre: affiche le contenu du buffer à l'écran.

continuer = True #variable booléenne qui permet de sortir de la boucle si elle est False. On quitte pygame si elle est False
while continuer:
    for event in pygame.event.get():                            #On parcourt tous les événements générés (clavier, souris, ...)
        if event.type == pygame.QUIT:                           #Si c'est un événement qui correspond à la sortie de pygame (clic sur la croix...), continuer devient False
            continuer  = False
pygame.quit()                                                   #Ne pas oublier de quitter proprement pygame
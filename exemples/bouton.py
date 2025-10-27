"""
    Dessine un bouton à l'écran sur lequel on peut cliquer.
"""
import pygame
from pygame.locals import *                                 #Permet de charger des constantes comme KEYDOWN ou KEYUP... dans l'espace de nom de ce module. Ceci permet d'écrire KEYDOWN au lieu de pygame.KEYDOWN

taille = largeur, hauteur = 800, 600                        #Taille de la fenêtre graphique
pygame.init()                                               #Initialisation de tous les modules pygame.
fenetre = pygame.display.set_mode(taille)                   #Création de la fenêtre graphique.
bouton = pygame.image.load("bouton.png")                    #Chargement de l'image et création de l'objet bouton de type Surface
bouton_rectangle_position = bouton.get_rect()               #On récupère le rectangle où se trouve la Surface bouton
bouton_rectangle_position.center = (largeur/2, hauteur/2)   #On place le rectangle au milieu de l'écran

continuer = True
bouton_enfonce = False #Variable booléenne qui permet de savoir si le bouton a été enfoncé afin de le redécaler vers le haut lorsqu'on relâche le bouton de la souris
while continuer:
    for event in pygame.event.get():                        #On parcourt tous les événements récupérés par pygame.
        if event.type == QUIT:                              #Si c'est un événement de fermeture de fenêtre (clic sur la croix...), on sort de la boucle.
            continuer  = False
        if event.type == MOUSEBUTTONDOWN and event.button==1 and bouton_rectangle_position.collidepoint(event.pos):
            #Si c'est un événement correspondant au bouton de souris gauche enfoncé et si la souris se trouve dans le rectange
            bouton_enfonce = True
            bouton_rectangle_position = bouton_rectangle_position.move(2,2) #On décale le bouton vers le bas
            #On peut ajouter ici une fonction à exécuter
        if event.type == MOUSEBUTTONUP and bouton_enfonce:  #Si on relâche le bouton de la souris et que le bouton a été enfoncé
            bouton_rectangle_position = bouton_rectangle_position.move(-2,-2) #On décale le bouton vers le haut
            bouton_enfonce = False
    fenetre.fill((255,255,255))                             #On efface l'écran
    fenetre.blit(bouton, bouton_rectangle_position)         #On dessine le bouton à l'endroit où se trouve le rectangle
    pygame.display.flip()                                   #On met à jour l'affichage: tout ce qui a été créé dans le buffer est envoyé à l'écran
pygame.quit()

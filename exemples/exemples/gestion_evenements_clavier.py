"""
    Déplace une balle grâce aux flèches du clavier.
"""

import pygame
from pygame.locals import * #Permet de charger des constantes comme KEYDOWN ou KEYUP... dans l'espace de nom de ce module. Ceci permet d'écrire KEYDOWN au lieu de pygame.KEYDOWN

pygame.init()                               #Initialisation de tous les modules pygame.

taille = largeur, hauteur = 800, 600
vitesse = 3
noir = 0, 0, 0

fenetre = pygame.display.set_mode(taille)   #Création de la fenêtre graphique

balle = pygame.image.load("ball.png")       #Chargement de l'image
ballerect = balle.get_rect()                #On récupère le rectangle où se trouve la Surface balle
continuer = True
deplacement = 0,0
while continuer:
    for event in pygame.event.get():        #On parcourt tous les événements générés
        if event.type == QUIT:              #Si c'est de type Quitter, on sort de la boucle
            continuer  = False
        if event.type == KEYDOWN:           #Si l'événement est de type Touche enfoncée, on gère les 4 cas
            if event.key == K_DOWN:         #Flèche vers le bas: on augmente l'ordonnée et l'abscisse ne change pas, etc...
                deplacement = 0,vitesse
            if event.key == K_UP:
                deplacement = 0,-vitesse
            if event.key == K_RIGHT:
                deplacement = vitesse,0
            if event.key == K_LEFT:
                deplacement = -vitesse,0

    ballerect = ballerect.move(deplacement) #On déplace le rectangle
    fenetre.fill(noir)                      #On efface l'écran
    fenetre.blit(balle, ballerect)          #On dessine (dans le buffer) la Surface balle là où se trouve le rectangle
    pygame.display.flip()                   #On met à jour l'affichage: le contenu du buffer est envoyé à l'écran
    pygame.time.Clock().tick(100)           #On ralentit l'exécution pour les ordinateurs très rapides: la boucle est exécutée 100 fois par seconde au maximum
pygame.quit()                               #On quitte proprement pygame (nettoyage de la mémoire)
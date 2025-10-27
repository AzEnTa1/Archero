"""
    Dessine un disque de rayon et de couleur aléatoires à l'endroit où on clique avec la souris.
"""
import pygame
from pygame.locals import * #Permet de charger des constantes comme KEYDOWN ou KEYUP... dans l'espace de nom de ce module. Ceci permet d'écrire KEYDOWN au lieu de pygame.KEYDOWN
from random import randint

taille = largeur, hauteur = 800, 600                            #Taille de la fenêtre graphique
couleurs = [(255,0,0), (0,255,0), (0,0,255), (0,255,255), (255,0,255), (255,255,0), (255,255,255)]
pygame.init()                                                   #Initialisation de tous les modules pygame.
fenetre = pygame.display.set_mode(taille)                       #Création de la fenêtre graphique.

continuer = True
while continuer:
    for event in pygame.event.get():                            #On parcourt tous les événements récupérés par pygame. On peut récupérer des informations sur chaque événement en fonction de son type (touche clavier appuyée, coordonnées de la souris...)
        if event.type == QUIT:                                  #Si c'est un événement de fermeture de fenêtre (clic sur la croix...), on sort de la boucle.
            continuer  = False
        if event.type == MOUSEBUTTONDOWN and event.button==1:   #Si c'est un événement correspondant au bouton de souris gauche enfoncé
            rayon = randint(5,50)                               #rayon aléatoire
            couleur = couleurs[randint(0, 6)]                   #couleur aléatoire
            pygame.draw.circle(fenetre, couleur, event.pos , rayon, 0) #Les coordonnées de la souris sont dans event.pos Ces données sont récupérées automatiquement par pygame.
    pygame.display.flip()                                       #Mise à jour de l'affichage en affichant le contenu du buffer à l'écran. Ici, on n'efface pas l'écran à chaque fois pour conserver tous les disques affichés.
pygame.quit()

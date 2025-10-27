"""
    Dessine un bouton rectangulaire avec du texte à l'écran sur lequel on peut cliquer. Voir le résultat dans la console.
"""
import pygame
from pygame.locals import *                 #Permet de charger des constantes comme KEYDOWN ou KEYUP... dans l'espace de nom de ce module. Ceci permet d'écrire KEYDOWN au lieu de pygame.KEYDOWN

taille = largeur, hauteur = 800, 600        #Taille de la fenêtre graphique
pygame.init()                               #Initialisation de tous les modules pygame.

fenetre = pygame.display.set_mode(taille)   #Création de la fenêtre graphique.
largeur_bouton, hauteur_bouton = 150, 50    #Taille du bouton
#Une méthode pratique est de créer une Surface pour représenter le bouton. Ca évitera ensuite de faire des tests pénibles pour savoir si le curseur souris est au-dessus du bouton.
bouton = pygame.Surface((largeur_bouton, hauteur_bouton))   #On crée la Surface avec les bonnes dimensions
bouton.fill((180, 180, 180))                #On remplit le bouton de gris
pygame.draw.rect(bouton, (255, 0, 0), bouton.get_rect(), 1)
police = pygame.font.SysFont('Arial', 20, bold=True)        #On crée la police qu'on va utiliser pour le texte
texte = police.render("Cliquer ici", True, (0,128,0))       #On crée une Surface qui contient le texte à afficher
bouton.blit(texte, ((largeur_bouton-texte.get_width())/2,(hauteur_bouton-texte.get_height())/2)) #On met le texte sur le bouton en le centrant

bouton_rectangle_position = bouton.get_rect()               #On récupère le rectangle où se trouve le bouton
bouton_rectangle_position.center = (largeur/2, hauteur/2)   #On place le rectangle au milieu de l'écran

continuer = True
while continuer:
    for event in pygame.event.get():                        #On parcourt tous les événements récupérés par pygame.
        if event.type == QUIT:                              #Si c'est un événement de fermeture de fenêtre (clic sur la croix...), on sort de la boucle.
            continuer  = False
        if event.type == MOUSEBUTTONDOWN and event.button==1 and bouton_rectangle_position.collidepoint(event.pos):
            #Si c'est un événement correspondant au bouton de souris gauche enfoncé et si la souris se trouve dans le rectangle
            print("Vous avez cliqué")                       #On affiche un message dans la console
            #On peut ajouter ici une fonction à exécuter
    fenetre.fill((255,255,255))                             #On efface l'écran
    fenetre.blit(bouton, bouton_rectangle_position)         #On dessine le bouton à l'endroit où se trouve le rectangle
    pygame.display.flip() #On met à jour l'affichage: tout ce qui a été créé dans le buffer est envoyé à l'écran
pygame.quit()
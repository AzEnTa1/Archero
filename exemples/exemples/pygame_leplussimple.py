"""
Balle qui rebondit sur les bords de la fenêtre graphique.
"""
import pygame

taille = largeur, hauteur = 600, 400        #Taille de la fenêtre
vitesse = [3, 3]                            #On déplace de 3 pixels en abscisse ou 3 pixels en ordonnée à chaque fois. Plus le nombre de pixels est élevé, plus ça semble rapide.
noir = 0, 0, 0                              #Couleur pour effacer la fenêtre

pygame.init()                               #Initialisation de tous les modules de Pygame
fenetre = pygame.display.set_mode(taille)   #Création de la fenêtre avec les bonnes dimensions. fenetre est une Surface
balle = pygame.image.load("ball.png")       #Chargement de l'image qui représente la balle. balle est une Surface
ballerect = balle.get_rect()                #Attention: on ne travaille pas sur la Surface balle directement mais sur le rectangle où elle se trouve: c'est celui-ci qu'on déplace pour obtenir la nouvelle position
continuer = True                            #variable booléenne qui permet de sortir de la boucle si elle est False. On quitte pygame si elle est False
while continuer:
    for event in pygame.event.get():        #On parcourt tous les événements générés (clavier, souris, ...)
        if event.type == pygame.QUIT:       #Si c'est un événement qui correspond à la sortie de pygame (clic sur la croix...), continuer devient False
            continuer  = False
    ballerect = ballerect.move(vitesse)     #On déplace le rectangle: le nouveau rectangle obtenu correspond à la nouvelle position de l'image.Attention, on travaille dans un buffer (tampon) et rien ne se passe à l'écran ici
    if ballerect.left < 0 or ballerect.right > largeur: #On inverse le déplacement si on heurte un bord de la fenêtre
        vitesse[0] = -vitesse[0]
    if ballerect.top < 0 or ballerect.bottom > hauteur:
        vitesse[1] = -vitesse[1]
    fenetre.fill(noir)                      #On efface la totalité de la fenêtre (toujours dans le buffer) en la remplissant de noir
    fenetre.blit(balle, ballerect)          #Permet de dessiner (dans le buffer) la Surface balle à l'endroit où se trouve le rectangle ballerect
    pygame.display.flip()                   #Met à jour l'affichage de la fenêtre: affiche le contenu du buffer à l'écran.
    pygame.time.Clock().tick(100)           #Permet de ralentir l'exécution sur un ordinateur très rapide: permet d'exécuter la boucle 100 fois par seconde maximum
pygame.quit()                               #Ne pas oublier de quitter proprement pygame
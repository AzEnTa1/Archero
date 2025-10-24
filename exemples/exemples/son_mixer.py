"""
    Exemple d'utilisation du module mixer.
    Appuyer sur espace et laisser la touche enfoncée pour jouer.
    Relâcher la touche espace pour passer en pause.
    Appuyer sur la touche entrée pour recommencer à 0.
"""

import pygame
from pygame.locals import *

#Initialisation
pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("Brooklyn.mp3")#On charge le son dans un objet de type Sound

continuer = True
en_pause = False #

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = False
		#Lancer le son si on appuie sur la touche espace et que ce n'est pas en pause
		if event.type == KEYDOWN and event.key == K_SPACE and en_pause == False:
			son.play()
			en_pause = True
		#Sortir de pause si on appuie sur la touche espace et que c'est en pause
		if event.type == KEYDOWN and event.key == K_SPACE and en_pause == True:
			pygame.mixer.unpause()
		#Mettre en pause si on relâche la touche espace
		if event.type == KEYUP and event.key == K_SPACE:
			pygame.mixer.pause()
		#Stopper le son si on appuie sur entrée, pour recommencer à 0
		if event.type == KEYDOWN and event.key == K_RETURN:
			son.stop()
			en_pause = False
pygame.quit()
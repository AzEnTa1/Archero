# Boite a outil, genre des fonctions utilitaires qu'on peut rééutiliser partoutimport math
import pygame

def distance(point1, point2):
    """Calcule la distance entre deux points"""
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def load_image(path):
    """Charge une image avec gestion d'erreur"""
    try:
        return pygame.image.load(path)
    except:
        print(f"Erreur chargement image: {path}")
        return pygame.Surface((50, 50))  # Image de secours

def clamp(value, min_val, max_val):
    """Limite une valeur entre min et max"""
    return max(min_val, min(value, max_val))
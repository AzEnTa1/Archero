import os
import csv
import json
import random

def Trouver_CSV(dossier):
    """
    Recherche tous les fichiers CSV dans un dossier spécifié.
    
    Args:
        dossier (str): Chemin du dossier à analyser
        
    Returns:
        list: Liste de tuples (chemin_complet, nom_fichier) pour chaque CSV trouvé
    """
    liste_csv_path = []
    for fichier in os.listdir(dossier):
        if fichier.endswith('.csv'):
            liste_csv_path.append((os.path.join(dossier, fichier), fichier))
    return liste_csv_path

def ouvreur_csv(chemin):
    """
    Lit un fichier CSV et retourne son contenu sous forme de liste de lignes.
    
    Args:
        chemin (str): Chemin d'accès au fichier CSV
        
    Returns:
        list: Liste des lignes du CSV (chaque ligne est une liste de valeurs)
    """
    liste = []
    with open(chemin, mode='r', encoding='utf-8') as fichier:
        fichier = csv.reader(fichier)
        for i in fichier:
            liste.append(i)
    return liste

def get_csv(fichier_base):
    """
    Lit un fichier CSV et le convertit en liste de dictionnaires.
    
    Args:
        fichier_base (str): Chemin relatif du fichier CSV
        
    Returns:
        list: Liste de dictionnaires représentant chaque ligne 
              ou None en cas d'erreur
    """
    fichier = []    
    try:
        with open("./" + fichier_base, mode='r', newline='', encoding="utf-8") as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            fichier = [ligne for ligne in lecteur_csv]
    except Exception as e:
        print(f"Erreur de lecture : {str(e)}")
        fichier = None

    if not fichier:
        print("Fichier vide ou erreur de lecture")
    return fichier

def scan_keys_csv(src):
    """
    Analyse les colonnes d'un CSV pour identifier :
    - Les colonnes numériques non constantes
    - Les colonnes non numériques ou constantes
    
    Args:
        src (str): Chemin du fichier CSV
        
    Returns:
        tuple: (keys_possible, fichier, keys_inpossible)
            - keys_possible: Clés utilisables pour les comparaisons
            - fichier: Données brutes du CSV
            - keys_inpossible: Clés inutilisables
    """
    fichier = get_csv(src)
    
    if not fichier:
        print("Fichier vide / erreur de lecture")
        return []
    
    keys_possible = []
    keys_inpossible = []

    for key in fichier[0].keys():
        colonne_valide = True
        same_values = True
        valeur_initiale = fichier[0].get(key, 0)
        
        for ligne in fichier:
            val = ligne.get(key, 0)
            
            # Vérification de l'unicité des valeurs
            if same_values and val != valeur_initiale:
                same_values = False
                
            # Conversion numérique
            try:
                float(val if val != "" else 0)
            except (ValueError, TypeError):
                colonne_valide = False
                break

        # Classification des colonnes
        if colonne_valide and not same_values:
            keys_possible.append(key)
        else:
            keys_inpossible.append(key)
            
    return keys_possible, fichier, keys_inpossible

def formater_csv(CSV_path, nom_ligne_number, nom_CSV):
    """
    Formate un CSV pour le traitement des données :
    - Filtre les colonnes non numériques
    - Structure les données dans un format standard
    
    Args:
        CSV_path (str): Chemin du fichier CSV
        nom_ligne_number (int): Index de la colonne contenant les noms de lignes
        nom_CSV (str): Nom du fichier CSV source
        
    Returns:
        list: Données formatées triées par valeur numérique
              Format : [nom_csv, nom_ligne, clé, valeur, groupe]
    """
    new_fichier = []
    keys_possible, fichier, keys_inpossible = scan_keys_csv(CSV_path)
    
    for ligne in fichier:
        nom_ligne = list(ligne.values())[nom_ligne_number]
        # Nettoyage des colonnes inutilisables
        for key in keys_inpossible:
            ligne.pop(key, None)
        # Formatage des entrées valides
        for items in ligne.items():
            if items[1] != "":
                new_fichier.append([nom_CSV, nom_ligne, items[0], items[1]])
    
    # Tri par valeur numérique
    return sorted(new_fichier, key=lambda x: float(x[-1]))

def split_CSV(CSV):
    """
    Répartit les données en 5 groupes de difficulté.
    
    Args:
        CSV (list): Données formatées à splitter
        
    Returns:
        list: Liste de 5 sous-listes avec index de groupe ajouté
    """
    CSV = CSV[0]
    taille = len(CSV)
    base_size, reste = divmod(taille, 5)
    resultats = []
    debut = 0
    
    for i in range(5):
        # Calcul de la taille du groupe
        fin = debut + base_size + (1 if i < reste else 0)
        # Ajout de l'index de groupe
        groupe = [ligne + [i] for ligne in CSV[debut:fin]]
        resultats.append(groupe)
        debut = fin
        
    return resultats


def get_value(difficulty=3, liste_value1=0):
    """
    Sélectionne une valeur selon la difficulté et le contexte.
    
    Args:
        difficulty (int): Niveau de difficulté (1-3)
        liste_value1 (int): Index du groupe précédent
        
    Returns:
        list: Une entrée aléatoire du groupe sélectionné
    """
    listes = split_CSV(CSV)
    if difficulty == 0:
        difficulty = 1
    # Stratégie de sélection selon la difficulté
    if difficulty == 1:  # Mode facile
        groupe = 4 if liste_value1 < 1 else 0
    elif difficulty == 2:  # Mode moyen
        groupe = (liste_value1 + 2) % 5
    else:  # Mode difficile
        décalage = random.randint(-1, 2)
        groupe = max(0, min(liste_value1 + décalage, 4))
    return random.choice(listes[groupe])

def change_CSV():
    """
    Change le CSV de référence aléatoirement.
    Met à jour la variable globale CSV avec de nouvelles données.
    """
    global CSV
    # Mapping des colonnes de nom pour les fichiers connus
    nom_ligne_map = {"Netflix_Files.csv": 2, "World_Country_Population.csv": 0, "clash_royale_cards_info.csv": 1, "meilleurs_buteurs.csv": 0}
    # Sélection aléatoire d'un nouveau CSV
    src_CSV, nom_CSV = random.choice(Trouver_CSV("data\CSV"))
    # Génération des nouvelles données
    CSV = formater_csv(src_CSV, nom_ligne_map.get(nom_CSV, 0), nom_CSV),
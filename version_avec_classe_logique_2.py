"""
Application de la logique 2

Plusieurs utilisateurs peuvent interagir avec cette version !

# Logique 2: pour chaque opération (enregistrer, terminer, vites en cours), tu vas consulter le fichier 
"""


# Implémente les multi-visites

from datetime import datetime
import classes

cheminFichier = "donnees_visiteurs.txt"
sprtrI = " ___ "
sprtrFV = " @_V-V_@ "
sprtrVisiteVisiteur = " @_Vtr-Vte_@ "

# PROGRAMME PRINCIPAL
MENUACTIF = 0
LISTE_VISITEURS = []

# Définition du menu 0
def menuPrincipal():
  global MENUACTIF
  print(
    """
    Bienvenu sur VISITORIA \n
    1. Enregistrer une visite \n
    2. Terminer une visite \n
    3. Voir les visites en cours \n
    4. Voir les visites terminées \n
    q. Pour quitter le programme \n
    """
  )
  choix = input("selectioneé une option: ")
  if choix == "1":
    MENUACTIF = 1

  elif choix =="2":
    MENUACTIF = 2

  elif choix =="3":
    MENUACTIF = 3

  elif choix =="4":
    MENUACTIF = 4
  
  else :
     MENUACTIF = "q"

# Définition du menu 1
# supposont que le nom et prenoms sont uniques

def menuEnregistrerVisite():
  global MENUACTIF

  nom = input("Nom: ")
  prenoms = input("Prénoms: ")

  result = classes.Visiteur.chercherVisiteur(nom, prenoms)
  if result == None:
    type_piece = input("Type de pièce: ")
    num_piece = input("Numero de la piéce: ")
    visiteur = classes.Visiteur(nom, prenoms, type_piece, num_piece)
    indexLigne = -1
  else:
    visiteur, indexLigne = result
  motif_visite = input("Motif de la visite: ")
  visiteur.assignerVisite(motif_visite, indexLigne)

  MENUACTIF = 0

# Définition du menu 2
def menuTerminerVisite():
  global MENUACTIF
  nom = (input("entrée le nomdu visiteur : "))
  prenoms = (input("entrée les prenoms du visiteur : "))
  result = classes.Visiteur.chercherVisiteur(nom, prenoms)
  if result == None:
    print("Ce visiteur n'existe pas !")
  else:
    visiteur, indexLigne = result
    ID_visite = int(input("entrée ID de la visite : "))

    trouver = False
    for visite in visiteur.mes_visites :
      if visite.id == ID_visite :
        trouver = True

    if trouver == False:
      print("C'est visite n'existe pas !  \n\n")
    else:
      print("Visite terminées avec success ! \n\n")
      classes.Visite.terminerVisite(ID_visite, indexLigne)

  MENUACTIF = 0

# Définition du menu 3 : voir les visites en cours
def menuVisiteEnCours():
  global MENUACTIF

  visite_encours: list[classes.TypeVisite] = classes.Visite.listerVisitesEncours()
  for visite in visite_encours:
    print(f'{visite.visiteur.nom_complet} {visite.motif} {visite.id} {visite.heure_entree}')

  MENUACTIF = 0

# Définition du menu 4 : voir les visites terminées
def menuVisiteTerminees():
  global MENUACTIF

  visite_terminees: list[classes.TypeVisite] = classes.Visite.listerVisitesTerminees()
  for visite in visite_terminees:
    print(f'{visite.visiteur.nom_complet} {visite.motif} {visite.id} {visite.heure_entree}')

  MENUACTIF = 0

#corps du programme
while True:
  if MENUACTIF == 0:
    menuPrincipal()

  elif MENUACTIF == 1:
    menuEnregistrerVisite()

  elif MENUACTIF == 2:
    menuTerminerVisite()

  elif MENUACTIF == 3:
    menuVisiteEnCours()

  elif MENUACTIF == 4:
    menuVisiteTerminees()

  # Terminer le programme
  if MENUACTIF == "q":
    break

print("\n\n\t Fin du programme !")
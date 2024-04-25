# Implémente les multi-visites

from datetime import datetime

MENUACTIF = 0
LISTE_VISITEURS = []

# TODO 
"""
Définir un chemin vers le fichier de sauvegarde 

Formuler un format d'enregistrement des visiteurs et leurs visites dans un fichier

Faire des tests à part où: 
- tu inséres manuellement 2 visiteurs dans le fichier avec 3 visites chacun
- et où tu arrives à charger ces 2 visiteurs et leurs visites dans un fichier python à part.

Applique la logique employée à notre programme


# Logique 1: tu peux charger les visiteurs du fichiers automatiquement au lancement du programme et à la fin du programme, les écrire dans le fichier.
# Logique 2: pour chaque opération (enregistrer, terminer, vites en cours), tu vas consulter le fichier 
# Logique n: tant que ça marche, no problem
"""

# Définition du menu 0
def menuPrincipal():
  global MENUACTIF
  print(
    """
    Bienvenu sur VISITORIA \n
    1. Enregistrer une visite \n
    2. Terminer une visite \n
    3. Voir les visites en cours \n
    """
  )
  choix = input("selectioneé une option: ")
  if choix == "1":
    MENUACTIF = 1

  elif choix =="2":
    MENUACTIF = 2

  elif choix =="3":
    MENUACTIF = 3

# Définition du menu 1
# supposont que le nom et prenoms sont uniques

def menuEnregistrerVisite():
  global MENUACTIF

  NomPrenom = input("Nom et prénoms: ")
  trouver = False
  for visiteur in LISTE_VISITEURS :
    if NomPrenom == visiteur["Nom et Prenoms"] :
      trouver = True
      visite = {}
      visite["Motif Visite"] = input("Motif Visite: ")
      visite["Heure entrée"] = datetime.now()
      id_visite = len(visiteur["Visites"])
      visiteur["Visites"][id_visite] = visite


  if trouver == False :
      visiteur = {
                  "Visites":{}
                  }
      visiteur["Nom et Prenoms"] = NomPrenom
      visiteur["Type de pièce"] = input("Type de pièce: ")
      visiteur["Num pièce"] = input("Num pièce: ")

      visite = {}
      visite["Motif Visite"] = input("Motif Visite: ")
      visite["Heure entrée"] = datetime.now()
      visite["Heure sortie"] = None
      id_visite = len(visiteur["Visites"])
      visite["id"] = id_visite

      visiteur["Visites"][id_visite] = visite

      LISTE_VISITEURS.append(visiteur)

  MENUACTIF = 0

# Définition du menu 2
def menuTerminerVisite():
  global MENUACTIF
  ID_visite = int(input("entreé ID de la visite: "))
  for visiteur in LISTE_VISITEURS :
    #print("ID_visite", ID_visite, type(ID_visite))
    #print("clés", list(visiteur["Visites"]))

    if visiteur["Visites"].get(ID_visite) :
      Terminer = input("taper 'q' pour terminer: ")
      while Terminer != 'q' :
        Terminer = input("taper 'q' pour terminer: ")
      visiteur["Visites"][ID_visite]["Heure sortie"] = datetime.now()
  MENUACTIF = 0

# Définition du menu 3 : voir les visites en cours
def menuVisiteEnCours():
  global MENUACTIF

  for visiteur in LISTE_VISITEURS :
    for visite in visiteur["Visites"].values():
      #print(visite)
      #print(visiteur)
      if visite["Heure sortie"] == None :
        print(f'{visiteur["Nom et Prenoms"]} {visite["id"]} {visite["Heure entrée"]}')

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

  # Terminer le programme
  if MENUACTIF == -1:
    break

print("\n\n\t Fin du programme !")
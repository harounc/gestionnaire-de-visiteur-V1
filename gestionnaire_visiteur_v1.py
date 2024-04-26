# Implémente les multi-visites

from datetime import datetime

"""
Gestionnaire de mots de passe
"""

cheminFichier = "donnees_visiteurs.txt"
separateur = "-@@@_/_/_/_@@@-"

def enregistrer():
    # Enregistrer un visiteur
    visite = {}
    visiteur = {
            "Visites":{}
            }
    Visiteur = visiteur["Nom et Prenoms"]
    Visite = visite["Motif Visite"]

    with open(cheminFichier, "a") as fp:
        fp.write(f"{Visiteur}{separateur}{Visite}\n")

def lister():
    # Lister les visiteurs
    with open(cheminFichier, "r") as fp:
        contenu = fp.read()
        # print("Contenu: ", type(contenu), contenu)
        listeVisiteurs = contenu.split("\n")
        # print("chaineCassee : ", listeUtilisateurs)

        for user in listeVisiteurs:
            if user != '':
                data = user.split(separateur)
                Visiteur = data[0]
                Visite = data[1]
                print(f"La liste des visiteurs : {Visiteur} {Visite}")



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

# Définition du menu 1
# supposont que le nom et prenoms sont uniques

def menuEnregistrerVisite():
  global MENUACTIF

  NomPrenom = input("Nom et prénoms: ")
  trouver = False
  for visiteur in LISTE_VISITEURS :
    if NomPrenom == visiteur["Nom et Prenoms"]:
      trouver = True
      visite = {}
      visite["Motif Visite"] = input("Motif Visite: ")
      visite["Heure entrée"] = datetime.now()
      visite["Heure sortie"] = None
      id_visite = len(visiteur["Visites"])
      visiteur["Visites"][id_visite] = visite

  if trouver == False:
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
  enregistrer()

  MENUACTIF = 0

# Définition du menu 2
def menuTerminerVisite():
  global MENUACTIF
  NomPrenom = (input("entrée le nom et prenoms du visiteur : "))
  ID_visite = int(input("entrée ID de la visite : "))
  for visiteur in LISTE_VISITEURS:
    #print("ID_visite", ID_visite, type(ID_visite))
    #print("clés", list(visiteur["Visites"]))

    if visiteur["Visites"].get(ID_visite) and visiteur["Nom et Prenoms"] == NomPrenom :
      Terminer = input("taper 'q' pour terminer: ")
      while Terminer != 'q':
        Terminer = input("taper 'q' pour terminer: ")
      visiteur["Visites"][ID_visite]["Heure sortie"] = datetime.now()
  lister()
  MENUACTIF = 0

# Définition du menu 3 : voir les visites en cours
def menuVisiteEnCours():
  global MENUACTIF

  for visiteur in LISTE_VISITEURS:
    for visite in visiteur["Visites"].values():
      print(visite)
      print(visiteur)
      if visite["Heure sortie"] == None:
        #print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visite["id"]} {visite["Heure entrée"]}')
        print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visiteur["Visites"]} {visite["Heure entrée"]}')

  MENUACTIF = 0

# Définition du menu 4 : voir les visites terminées
def menuVisiteTerminees():
  global MENUACTIF

  for visiteur in LISTE_VISITEURS:
    for visite in visiteur["Visites"].values():
      print(visite)
      print(visiteur)
      if visite["Heure sortie"] != None:
        #print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visite["id"]} {visite["Heure entrée"]}')
        print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visiteur["Visites"]} {visite["Heure entrée"]}')

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
  if MENUACTIF == -1:
    break

print("\n\n\t Fin du programme !")
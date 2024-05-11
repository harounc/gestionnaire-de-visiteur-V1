# TODO 
"""
1-Définir un chemin vers le fichier de sauvegarde :
    cheminFichier = "donnees_visiteurs.txt"
    separateurInterne = "-/_/_/_/-"
    separateurFin = "___@___"
  
2-Formuler un format d'enregistrement des visiteurs et leurs visites dans un fichier :
    Nom et Prenom 1-/_/_/_/-id visite1-/_/_/_/-Motif de la visite1-/_/_/_/-Heure Entrée1-/_/_/_/-Heure Sortie1___@___id visite2-/_/_/_/-Motif de la visite2-/_/_/_/-Heure Entrée2-/_/_/_/-Heure Sortie2___@___id visite3-/_/_/_/-Motif de la visite3-/_/_/_/-Heure Entrée3-/_/_/_/-Heure Sortie3
    Nom et Prenom 2-/_/_/_/-id visite1-/_/_/_/-Motif de la visite1-/_/_/_/-Heure Entrée1-/_/_/_/-Heure Sortie1___@___id visite2-/_/_/_/-Motif de la visite2-/_/_/_/-Heure Entrée2-/_/_/_/-Heure Sortie2___@___id visite3-/_/_/_/-Motif de la visite3-/_/_/_/-Heure Entrée3-/_/_/_/-Heure Sortie3

3-Faire des tests à part où: 
- tu inséres manuellement 2 visiteurs dans le fichier avec 3 visites chacun

    Exemple :
          {Visiteur 1}{separateurInterne}{Visite 1}{separateurFin}{Visite 2}{separateurFin}{Visite 3}
          {Visiteur 2}{separateurInterne}{Visite 1}{separateurFin}{Visite 2}{separateurFin}{Visite 3}

- et où tu arrives à charger ces 2 visiteurs et leurs visites dans un fichier python à part.

4-Applique la logique employée à notre programme
# Logique 1: tu peux charger les visiteurs du fichiers automatiquement au lancement du programme et à la fin du programme, les écrire dans le fichier.
# Logique 2: pour chaque opération (enregistrer, terminer, vites en cours), tu vas consulter le fichier 
# Logique n: tant que ça marche, no problem

"""


# Implémente les multi-visites

from datetime import datetime

"""
Gestionnaire de mots de passe
"""

cheminFichier = "donnees_visiteurs.txt"
sprtrI = " ___ "
sprtrFV = " @_V-V_@ "
sprtrVisiteVisiteur = " @_Vtr-Vte_@ "

def stocker(visiteurs: list):
    with open(cheminFichier, "w") as fp:  
        for visiteur in visiteurs:
            chaine = ""
            chaine += f"{visiteur["Nom et Prenoms"]}{sprtrI}{visiteur["Type de pièce"]}{sprtrI}{visiteur["Num pièce"]}{sprtrVisiteVisiteur}"
            for visite in visiteur["Visites"].values():
                #print(visite,visiteur["Visites"], type(visite))
                chaine += f"{visite["Motif Visite"]}{sprtrI}{visite["Heure entrée"]}{sprtrI}{visite["Heure sortie"]}{sprtrFV}"
            chaine += f"\n" 
            fp.write(chaine)

# Lister les visiteurs
def lister():
    visiteurs = []
    with open(cheminFichier, "r") as fp:
        contenu = fp.read()
        listeVisiteurs = contenu.split("\n")
        for user in listeVisiteurs:
            if user != '':
                visiteur = {}

                data = user.split(sprtrVisiteVisiteur)
                info_visiteur = data[0]
                infos = info_visiteur.split(sprtrI)
                nomprenom_visiteur = infos[0]
                typepiece_visiteur = infos[1]
                numeropiece_visiteur = infos[2]

                visiteur["Nom et Prenoms"] = nomprenom_visiteur
                visiteur["Type de pièce"] = typepiece_visiteur
                visiteur["Num pièce"] = numeropiece_visiteur

                visiteur["Visites"] = {}

                #print(f"Informations du visiteur : {nomprenom_visiteur} {typepiece_visiteur} {numeropiece_visiteur}")
                info_visite = data[1]
                liste_visite = info_visite.split(sprtrFV)
                id_visite = 0
                for visite in liste_visite:
                    if visite != '':
                        details_visite = visite.split(sprtrI)
                        motif_visite = details_visite[0]
                        heure_entree = details_visite[1]
                        heure_sortie = details_visite[2]
                        #print(f"\t\t{motif_visite} {heure_entree} {heure_sortie}")
                        # visiteur["Visites"]["Motif Visite"] = motif_visite
                        # visiteur["Visites"]["Heure entrée"] = heure_entree
                        # visiteur["Visites"]["Heure sortie"] = heure_sortie
                        visite_actuelle = {}
                        visite_actuelle["Motif Visite"] = motif_visite
                        visite_actuelle["Heure entrée"] = heure_entree
                        visite_actuelle["Heure sortie"] = heure_sortie
                        visiteur["Visites"][id_visite] = visite_actuelle
                        id_visite += 1
        visiteurs.append(visiteur)
    return visiteurs
   
# PROGRAMME PRINCIPAL
MENUACTIF = 0
LISTE_VISITEURS = lister()

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

  MENUACTIF = 0

# Définition du menu 3 : voir les visites en cours
def menuVisiteEnCours():
  global MENUACTIF

  for visiteur in LISTE_VISITEURS:
    for id_visite in visiteur["Visites"].keys():
      visite = visiteur["Visites"][id_visite]
      #print(visite)
      #print(visiteur)
      if visite["Heure sortie"] == None:
        #print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visite["id"]} {visite["Heure entrée"]}')
        print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {id_visite} {visite["Heure entrée"]}')

  MENUACTIF = 0

# Définition du menu 4 : voir les visites terminées
def menuVisiteTerminees():
  global MENUACTIF

  for visiteur in LISTE_VISITEURS:
    #print(visiteur)
    for id_visite in visiteur["Visites"].keys():
      visite = visiteur["Visites"][id_visite]
      if visite["Heure sortie"] != None:
        #print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {visite["id"]} {visite["Heure entrée"]}')
        print(f'{visiteur["Nom et Prenoms"]} {visite["Motif Visite"]} {id_visite} {visite["Heure entrée"]}')

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

stocker(LISTE_VISITEURS)
print("\n\n\t Fin du programme !")
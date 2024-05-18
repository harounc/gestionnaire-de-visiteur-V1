"""
Application de la logique 1

# Logique 1: tu peux charger les visiteurs du fichiers automatiquement au lancement du programme et à la fin du programme, les écrire dans le fichier.
"""


# Implémente les multi-visites

from datetime import datetime
import classes

"""
Gestionnaire de mots de passe
"""


"""
# Élabore la nouvelle structure de tes données pouvant prendre en compte cette nouveauté
VISITE = {
    "Motif Visite" : str,
    "Heure entrée" : str,
    "Heure sortie" : str
}

VISITEUR = {
    "Nom et Prenoms" : str,
    "Type de pièce" : str,
    "Num pièce" : int,
    "Visites" : dict[int,VISITE]
}

LISTE_VISITEURS = []

################# Exemple ################################"
VISITEUR = {
    "Nom et Prenoms" : "HAROUNA",
    "Type de pièce" : "CNI",
    "Num pièce" : 000012233,
    "Visites" : {
        1:{
          "Motif Visite" : sign contrat,
          "Heure entrée" : 10H,
          "Heure sortie" : 11H
        }
    }
}
"""

cheminFichier = "donnees_visiteurs.txt"
sprtrI = " ___ "
sprtrFV = " @_V-V_@ "
sprtrVisiteVisiteur = " @_Vtr-Vte_@ "

def stocker(visiteurs: list):
    with open(cheminFichier, "w") as fp:  
        for visiteur in classes.Visiteur.BDD:
            chaine = ""
            chaine += f"{visiteur.nom_complet}{sprtrI}{visiteur.type_piece}{sprtrI}{visiteur.num_piece}{sprtrVisiteVisiteur}"
            for visite in visiteur.mes_visites:
                #print(visite,visiteur["Visites"], type(visite))
                chaine += f"{visite.motif}{sprtrI}{visite.heure_entree}{sprtrI}{visite.heure_fin}{sprtrFV}"
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
                        print("details_visite ", details_visite)
                        motif_visite = details_visite[0]
                        heure_entree = details_visite[1]
                        heure_sortie = details_visite[2]
                        visite_actuelle = {}
                        visite_actuelle["Motif Visite"] = motif_visite
                        visite_actuelle["Heure entrée"] = heure_entree
                        visite_actuelle["Heure sortie"] = heure_sortie
                        visiteur["Visites"][id_visite] = visite_actuelle
                        id_visite += 1
        visiteurs.append(visiteur)
    return visiteurs
   
def injecter_donnees(liste_visiteurs: list) -> None:
   for visiteur in liste_visiteurs:
      nom_prenoms = visiteur["Nom et Prenoms"]
      type_piece = visiteur["Type de pièce"]
      num_piece = visiteur["Num pièce"]

      nom, prenoms = nom_prenoms.split(" ")
      objet_visiteur = classes.Visiteur(nom, prenoms, type_piece, num_piece)

      dict_visites = visiteur["Visites"]
      if len(dict_visites) != 0 :
        for visite in dict_visites.values():
          motif = visite["Motif Visite"]
          objet_visiteur.assignerVisite(motif)         

# PROGRAMME PRINCIPAL
MENUACTIF = 0
LISTE_VISITEURS = []

# Création de chaque visiteur et visite dans leur version avec classe.
injecter_donnees(lister())

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

  visiteur = classes.Visiteur.chercherVisiteur(nom, prenoms)
  if visiteur == None:
    type_piece = input("Type de pièce: ")
    num_piece = input("Numero de la piéce: ")
    visiteur = classes.Visiteur(nom, prenoms, type_piece, num_piece)

  motif_visite = input("Motif de la visite: ")
  visiteur.assignerVisite(motif_visite)

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

  visite_encours: list[classes.TypeVisite] = classes.Visite.listerVisitesEncours()
  for visite in visite_encours:
    print(f'{visite.visiteur.nom_complet} {visite.motif} {visite.id} {visite.heure_entree}')

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
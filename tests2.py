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

cheminFichier = "donneesV.txt"
sprtrI = "-/_/_/_/-"
sprtrFV = "___@@@___"
sprtrVisiteVisiteur = "_\_"
def stocker(a: str, visites: list):
    with open(cheminFichier, "a") as fp:
        chaine = ""
        chaine += f"{a} {sprtrVisiteVisiteur}"
        for visite in visites:
            chaine += f"{visite["Motif Visite"]}{sprtrI}{visite["Heure entrée"]}{sprtrI}{visite["Heure sortie"]}{sprtrFV}"
        fp.write(chaine) 


        #fp.write(f"{a}{separateurInterne}{b}{separateurInterne}{c}{separateurInterne}{d}\n")

data_visites = [
    {
        "Motif Visite" : "facture",
        "Heure entrée" : "10H30",
        "Heure sortie" : "11H00"
    },
    {
        "Motif Visite" : "STC",
        "Heure entrée" : "14H00",
        "Heure sortie" : "15H30" 
    }
]

#stocker("coulibaly harouna", data_visites)

def lister():
    # Lister les visiteurs
    with open(cheminFichier, "r") as fp:
        contenu = fp.read()
        # print("Contenu: ", type(contenu), contenu)
        listeVisiteurs = contenu.split("\n")
        # print("chaineCassee : ", listeUtilisateurs)
        for user in listeVisiteurs:
            if user != '':
                data = user.split(sprtrVisiteVisiteur)
                nom_prenomVisisteur = data[0]
                infoVisites = data[1]
                print("Nom et prenoms visiteur : ", nom_prenomVisisteur)

                listeVisites = infoVisites.split(sprtrFV)
                for visite in listeVisites:
                    if visite != '':
                        detailsVisite = visite.split(sprtrI)
                        motifVisite = detailsVisite[0]
                        heureEntree = detailsVisite[1]
                        heureSortie = detailsVisite[2]
                        print(f"\t\t{motifVisite} {heureEntree} {heureSortie}")
        
#lister()






# Implémente les multi-visites

from datetime import datetime

cheminFichier = "donnees_visiteurs.txt"
separateur = "-@@@///@@@-"

def stocker(a: str,b: str):
    # Enregistrer un visiteur
    # visite = {}
    # visiteur = {
    #         "Visites":{}
    #         }
    # visiteur["Nom et Prenoms"] = a
    # visite["Motif Visite"] = b

    with open(cheminFichier, "a") as fp:
        fp.write(f"{a}{separateur}{b}\n")

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
                a = data[0]
                b = data[1]
                print(f"La liste des visiteurs : {a} {b}")

# stocker("Mariam", "Salutations du DG")
# stocker("Mariam", "Visite de courtoisie")
# stocker("Jean", "Signature de contrat")

lister()
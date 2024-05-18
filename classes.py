from datetime import datetime
from typing import Optional, TypeVar, Union

TypeVisite = TypeVar("TypeVisite", bound="Visite")
TypeVisiteur = TypeVar("TypeVisiteur", bound="Visiteur")

# Règle 1: Aucun 'print' dans les méthodes
# Règle 2: Aucun 'input' dans les méthodes


cheminFichier = "donnees_visiteurs.txt"
sprtrI = " ___ "
sprtrFV = " @_V-V_@ "
sprtrVisiteVisiteur = " @_Vtr-Vte_@ "


"""
TODO: 
- Terminer les méthodes 
- Les insérer dans l'algo principal
"""

"""
Opération sur les visites
- création
- terminer
- liste les visites (en cours & terminées)

"""
class Visite:
  # BDD: list[TypeVisite] = []

  def __init__(self, motif: str, visiteur: TypeVisiteur, id = None):
    self.motif = motif
    self.heure_entree = datetime.now()
    self.heure_fin = None

    self.visiteur = visiteur
    self.id = int(id) if type(id) == str else id
    # self.signaler(self)

  @classmethod
  def signaler(cls, visite: TypeVisite):
    """
    Ajouter la visite fraichement créé à la liste des visites
    """
    # cls.BDD.append(visite)
    visite.id = len(cls.BDD)

  @classmethod
  def chercherVisites(cls, id_visite: int)  -> None:
    # TODO: À terminer
    """
    Rechercher une visite grace à son ID et la retourner
    """
    for visite in cls.BDD:
      if visite.id == id_visite:
        return visite
 
  @classmethod
  def terminerVisite(cls, id_visite: int, indexLigne: int)  -> None:
    # TODO: À terminer
    """
    Recuperer la visite retournée par la methode chercherVisites et la terminer
    """
    if indexLigne == -1:
       raise Exception("Impossible !")

    allLignes = []
    with open(cheminFichier, "r") as fp:
      allLignes = fp.readlines()

      user = allLignes[indexLigne]

      data = user.split(sprtrVisiteVisiteur)

      info_visiteurs = data[0]
      info_visite = data[1]
      liste_visite = info_visite.split(sprtrFV)

      chaine_reconstituee = f"{info_visiteurs}{sprtrVisiteVisiteur}"

      for visite in liste_visite:
          if visite != '':
              details_visite = visite.split(sprtrI)
              id_visite_str = details_visite[0]
              motif_visite = details_visite[1]
              heure_entree = details_visite[2]
              heure_sortie = details_visite[3]

              if int(id_visite_str) == id_visite:
                chaine_reconstituee += f"{id_visite}{sprtrI}{motif_visite}{sprtrI}{heure_entree}{sprtrI}{datetime.now()}{sprtrFV}"
              else:
                chaine_reconstituee += f"{f'{sprtrI}'.join(details_visite)}{sprtrFV}"

      allLignes[indexLigne] = chaine_reconstituee

    with open(cheminFichier, "w") as fp:
      fp.write("".join(allLignes))


    
  @classmethod
  def listerVisitesEncours(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites non terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesEncours: list[TypeVisite] = []

    with open(cheminFichier, "r") as fp:
        contenu = fp.read()
        listeVisiteurs = contenu.split("\n")
        for user in listeVisiteurs:
            if user != '':
                data = user.split(sprtrVisiteVisiteur)
                info_visiteur = data[0]
                infos = info_visiteur.split(sprtrI)
                nomprenom_visiteur = infos[0]
                typepiece_visiteur = infos[1]
                numeropiece_visiteur = infos[2]
                
                nom_visiteur, prenoms_visiteur = nomprenom_visiteur.split(" ")
                objet_visiteur = Visiteur(nom_visiteur, prenoms_visiteur, typepiece_visiteur, numeropiece_visiteur)

                #print(f"Informations du visiteur : {nomprenom_visiteur} {typepiece_visiteur} {numeropiece_visiteur}")
                info_visite = data[1]
                liste_visite = info_visite.split(sprtrFV)
                for visite in liste_visite:
                    if visite != '':
                        details_visite = visite.split(sprtrI)
                        id_visite = details_visite[0]
                        motif_visite = details_visite[1]
                        heure_entree = details_visite[2]
                        heure_sortie = details_visite[3]
                        if heure_sortie == 'None':
                          objet_visite = Visite(motif_visite, objet_visiteur, id = id_visite)
                          listeVisitesEncours.append(objet_visite)

    return listeVisitesEncours


  @classmethod
  def listerVisitesTerminees(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesTerminees: list[TypeVisite] = []
    with open(cheminFichier, "r") as fp:
        contenu = fp.read()
        listeVisiteurs = contenu.split("\n")
        for user in listeVisiteurs:
            if user != '':
                data = user.split(sprtrVisiteVisiteur)
                info_visiteur = data[0]
                infos = info_visiteur.split(sprtrI)
                nomprenom_visiteur = infos[0]
                typepiece_visiteur = infos[1]
                numeropiece_visiteur = infos[2]
                
                nom_visiteur, prenoms_visiteur = nomprenom_visiteur.split(" ")
                objet_visiteur = Visiteur(nom_visiteur, prenoms_visiteur, typepiece_visiteur, numeropiece_visiteur)

                #print(f"Informations du visiteur : {nomprenom_visiteur} {typepiece_visiteur} {numeropiece_visiteur}")
                info_visite = data[1]
                liste_visite = info_visite.split(sprtrFV)
                for visite in liste_visite:
                    if visite != '':
                        details_visite = visite.split(sprtrI)
                        id_visite = details_visite[0]
                        motif_visite = details_visite[1]
                        heure_entree = details_visite[2]
                        heure_sortie = details_visite[3]
                        if heure_sortie != 'None':
                          objet_visite = Visite(motif_visite, objet_visiteur, id = id_visite)
                          listeVisitesTerminees.append(objet_visite)

    return listeVisitesTerminees


"""
Opérations sur les visiteurs
- création
- assignation d'une visite
- ajouter à la liste des visiteurs
- retrouver un visiteur
"""
class Visiteur:
  # BDD: list[TypeVisiteur] = []

  def __init__(self, nom: str, prenoms: str, type_piece: str, num_piece: str):
    self.nom = nom
    self.prenoms = prenoms
    self.type_piece = type_piece
    self.num_piece = num_piece

    self.id = None
    self.mes_visites = []

  @property
  def nom_complet(self):
    return self.nom + " " + self.prenoms

  def assignerVisite(self, motif: str, indexLigne: int) -> None:
    """
    Crée une nouvelle visite et l'assigne au visiteur 

    Ex: 
        v1 = Visiteur()
        v1.assignerVisite("Salut tation")

    """
    allLignes = []
    with open(cheminFichier, "r") as fp:
      allLignes = fp.readlines()

    with open(cheminFichier, "w") as fp:
      if indexLigne == -1:
        chaine = f"{self.nom_complet}{sprtrI}{self.type_piece}{sprtrI}{self.num_piece}{sprtrVisiteVisiteur}"
        visite = Visite(motif, self)
        chaine += f"0{sprtrI}{visite.motif}{sprtrI}{visite.heure_entree}{sprtrI}{visite.heure_fin}{sprtrFV}"
        allLignes.append(chaine)
      else:
        chaine = allLignes[indexLigne] # Copier toute la ligne dans chaine
        visite = Visite(motif, self)

        data = chaine.split(sprtrVisiteVisiteur)
        info_visiteur = data[0]
        infos = info_visiteur.split(sprtrI)
        info_visite = data[1]
        liste_visite = info_visite.split(sprtrFV)

        id_visite = len([v for v in liste_visite if v != ''])
        
        chaine += f"{id_visite}{sprtrI}{visite.motif}{sprtrI}{visite.heure_entree}{sprtrI}{visite.heure_fin}{sprtrFV}"
        allLignes[indexLigne] = chaine
      
      fp.write("\n".join([ line.replace("\n", "") for line in allLignes ]))

  @classmethod
  def chercherVisiteur(cls, nom: str, prenoms: str) -> Optional[list[TypeVisiteur]]:
    # TODO: À terminer
    with open(cheminFichier, "r") as fp:
      contenu = fp.read()
      listeVisiteurs = contenu.split("\n")
      indexLigne = -1
      for user in listeVisiteurs:
        indexLigne += 1
        if user != '':
          visiteur = {}

          data = user.split(sprtrVisiteVisiteur)
          info_visiteur = data[0]
          infos = info_visiteur.split(sprtrI)
          nomprenom_visiteur = infos[0]
          nom_visiteur, prenoms_visiteur = nomprenom_visiteur.split(" ")
          typepiece_visiteur = infos[1]
          numeropiece_visiteur = infos[2]

          if nom_visiteur == nom and prenoms_visiteur == prenoms:
            objet_visiteur = cls(nom, prenoms, typepiece_visiteur, numeropiece_visiteur)

            info_visite = data[1]
            liste_visite = info_visite.split(sprtrFV)
            for visite in liste_visite:
                if visite != '':
                    details_visite = visite.split(sprtrI)
                    id_visite = details_visite[0]
                    motif_visite = details_visite[1]
                    heure_entree = details_visite[2]
                    heure_sortie = details_visite[3]
                    
                    v = Visite(motif_visite, objet_visiteur, id = id_visite)
                    objet_visiteur.mes_visites.append(v)

            return objet_visiteur, indexLigne


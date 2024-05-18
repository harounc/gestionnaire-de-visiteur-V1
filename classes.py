from datetime import datetime
from typing import Optional, TypeVar

TypeVisite = TypeVar("TypeVisite", bound="Visite")
TypeVisiteur = TypeVar("TypeVisiteur", bound="Visiteur")

# Règle 1: Aucun 'print' dans les méthodes
# Règle 2: Aucun 'input' dans les méthodes

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
  BDD: list[TypeVisite] = []

  def __init__(self, motif: str, visiteur: TypeVisiteur):
    self.motif = motif
    self.heure_entree = datetime.now()
    self.heure_fin = None

    self.visiteur = visiteur
    self.id = None
    self.signaler(self)

  @classmethod
  def signaler(cls, visite: TypeVisite):
    """
    Ajouter la visite fraichement créé à la liste des visites
    """
    cls.BDD.append(visite)
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
  def terminerVisites(cls, visite: TypeVisite)  -> None:
    # TODO: À terminer
    """
    Recuperer la visite retournée par la methode chercherVisites et la terminer
    """
    visite.heure_fin = datetime.now()

  @classmethod
  def listerVisitesEncours(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites non terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesEncours: list[TypeVisite] = []
    for visite in cls.BDD:
      if visite.heure_fin == None:
          listeVisitesEncours.append(visite)
    return listeVisitesEncours


  @classmethod
  def listerVisitesTerminees(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesTerminees: list[TypeVisite] = []
    for visite in cls.BDD:
      if visite.heure_fin != None:
        listeVisitesTerminees.append(visite)
    return listeVisitesTerminees


"""
Opérations sur les visiteurs
- création
- assignation d'une visite
- ajouter à la liste des visiteurs
- retrouver un visiteur
"""
class Visiteur:
  BDD: list[TypeVisiteur] = []

  def __init__(self, nom: str, prenoms: str, type_piece: str, num_piece: str):
    self.nom = nom
    self.prenoms = prenoms
    self.type_piece = type_piece
    self.num_piece = num_piece

    # Il est considéré sans aucune visite au début
    self.mes_visites = []

    # Ajout à la DB
    self.id = None
    self.signaler(self) # <=> Visiteur.BDD.append(visiteur)

  @property
  def nom_complet(self):
    return self.nom + " " + self.prenoms

  @classmethod
  def signaler(cls, visiteur: TypeVisiteur):
    """
    Ajouter le visiteur fraichement créé à la liste des visiteurs
    """
    cls.BDD.append(visiteur)
    visiteur.id = len(cls.BDD)

  def assignerVisite(self, motif: str) -> None:
    """
    Crée une nouvelle visite et l'assigne au visiteur 

    Ex: 
        v1 = Visiteur()
        v1.assignerVisite("Salut tation")

    """
    v = Visite(motif,self)
    self.mes_visites.append(v)

  @classmethod
  def chercherVisiteur(cls, nom: str, prenoms: str) -> Optional[TypeVisiteur]:
    # TODO: À terminer
    for visiteur in cls.BDD:
      if visiteur.nom == nom and visiteur.prenoms == prenoms:
        return visiteur





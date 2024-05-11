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
  BDD = []

  def __init__(self, motif: str):
    self.motif = motif
    self.heure_entree = datetime.now()
    self.heure_fin = None

    self.id = None
    self.signaler(self)

  @classmethod
  def signaler(cls, visite):
    """
    Ajouter la visite fraichement créé à la liste des visites
    """
    cls.BDD.append(visite)
    visite.id = len(cls.BDD)

  def terminer(self)  -> None:
    pass
    # TODO: À terminer

  @classmethod
  def listerVisitesEncours(cls) -> list[TypeVisite]:
    pass
    # TODO: À terminer

  @classmethod
  def listerVisitesTerminees(cls) -> list[TypeVisite]:
      pass
    # TODO: À terminer


"""
Opérations sur les visiteurs
- création
- assignation d'une visite
- ajouter à la liste des visiteurs
- retrouver un visiteur
"""
class Visiteur:
  BDD = []

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

  @classmethod
  def signaler(cls, visiteur):
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
    id_visite = len(self.mes_visites)
    v = Visite(motif, id_visite)
    self.mes_visites.append(v)

  @classmethod
  def retrouver(self) -> Optional[TypeVisiteur]:
    pass
    # TODO: À terminer




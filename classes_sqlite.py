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
import sqlite3

DB_NAME = "gest_visit.sqlite3"
# se connecter à la base de donnéés
conn = sqlite3.connect(DB_NAME)

# créer un curseur pour communiquer avec la base de donnée
curseur = conn.cursor()

#créer une table dans la base de données

curseur.execute("""
    CREATE TABLE IF NOT EXISTS Visiteurs (
        id_visiteur INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_visiteur TEXT,
        prenoms_visiteur TEXT,
        type_piece TEXT,
        numero_piece TEXT
    )
""")

curseur.execute("""
    CREATE TABLE IF NOT EXISTS Visites (
        id_visite INTEGER PRIMARY KEY AUTOINCREMENT,
        motif_visite TEXT,
        heure_entree TEXT,
        heure_fin TEXT,
        id_visiteur INTEGER,
        FOREIGN KEY (id_visiteur) REFERENCES Visiteurs(id_visiteur)
    )
""")

class Visite:
  # BDD: list[TypeVisite] = []

  def __init__(self, motif: str, visiteur: TypeVisiteur, id: Optional[int] = None, heure_entree: Optional[str] = None):
    self.motif = motif
    self.heure_entree = heure_entree or datetime.now()
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
  def terminerVisite(cls, id_visite: int, indexLigne: Optional[int] = None)  -> None:
    # TODO: À terminer
    """
    Recuperer la visite retournée par la methode chercherVisites et la terminer
    """
    heure_fin = datetime.now()
    requeteUpdate = f"UPDATE Visites set heure_fin = '{heure_fin}' WHERE id_visite = {id_visite} "
    curseur.execute(requeteUpdate)
    conn.commit()
    
  @classmethod
  def listerVisitesEncours(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites non terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesEncours: list[TypeVisite] = []

    requeteSQL = "SELECT * FROM Visites WHERE heure_fin IS NULL"
    listeVisites = curseur.execute(requeteSQL).fetchall()
    if listeVisites:
       for db_visite in listeVisites:
          id_visiteur = db_visite[4]
        
          # On récupère ensuite les informations du visiteur associé pour construire un objet Visteur
          requeteVisteur = f"SELECT * FROM Visiteurs WHERE id_visiteur = {id_visiteur}"
          resultatVisiteur = curseur.execute(requeteVisteur).fetchone()
          nom_visiteur = resultatVisiteur[1]
          prenoms_visiteur = resultatVisiteur[2]
          typepiece_visiteur = resultatVisiteur[3]
          numeropiece_visiteur = resultatVisiteur[4]

          objet_visiteur = Visiteur(nom_visiteur, prenoms_visiteur, typepiece_visiteur, numeropiece_visiteur)


          # Grace à ce objet visiteur, on va ensuite reconstituer un objet Visite (dont le constructeur a besoin du Visiteur) 
          id_visite = db_visite[0]
          motif_visite = db_visite[1]
          heure_entree = db_visite[2]
          heure_sortie = db_visite[3]
          objet_visite = Visite(motif_visite, objet_visiteur, id = id_visite, heure_entree = heure_entree)
          listeVisitesEncours.append(objet_visite)

    return listeVisitesEncours


  def listerVisitesEncoursPourUnVisiteur(cls, id_visiteur) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites non terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesEncours: list[TypeVisite] = []

    requeteSQL = "SELECT * FROM Visites WHERE heure_fin IS NULL AND id_visiteur = {id_visiteur}"
    listeVisites = curseur.execute(requeteSQL).fetchall()
    if listeVisites:
       for db_visite in listeVisites:
          id_visiteur = db_visite[4]
        
          # On récupère ensuite les informations du visiteur associé pour construire un objet Visteur
          requeteVisteur = f"SELECT * FROM Visiteurs WHERE id_visiteur = {id_visiteur}"
          resultatVisiteur = curseur.execute(requeteVisteur).fetchone()
          nom_visiteur = resultatVisiteur[1]
          prenoms_visiteur = resultatVisiteur[2]
          typepiece_visiteur = resultatVisiteur[3]
          numeropiece_visiteur = resultatVisiteur[4]

          objet_visiteur = Visiteur(nom_visiteur, prenoms_visiteur, typepiece_visiteur, numeropiece_visiteur)


          # Grace à ce objet visiteur, on va ensuite reconstituer un objet Visite (dont le constructeur a besoin du Visiteur) 
          id_visite = db_visite[0]
          motif_visite = db_visite[1]
          heure_entree = db_visite[2]
          heure_sortie = db_visite[3]
          objet_visite = Visite(motif_visite, objet_visiteur, id = id_visite, heure_entree = heure_entree)
          listeVisitesEncours.append(objet_visite)

    return listeVisitesEncours

  @classmethod
  def listerVisitesTerminees(cls) -> list[TypeVisite]:
    # TODO: À terminer
    """
    Recupère toutes les visites terminées, les stockent dans une variable avant de les retourner tous
    """
    listeVisitesTerminees: list[TypeVisite] = []

    requeteSQL = "SELECT * FROM Visites WHERE heure_fin IS NOT NULL"
    listeVisites = curseur.execute(requeteSQL).fetchall()
    if listeVisites:
       for db_visite in listeVisites:
          id_visiteur = db_visite[4]
        
          # On récupère ensuite les informations du visiteur associé pour construire un objet Visteur
          requeteVisteur = f"SELECT * FROM Visiteurs WHERE id_visiteur = {id_visiteur}"
          resultatVisiteur = curseur.execute(requeteVisteur).fetchone()
          nom_visiteur = resultatVisiteur[1]
          prenoms_visiteur = resultatVisiteur[2]
          typepiece_visiteur = resultatVisiteur[3]
          numeropiece_visiteur = resultatVisiteur[4]

          objet_visiteur = Visiteur(nom_visiteur, prenoms_visiteur, typepiece_visiteur, numeropiece_visiteur)


          # Grace à ce objet visiteur, on va ensuite reconstituer un objet Visite (dont le constructeur a besoin du Visiteur) 
          id_visite = db_visite[0]
          motif_visite = db_visite[1]
          heure_entree = db_visite[2]
          heure_sortie = db_visite[3]
          objet_visite = Visite(motif_visite, objet_visiteur, id = id_visite, heure_entree = heure_entree)
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

  def assignerVisite(self, motif: str, id_visiteur: int) -> None:
    """
    Crée une nouvelle visite et l'assigne au visiteur 

    Ex: 
        v1 = Visiteur()
        v1.assignerVisite("Salut tation")

    """
    # allLignes = []
    # with open(cheminFichier, "r") as fp:
    #   allLignes = fp.readlines()


    heure_entree = datetime.now()
    if id_visiteur == -1:
      visite = Visite(motif, self)
      requeteVisiteur = f"insert into Visiteurs \
        (nom_visiteur, prenoms_visiteur, type_piece, numero_piece) \
          VALUES ('{self.nom}', '{self.prenoms}', '{self.type_piece}', '{self.num_piece}') ;\
      "
      resVisiteur = curseur.execute(requeteVisiteur)
      id_visiteur_cree = resVisiteur.lastrowid

      requeteSQL = f"insert into Visites (motif_visite, heure_entree, heure_fin, id_visiteur) VALUES ('{motif}', '{heure_entree}', NULL, {id_visiteur_cree}) ;"
      curseur.execute(requeteSQL)
    else:
      # chaine = allLignes[indexLigne] # Copier toute la ligne dans chaine
      visite = Visite(motif, self)
      requeteSQL = f"insert into Visites (motif_visite, heure_entree, heure_fin, id_visiteur) VALUES ('{motif}', '{heure_entree}', NULL, {id_visiteur}) ;"
      curseur.execute(requeteSQL)

    conn.commit()

  @classmethod
  def chercherVisiteur(cls, nom: str, prenoms: str) -> Optional[list[TypeVisiteur]]:
    requeteSQL = f"SELECT * from Visiteurs WHERE nom_visiteur = '{nom}' AND prenoms_visiteur = '{prenoms}' ;"

    resultat = curseur.execute(requeteSQL).fetchone()
    # Le résultat est soit nul soit une liste de 5 éléments

    if resultat:
      id_visiteur =  resultat[0]
      typepiece_visiteur = resultat[3]
      numeropiece_visiteur = resultat[4]

      objet_visiteur = cls(nom, prenoms, typepiece_visiteur, numeropiece_visiteur)

      
      # Chargement des visites associées

      requeteSQL = f"SELECT * from Visites WHERE id_visiteur = {id_visiteur} ;"
      listeVisites = curseur.execute(requeteSQL).fetchall()
      if listeVisites:
        for db_visite in listeVisites:
          id_visite = db_visite[0]
          motif_visite = db_visite[1]
          heure_entree = db_visite[2]
          heure_sortie = db_visite[3]

          v = Visite(motif_visite, objet_visiteur, id = id_visite)
          objet_visiteur.mes_visites.append(v)
      
      return objet_visiteur, id_visiteur

    return None    



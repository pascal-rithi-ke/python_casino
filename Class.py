import bcrypt

class User:
  def __init__(self, prenom, nom, id, password):
    self.prenom = prenom
    self.nom = nom
    self.id = id
    self.password = password

class Partie:
  def __init__(self, idPartie, idUser, nomUser, prenomUser):
    self.id = idPartie
    self.idUser = idUser
    self.nomUser = nomUser
    self.prenomUser = prenomUser
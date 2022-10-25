class User:
  def __init__(self, prenom, nom, id, username ,password, nbcoup):
    self.prenom = prenom
    self.username = username
    self.nom = nom
    self.id = id
    self.password = password
    self.nbcoup = nbcoup

class Partie:
  def __init__(self, idPartie, idUser, nomUser, prenomUser, username, User_nbcoup):
    self.id = idPartie
    self.idUser = idUser
    self.nomUser = nomUser
    self.prenomUser = prenomUser
    self.username = username
    self.User_nbcoup = User_nbcoup
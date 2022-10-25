import random, string
from FolderClass.Class import User,Partie
from db import userCollection, partieCollection

#Genere un id aléatoire
def generateId(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def askUserInfoForRegister():
    while True:
        try:
            id = generateId(8)
            prenom = str(input("Quelle est votre prénom \n\n"))
            nom = str(input("Quelle est votre nom \n\n"))
            print(f"Bienvenue {prenom} {nom} \n\n")
            username = str(input("Veuillez choisir un nom d'utilisateur \n\n"))
            password = str(input("Définissez votre mot de passe \n\n"))
            return User(prenom, nom, id,username, password, [str(1)])
        except:
            return 'Vous devez rentrer vos information sous forme de chaine de caractère \n\n'

def askUserInfoForLogin():
    while True:
        try:
            username = str(input("Veuillez saisir votre nom d'utilisateur \n\n"))
            password = str(input("Saisissez votre mot de passe \n\n"))
            return Login(username, password)
        except:
            return 'User not found'

def Register(user: User):
    try:
        ObjUser = {"id":user.id,"prenom":user.prenom,"username": user.username, "nom":user.nom,"password":user.password, "levels" : user.nbcoup}
        userCollection.insert_one(ObjUser) 
        return 'ok'
    except:
        return 'user not created'

def Login(username, password):
    ObjLogin = {'username': username, 'password': password}
    try:
        user = userCollection.find_one(ObjLogin)
        return user
    except:
        return 'user not found'

def InitPartie(user: User):
    idPartie = generateId(16)
    partie = Partie(idPartie,user.id,user.nom,user.prenom)
    ObjPartie = {"idPartie":partie.id,"idUser":user.id,"nom":user.nom,"prenom":user.prenom}
    try:
        partieCollection.insert_one(ObjPartie)
        return 'ok'
    except:
        return 'partie not created'

def UpdateUserLevels(levels: list, idUser: str):
    filter = {'id': idUser}
    newValues = {"$set" : {'levels': levels}}
    return userCollection.update_one(filter, newValues)
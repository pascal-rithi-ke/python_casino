import random, string
from Class import User,Partie
from FunctionFile import generateId
from db import userCollection, partieCollection

#Genere un id aléatoire
def generateId(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def Register(user: User):
    try:
        ObjUser = {"id":user.id,"prenom":user.prenom,"nom":user.nom,"password":user.password}
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
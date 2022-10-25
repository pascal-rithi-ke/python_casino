import os, pymongo

from dotenv import load_dotenv
from FolderClass.Class import User,Partie
#from FolderFunction.Function import generateId

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.lfi8yfs.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(DATABASE_URL)

tableBdd = client["casino_project"]
userCollection = tableBdd["users"]
partieCollection = tableBdd["partie"]
# print(client.list_database_names())

'''saisieUser = input("Bonjour Voulez vous jouer ? O/N\n")
while saisieUser != "O" or saisieUser != "N":
    if saisieUser != "O" or saisieUser != "N":
        saisieUser = input("Veuillez choisir entre O/N\n")
    if saisieUser == "O":
        # ajouter un user dans la bdd
        id = generateId(16)
        nbcoup = 10
        prenom = input("Quel est votre prénom ?\n")
        nom = input("Quel est votre nom ?\n")
        username = input("Quel est votre username ?\n")
        password = input("Quelle est votre mot de passe\n")

        user = User(prenom,nom,id,password, username,nbcoup)
        ObjUser = {"id":user.id,"prenom":user.prenom,"nom":user.nom, "username": user.username ,"password":password, "nbcoup": user.nbcoup}
        addUser = userCollection.insert_one(ObjUser) 

        # insère le joueur dans la collection partie
        idPartie = generateId(16)
        partie = Partie(idPartie,id,nom,prenom, username ,nbcoup)
        ObjPartie = {"idPartie":idPartie,"idUser":user.id,"nomUser":user.nom,"prenomUser":user.prenom, "Username":username, "User_nbcoup":user.nbcoup}
        addPartie = partieCollection.insert_one(ObjPartie)
        break
    if saisieUser == "N":
        print("Aurevoir")
        break'''
    
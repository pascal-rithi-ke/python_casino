import os, pymongo

from dotenv import load_dotenv
from Class import User,Partie
from FunctionFile import generateId

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.lfi8yfs.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(DATABASE_URL)

tableBdd = client["casino_project"]
userCollection = tableBdd["users"]
partieCollection = tableBdd["partie"]
# print(client.list_database_names())

saisieUser = input("Bonjour Voulez vous jouer ? O/N\n")
while saisieUser != "O" or saisieUser != "N":
    saisieUser = input("Veuillez choisir entre O/N\n")
    if saisieUser == "O":
        # ajouter un user dans la bdd
        id = generateId(16)
        prenom = input("Quel est votre prénom ?\n")
        nom = input("Quel est votre nom ?\n")
        password = input("Quelle est votre mot de passe\n")
        user = User(prenom,nom,id,password)
        ObjUser = {"id":user.id,"prenom":user.prenom,"nom":user.nom,"password":password}
        addUser = userCollection.insert_one(ObjUser) 

        # insère le joueur dans la collection partie
        idPartie = generateId(16)
        partie = Partie(idPartie,id,nom,prenom)
        ObjPartie = {"idPartie":idPartie,"idUser":user.id,"nom":user.nom,"prenom":user.prenom}
        addPartie = partieCollection.insert_one(ObjPartie)
        break
    elif saisieUser == "N":
        print("Aurevoir")
        break
    
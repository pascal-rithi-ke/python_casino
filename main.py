# 1è façon avec True
from random import randrange
from Class import User,Partie
from FunctionFile import generateId
#from database.db import casino_db, generateId


#users = casino_db.get_collection('users')
#users.insert_one({'username': 'testRegister', 'password': 'testRegister', 'id': generateId(9)})
#for user in users.find():
#    print(user)

authenticated = False

#game loop  
while True :
    nb_coup = 0
    level = 0
    # login or register
    while True:
        try:
            login_or_register = int(input('Taper 1 pour vous connecter 0 pour vous enregistrer \n\n'))
            if(login_or_register == 0 or login_or_register == 1):
                break
            else:
                print('Erreur vous devez choisir 1 pour vous connecter ou 0 pour vous enregistrer')
        except:
            print('Erreur')

    if(login_or_register == 1):
        levels = [str(1)]
    else:
        levels = [str(1), str(2)]

    authenticated = True
    # choix du niveau
    while True:
        try:
            user_avaible_levels_string = ' | '.join(levels)
            selected_level = int(input(f'Sélectionner un niveau parmis eux: ' + str(user_avaible_levels_string) + '\n\n'))
            if(str(selected_level) in levels):
                break
            else:
                print('Erreur vous avez sélectionné un niveau que vous n\'avez pas débloquer ou inexistant \n\n Sélectionner parmis les niveaux :' + user_avaible_levels_string)
        except:
            print('Erreur')

    # initialisation des règles
    if(selected_level == 1):
        nb_ordi = randrange(1, 10, 1)
        nb_legit_coup = 3
    elif(selected_level == 2):
        nb_ordi = randrange(1, 20, 1)
        nb_legit_coup = 5
    elif(selected_level == 3):
        nb_ordi = randrange (1, 30, 1)
        nb_legit_coup = 7
    print('Mon choix est = ', nb_ordi)
    
    # début du jeu
    while nb_coup <= nb_legit_coup:
        while True:
            try:
                nb_user = int(input ("Entrez SVP votre nombre ? \n\n"))
                break
            except:
                print('Erreur')
        nb_coup += 1
        if(nb_coup < nb_legit_coup):
            if nb_user > nb_ordi :
                print ('Votre nbre est trop grand')
            elif nb_user < nb_ordi :
                print ('Votre nbre est trop petit')
            else :
                print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                break
        else:
            print('vous avez perdu')
    continue_casino = ''
    while True:
        try:
            continue_casino = int(input("Voulez vous continuer ? 1 pour continuer 0 pour quitter \n\n"))
            if(continue_casino == 0 or continue_casino == 1):
                break
        except:
            print('Erreur vous devez choisir en entre 1 et 0 pour continuer ou quitter le jeu \n\n')
    if(continue_casino == 0):
        break

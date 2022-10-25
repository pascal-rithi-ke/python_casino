# 1è façon avec True
from random import randrange

nb_coup = 0
level = 0

#game loop  
while True :
    # login or register
    while True:
        try:
            login_or_register = int(input('Taper 1 pour vous connecter 0 pour vous enregistrer'))
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

    # choix du niveau
    while True:
        try:
            user_avaible_levels_string = ' | '.join(levels)
            selected_level = int(input(f'Sélectionner un niveau parmis eux: ' + str(user_avaible_levels_string)))
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
    while nb_coup != nb_legit_coup:
        while True:
            try:
                nb_user = int(input ("Entrez SVP votre nombre ? "))
                break
            except:
                print('Erreur')
        nb_coup += 1
        if(nb_coup < nb_ordi):
            if nb_user > nb_ordi :
                print ('Votre nbre est trop grand')
            elif nb_user < nb_ordi :
                print ('Votre nbre est trop petit')
            else :
                print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
                break
        else:
            print('vous avez perdu')

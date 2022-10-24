from random import randrange
nb_ordi = randrange (1, 11, 1)
print('Mon choix est = ', nb_ordi)
nb_coup = 0
while True :
    while True:
        try:
            nb_user = int(input ("Entrez SVP votre nombre ? "))
            break
        except:
            print('Choisissez un NOMBRE')
    nb_coup += 1
    if nb_user > nb_ordi :
        print ('Votre nbre est trop grand')
    elif nb_user < nb_ordi :
        print ('Votre nbre est trop petit')
    else :
        print ("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))
        break
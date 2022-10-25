import random, string

#Genere un id aléatoire
def generateId(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
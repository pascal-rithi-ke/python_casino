import os
import pymongo
import random, string
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.lfi8yfs.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(DATABASE_URL)
#affiche les tables de la base de données
print(client.list_database_names())

#Genere un id aléatoire
def generateId(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    



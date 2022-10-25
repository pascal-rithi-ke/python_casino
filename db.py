import os, pymongo

from dotenv import load_dotenv
from FolderClass.Class import User,Partie

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.lfi8yfs.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(DATABASE_URL)

tableBdd = client["casino_project"]
userCollection = tableBdd["users"]
partieCollection = tableBdd["partie"]

    
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.sp2ay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client=pymongo.MongoClient(DATABASE_URL)
print(client.list_database_names())
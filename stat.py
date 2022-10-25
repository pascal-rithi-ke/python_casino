import os, pymongo, csv
import matplotlib.pyplot as plt
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('ID_MONGO')
PASS = os.environ.get('PASS_MONGO')

DATABASE_URL =f'mongodb+srv://{ID}:{PASS}@cluster0.lfi8yfs.mongodb.net/?retryWrites=true&w=majority'
client=pymongo.MongoClient(DATABASE_URL)

tableBdd = client["casino_project"]
partieCollection = tableBdd["partie"]

Nbpartie = partieCollection.count_documents({}) # 2
# nombre de coup à la fin
# insérer à la fin de la manche

data = []
for info in partieCollection.find():
    data.append(info)
df = pd.DataFrame(data)    
df.to_csv("DataGame.csv", sep=";", encoding='utf-8', index=False)

x = []
y = []
with open('DataGame.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ';')
      
    for row in plots:
        x.append(row[0])
        y.append(row[1])
    print(row)
  
plt.bar(x, y, color = 'g', width = 0.72, label = "Indice du jeu")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Total de partie jouée:'+ str(Nbpartie))
plt.legend()
plt.show()
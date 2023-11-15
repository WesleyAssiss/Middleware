from connector import ConnectionDB
import random


db = ConnectionDB()
id = random.randint(0, 10)
resp = db.insert(id,'ALARME ATIVADO')
print(resp)

resp = db.select_many()
for key, value in resp:
    print(f'{key}: {value}')

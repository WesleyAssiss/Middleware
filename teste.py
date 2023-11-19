from connector import ConnectionDB
import random
import cryptocode


db = ConnectionDB()
id = random.randint(0, 10)
x = cryptocode.encrypt("alarme ativado", "999")
resp = db.insert(id, x)
print(resp)

resp = db.select_many()
for key, value in resp:
    print(f'{key}: {cryptocode.decrypt(value, "999")}')

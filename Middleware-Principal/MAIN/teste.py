from BANCO import connector

db = connector.ConnectionDB()


resp = db.select_many()

for i in resp:
    print(i)
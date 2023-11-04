from pymongo import MongoClient

class ConnectionDB:

    def __init__(self) -> None:
        self.client = MongoClient("localhost", 27017)
        self.db = self.client['sensor']
        self.collection = self.db['tb_sensor']
    
    def insert(self, acao, data_hora, estado):
        filtro = {"acao": acao, "data_hora": data_hora, "estado": estado}
        resp = self.collection.insert_one(filtro)
        if not resp:
            return('error')
    
    def select_one(self):
        resp = self.collection.find_one()
        if not resp:
            return('error')
        
    def select_many(self):
        resp = self.collection.find()
        if not resp:
            return('error')


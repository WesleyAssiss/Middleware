from pymongo import MongoClient
from bson.json_util import dumps, loads

class ConnectionDB:
    def __init__(self, controlador_id) -> None:
        self.client = MongoClient("localhost", 27017)
        self.db = self.client[f'sensor_controlador_{controlador_id}']
        self.collection = self.db[f'tb_sensor_controlador_{controlador_id}']

    def insert(self, acao, estado):
        filtro = {"acao": acao, "estado": estado}
        resp = self.collection.insert_one(filtro)
        if not resp:
            return 'error'
        return 'Dado Inserido!'

    def select_one(self):
        resp = self.collection.find_one()
        if not resp:
            return 'error'
        return self.__transformar_dados(resp)

    def select_many(self):
        resp = self.collection.find()
        if not resp:
            return 'error'
        return self.__transformar_dados(resp)

    def __transformar_dados(self, dados):
        dados_dict = loads(dumps(dados))
        for i in dados_dict:
            i.pop('_id')
        return dados_dict

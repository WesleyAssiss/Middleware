import rpyc
from connector import ConnectionDB
from sub_controlador import *
from pub_controlador import *


class MeuServico(rpyc.Service):

    db = ConnectionDB()

    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_one(self):
        resp = self.db.select_one()
        return resp
    
    def exposed_select_many(self):
        resp = self.db.select_many()
        return resp

    def exposed_mudar_estado_atuador(self):
        public("Alarme desativado")
    
    def exposed_acompanhar_sensor(self):
        resp = on_message()
        return resp

    def on_disconnect(self, conn):
        print("disconnect")


from rpyc.utils.server import ThreadedServer

t = ThreadedServer(MeuServico, port=18861)
t.start()

import rpyc
from connector import ConnectionDB
from pub_controlador import *


class MeuServico(rpyc.Service):

    db = ConnectionDB()

    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_one(self):
        self.db.select_one()
    
    def exposed_select_many(self):
        self.db.select_many()

    def exposed_mudar_estado_atuador(self):
        public("Alarme desativado")
    
    def exposed_acompanhar_sensor(self):
        pass

    def on_disconnect(self, conn):
        print("disconnect")


from rpyc.utils.server import ThreadedServer

t = ThreadedServer(MeuServico, port=18861)
t.start()

import rpyc
from connector import ConnectionDB
from pub_sensor import *


class MeuServico(rpyc.Service):

    db = ConnectionDB()
    
    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_many(self):
        resp = self.db.select_many()
        return resp
    
    def exposed_mudar_estado_atuador(self):
        mudar_estado()

    def on_disconnect(self, conn):
        print("disconnect")


if __name__=="__main__":
    from rpyc.utils.server import ThreadedServer
    
    print('servidor on')

    t = ThreadedServer(MeuServico, port=18861)
    t.start()

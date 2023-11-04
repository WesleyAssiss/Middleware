import rpyc
from teste import *


class MeuServico(rpyc.Service):

    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_sensor(self):
        pass

    def exposed_mudar_estado_atuador(self):
        pass

    def on_disconnect(self, conn):
        print("disconnect")


from rpyc.utils.server import ThreadedServer

t = ThreadedServer(MeuServico, port=18861)
t.start()

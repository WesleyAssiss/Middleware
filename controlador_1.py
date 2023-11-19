import rpyc
from connector import ConnectionDB
from broker_configs import broker_configs
import paho.mqtt.publish as publish


class MeuServico(rpyc.Service):

    db = ConnectionDB()
    
    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_many(self):
        resp = self.db.select_many()
        return resp
    
    def exposed_mudar_estado_atuador(self):
        broker_address = broker_configs["HOST"]
        port = broker_configs["PORT"]

        topic = broker_configs["TOPIC"]
        message = "MUDAR ESTADO"

        publish.single(topic, message, hostname=broker_address, port=port)
        return f"Estado alterado"

    def on_disconnect(self, conn):
        print("disconnect")


if __name__=="__main__":
    from rpyc.utils.server import ThreadedServer
    
    print('servidor on')

    t = ThreadedServer(MeuServico, port=18860)
    t.start()

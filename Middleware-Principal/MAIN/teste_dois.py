import paho.mqtt.client as mqtt
from BANCO.connector import ConnectionDB
from BROKER.broker_configs import broker_configs
import threading
from queue import Queue
import rpyc


conn_db = ConnectionDB()
dados_do_sensor = Queue()
dados_do_sensor_lock = threading.Lock()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(broker_configs["TOPIC"])

def on_message(client, userdata, msg):
    add(msg)
    print(msg.payload.decode())
    # trata_message(msg)

def add(msg):
    with dados_do_sensor_lock:
        dados_do_sensor.put(msg.payload.decode())
        print(dados_do_sensor.get())

def trata_message(msg):
    acao, data_hora = msg.payload.decode().split(";")
    conn_db.insert(acao=acao, data_hora=data_hora, estado="ALARME ACIONADO")

def inicia_loop():    
    client = mqtt.Client()
    client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

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

    # def exposed_mudar_estado_atuador(self):
    #     return dados_do_sensor
    
    def exposed_acompanhar_sensor(self):
        with dados_do_sensor_lock:
            if dados_do_sensor.empty:
                return dados_do_sensor.get()
        return None

    def on_disconnect(self, conn):
        print("disconnect")


if __name__=="__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MeuServico, port=18861)
    t.start()

    thread_sub = threading.Thread(target=inicia_loop)

    thread_sub.start()

    thread_sub.join()
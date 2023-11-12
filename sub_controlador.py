import paho.mqtt.client as mqtt
from connector import ConnectionDB
from broker_configs import broker_configs
import threading
from queue import Queue


conn_db = ConnectionDB()
dados_do_sensor = Queue()
dados_do_sensor_lock = threading.Lock()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(broker_configs["TOPIC"])

def on_message(client, userdata, msg):
    add(msg)
    print(msg.payload.decode())
    trata_message(msg)

def add(msg):
    with dados_do_sensor_lock:
        dados_do_sensor.put(msg.payload.decode())

def trata_message(msg):
    acao = msg.payload.decode()
    conn_db.insert(acao=acao, estado="ALARME ACIONADO")

def inicia_loop():    
    client = mqtt.Client()
    client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

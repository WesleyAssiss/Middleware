import paho.mqtt.client as mqtt
from connector import ConnectionDB
from broker_configs import broker_configs

conn_db = ConnectionDB()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(broker_configs["TOPIC"])

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    trata_message(msg)

def trata_message(msg):
    acao, data_hora = msg.payload.decode().split(";")
    conn_db.insert(acao=acao, data_hora=data_hora, estado="Alarme ativado")

    
client = mqtt.Client()
client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
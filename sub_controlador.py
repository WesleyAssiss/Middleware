import paho.mqtt.client as mqtt
from connector import ConnectionDB
from broker_configs import broker_configs
import time


conn_db = ConnectionDB()
alarme_ativado = False


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(broker_configs["TOPIC"])


def on_message(client, userdata, msg):
    print(msg.payload.decode())
    verifica_mensagem(msg)


def liga_alarme():
    global alarme_ativado
    alarme_ativado = True
    conn_db.insert(0, estado="ALARME ACIONADO")
    desliga_alarme()


def desliga_alarme():
    global alarme_ativado
    if alarme_ativado:
        alarme_ativado = False
        time.sleep(5)
        conn_db.insert(0, estado="ALARME DESLIGADO")


def muda_estado():
    global alarme_ativado
    if alarme_ativado:
        desliga_alarme()
    else:
        liga_alarme()


def verifica_mensagem(msg):
    if msg.payload.decode() == "ALARME ACIONADO":
        print('ta aqui')
        liga_alarme()
    elif msg.payload.decode() == "MUDAR ESTADO":
        print('aquiii')
        desliga_alarme()
    else:
        'error'


client = mqtt.Client()
client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

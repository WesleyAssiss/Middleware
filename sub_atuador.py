import paho.mqtt.client as mqtt
from broker_configs import broker_configs


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(broker_configs["TOPIC"])

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    acende_lampada()

def acende_lampada():
    print("ALARME ACIONADO")
 
client = mqtt.Client()
client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
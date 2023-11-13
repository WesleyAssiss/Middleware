import paho.mqtt.publish as publish
from BROKER.broker_configs import broker_configs
import time

while True:
    broker_address = broker_configs["HOST"]
    port = broker_configs["PORT"]

    topic = broker_configs["TOPIC_SENSOR"]
    message = "MOVIMENTO DETECTADO"

    publish.single(topic, message, hostname=broker_address, port=port)

    print("Enviando movimento para o Controlador01 e Controlador02")

    time.sleep(5)

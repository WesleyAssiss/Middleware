import paho.mqtt.publish as publish
from broker_configs import broker_configs

def mudar_estado():
    broker_address = broker_configs["HOST"]
    port = broker_configs["PORT"]

    topic = broker_configs["TOPIC"]
    message = "MUDAR ESTADO"

    publish.single(topic, message, hostname=broker_address, port=port)
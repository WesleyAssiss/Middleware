import paho.mqtt.client as mqtt
from broker_configs import broker_configs

def public(pyload = "teste"):
    mqtt_client = mqtt.Client('meu_publisher')
    mqtt_client.connect(broker_configs["HOST"], broker_configs["PORT"])

    mqtt_client.publish(broker_configs["TOPIC"], payload=pyload)

    print("publiquei!!!")
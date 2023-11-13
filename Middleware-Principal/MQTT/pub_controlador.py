import paho.mqtt.client as mqtt
from BROKER.broker_configs import broker_configs
import time
def public(payload="teste", topic=None):
    mqtt_client = mqtt.Client('meu_publisher')
    mqtt_client.connect(broker_configs["HOST"], broker_configs["PORT"])

    mqtt_client.loop_start()  # Inicia o loop MQTT em uma thread separada

    while True:
        mqtt_client.publish(topic, payload=payload)
        print(f"Publicado no tópico {topic}!")
        # Intervalo para a próxima publicação (ajuste conforme necessário)
        time.sleep(5)

# Mantendo a publicação contínua para Controlador 01
public(payload="Comando para Controlador 01", topic=broker_configs["TOPIC_CONTROLADOR01"])

# Mantendo a publicação contínua para Controlador 02
public(payload="Comando para Controlador 02", topic=broker_configs["TOPIC_CONTROLADOR02"])

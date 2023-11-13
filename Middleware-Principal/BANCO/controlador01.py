import paho.mqtt.client as mqtt
from BROKER.broker_configs import broker_configs

def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe(broker_configs["TOPIC_SENSOR"])

def on_message(client, userdata, msg):
    mensagem_do_sensor = msg.payload.decode()
    print("Mensagem do sensor para Controlador 01:", mensagem_do_sensor)


    publicar_no_mqtt(mensagem_do_sensor, broker_configs["TOPIC_ATUADOR"])
    informar_atuador(mensagem_do_sensor)  # Enviando mensagem para o sub_atuador

def publicar_no_mqtt(mensagem, topico):
    cliente_mqtt = mqtt.Client('controlador01_publicador')
    cliente_mqtt.connect(broker_configs["HOST"], broker_configs["PORT"])
    cliente_mqtt.publish(topico, payload=mensagem)

def informar_atuador(acao):
    mqtt_client = mqtt.Client('controlador01_sub_atuador')
    mqtt_client.connect(broker_configs["HOST"], broker_configs["PORT"])
    mqtt_client.publish(broker_configs["TOPIC_CONTROLADOR01"], payload=acao)
    print(f"Mandando ação para o sub_atuador: {acao}")

# Configuração do cliente MQTT para Controlador01
cliente = mqtt.Client()
cliente.on_connect = on_connect
cliente.on_message = on_message
cliente.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
cliente.loop_forever()

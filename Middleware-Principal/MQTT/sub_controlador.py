import paho.mqtt.client as mqtt
from BANCO.connector import ConnectionDB
from BROKER.broker_configs import broker_configs

def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe(broker_configs["TOPIC_SENSOR"])
    client.subscribe(broker_configs["TOPIC_CONTROLADOR01"])
    client.subscribe(broker_configs["TOPIC_CONTROLADOR02"])

def on_message(client, userdata, msg):
    acao = msg.payload.decode()
    if msg.topic == broker_configs["TOPIC_SENSOR"]:
        # Registro na base de dados para ambos os controladores
        conn_db = ConnectionDB(controlador_id=1 if "CONTROLADOR01" in msg.topic else 2)
        conn_db.insert(acao=acao, estado="ALARME ACIONADO")
        print(f"Ação registrada para {msg.topic}: {acao}")

def iniciar_conexao():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
    client.loop_start()  # Inicia o loop MQTT em uma thread separada

    # Mantém o script em execução contínua
    while True:
        continue  # Mantém a execução contínua, você pode adicionar outras operações aqui

# Iniciar a escuta do tópico SENSOR para o Controlador 01 e Controlador 02
# Exemplo:
iniciar_conexao()

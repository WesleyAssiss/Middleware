import paho.mqtt.client as mqtt
from BROKER.broker_configs import broker_configs

alarme_acionado = False


def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe(broker_configs["TOPIC_CONTROLADOR01"])
    client.subscribe(broker_configs["TOPIC_CONTROLADOR02"])


def on_message(client, userdata, msg):
    global alarme_acionado
    acao = msg.payload.decode()

    if acao == "ALARME ACIONADO":
        alarme_acionado = True
        print("Alarme foi acionado!")
    elif acao == "DESATIVAR ALARME":
        alarme_acionado = False
        print("Alarme desativado!")
    else:
        print("Ação desconhecida:", acao)

    tomar_decisao()


def acende_lampada():
    print("ALARME ACIONADO")


def desliga_alarme():
    print("ALARME DESLIGADO")


def tomar_decisao():
    if alarme_acionado:
        desliga_alarme()
    else:
        acende_lampada()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_configs["HOST"], broker_configs["PORT"], broker_configs["KEPPALIVE"])
client.loop_forever()

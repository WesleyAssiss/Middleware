import rpyc

proxy = rpyc.connect('localhost', 18861)


def select_one():
    resp = proxy.root.select_one()
    print(resp)


def select_many():
    resp = proxy.root.select_many()
    print(resp)


def mudar_estado_atuador():
    resp = proxy.root.mudar_estado_atuador()
    print(resp)


def acompanhar_sensor(id):
    resp = proxy.root.acompanhar_sensor()
    print(resp)


while True:
    print()
    entrada = input("1 - Entrar no Sistema\n"
                    "2 - Entrar na Sala\n"
                    "3 - Sair da Sala\n"
                    "4 - Enviar mensagem\n"
                    "9 - Finalizar Sistema\n"
                    "Escolha uma opção: ")
    print()

    if int(entrada) == 1:
        select_one()

    elif int(entrada) == 2:
        select_many()

    elif int(entrada) == 3:
        mudar_estado_atuador()

    elif int(entrada) == 4:
        acompanhar_sensor()

    elif int(entrada) == 9:
        proxy.closed()
        break
    else:
        print("Entrada inválida.")

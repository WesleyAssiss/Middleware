import rpyc

proxy = rpyc.connect('localhost', 18861)


def select_one():
    resp = proxy.root.select_one()
    print(resp)


def select_many():
    resp = proxy.root.select_many()

    for value in resp:
        print(value)


def mudar_estado_atuador():
    resp = proxy.root.mudar_estado_atuador()
    print(resp)


def acompanhar_sensor():
    resp = proxy.root.acompanhar_sensor()
    print(f'resposta: {resp}')


while True:
    print()
    entrada = input("1 - Mostrar última atualização sensor\n"
                    "2 - Mostrar todos os dados coletados pelo sensor\n"
                    "3 - Mudar estado do atuador\n"
                    "4 - Acompanhar sensor\n"
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
        proxy.close()
        break
    else:
        print("Entrada inválida.")

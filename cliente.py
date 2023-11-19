import time
import rpyc
from cryptocode import decrypt


def conectar_ao_controlador(controlador):
    while True:
        try:
            print(f"Tentando se conectar ao Controlador{controlador}...")
            proxy = rpyc.connect('localhost', 18860 if controlador == 1 else 18861)
            print(f"Conexão bem-sucedida com o Controlador{controlador}.")
            return proxy
        except ConnectionRefusedError:
            print(f"Erro ao conectar ao Controlador{controlador}. Tentando novamente em 10 segundos...")
            time.sleep(10)


def trocar_controlador(atual, outro):
    print(f"Parando de se conectar ao Controlador{atual}. Procurando outro controlador disponível...")
    proxy.close()
    return conectar_ao_controlador(outro)


controlador_atual = 1
proxy = conectar_ao_controlador(controlador_atual)


def select_many():
    resp = proxy.root.select_many()

    for value in resp:
        print(f"{value[0]}: {decrypt(value[1], str(value[0]))}")


def mudar_estado_atuador():
    resp = proxy.root.mudar_estado_atuador()
    print(resp)


while True:
    print()
    entrada = input("1 - Mostrar dados do banco\n"
                    "2 - Mudar estado do atuador\n"
                    "0 - Finalizar Sistema\n"
                    "Escolha uma opção: ")
    print()

    try:
        if int(entrada) == 1:
            select_many()

        elif int(entrada) == 2:
            mudar_estado_atuador()

        elif int(entrada) == 0:
            proxy.close()
            break
        else:
            print("Entrada inválida.")
    except ConnectionRefusedError:
        print(f"Erro ao acessar Controlador{controlador_atual}. Tentando conectar a outro controlador...")

        controlador_atual = 3 - controlador_atual
        proxy = trocar_controlador(controlador_atual, 3 - controlador_atual)

print("Sistema finalizado.")

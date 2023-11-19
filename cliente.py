import rpyc
from cryptocode import decrypt

proxy = rpyc.connect('localhost', 18861)

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

    if int(entrada) == 1:
        select_many()

    elif int(entrada) == 2:
        mudar_estado_atuador()

    elif int(entrada) == 0:
        proxy.close()
        break
    else:
        print("Entrada inválida.")

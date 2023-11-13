import rpyc
import time

def conectar_ao_controlador(port, client_id):
    tentativas = 0
    while tentativas < 5:  # Defina um número máximo de tentativas
        try:
            proxy = rpyc.connect('localhost', port)
            print(f"Conectado ao Controlador na porta {port}")
            # Enviar uma mensagem de confirmação para o controlador
            proxy.root.confirmar_conexao(client_id)
            return proxy
        except ConnectionRefusedError:
            print(f"Controlador na porta {port} indisponível. Tentando outro controlador.")
            tentativas += 1
            time.sleep(5)
    print("Número máximo de tentativas alcançado. Controlador indisponível.")
    return None

def select_one(proxy):
    while True:
        try:
            resp = proxy.root.select_one()
            print("Última atualização do sensor:", resp)
            break
        except:
            print("Esperando conexão com o controlador...")
            time.sleep(5)

def select_many(proxy):
    while True:
        try:
            resp = proxy.root.select_many()
            print("Todos os dados coletados pelo sensor:")
            for value in resp:
                print(value)
            break
        except:
            print("Esperando conexão com o controlador...")
            time.sleep(5)

def mudar_estado_atuador(proxy):
    while True:
        try:
            new_state = input("Insira o novo estado do atuador: ")
            resp = proxy.root.mudar_estado_atuador(new_state)
            print(resp)
            break
        except:
            print("Esperando conexão com o controlador...")
            time.sleep(5)

def acompanhar_sensor(proxy):
    while True:
        try:
            resp = proxy.root.acompanhar_sensor()
            print(f"Dados do sensor: {resp}")
            break
        except:
            print("Esperando conexão com o controlador...")
            time.sleep(5)

def encerrar_conexao(proxy):
    proxy.close()

def menu():
    while True:
        print("\nEscolha uma opção:")
        entrada = input("1 - Mostrar última atualização do sensor\n"
                        "2 - Mostrar todos os dados coletados pelo sensor\n"
                        "3 - Mudar estado do atuador\n"
                        "4 - Acompanhar sensor\n"
                        "9 - Finalizar Sistema\n"
                        "Escolha uma opção: ")

        if entrada in ['1', '2', '3', '4']:
            port = 18861 if entrada in ['1', '2'] else 18862
            client_id = "client1" if entrada in ['1', '2'] else "client2"  # Definir o client_id
            proxy = conectar_ao_controlador(port, client_id)  # Ajuste para passar o client_id
            if proxy:
                if entrada == '1':
                    select_one(proxy)
                elif entrada == '2':
                    select_many(proxy)
                elif entrada == '3':
                    mudar_estado_atuador(proxy)
                elif entrada == '4':
                    acompanhar_sensor(proxy)
            else:
                print("Esperando conexão com o controlador...")

        elif entrada == '9':
            if proxy:
                encerrar_conexao(proxy)
            break
        else:
            print("Entrada inválida.")

if __name__ == "__main__":
    menu()

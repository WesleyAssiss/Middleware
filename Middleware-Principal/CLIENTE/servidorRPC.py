import rpyc
import time
from BANCO.connector import ConnectionDB

class MeuServico(rpyc.Service):
    clients = {"client1": False, "client2": False}
    db_controller_01 = ConnectionDB(1)
    db_controller_02 = ConnectionDB(2)

    def on_connect(self, conn):
        print("Conexão recebida")

    def on_disconnect(self, conn):
        print("Conexão encerrada")

    def exposed_confirmar_conexao(self, client_id):
        self.clients[client_id] = True
        print(f"Cliente {client_id} conectado!")

    def exposed_select_one(self, controller_id):
        if controller_id == 1:
            return self._reconectar(self.db_controller_01.select_one)
        elif controller_id == 2:
            return self._reconectar(self.db_controller_02.select_one)
        else:
            return "Controlador inválido"

    def exposed_select_many(self, controller_id):
        if controller_id == 1:
            return self._reconectar(self.db_controller_01.select_many)
        elif controller_id == 2:
            return self._reconectar(self.db_controller_02.select_many)
        else:
            return "Controlador inválido"

    def exposed_mudar_estado_atuador(self, new_state, controller_id):
        if controller_id == 1:
            return self._reconectar(self.db_controller_01.insert, new_state)
        elif controller_id == 2:
            return self._reconectar(self.db_controller_02.insert, new_state)
        else:
            return "Controlador inválido"

    def exposed_acompanhar_sensor(self, controller_id):
        if controller_id == 1:
            return self._reconectar(self.db_controller_01.select_one)
        elif controller_id == 2:
            return self._reconectar(self.db_controller_02.select_one)
        else:
            return "Controlador inválido"

    def _reconectar(self, func, *args):
        while True:
            try:
                return func(*args)
            except:
                print("Esperando conexão com o banco de dados...")
                time.sleep(5)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    print('Servidor para ambos os Controladores ativo')

    t = ThreadedServer(MeuServico, port=18860)  # Definindo a porta para o servidor único
    t.start()

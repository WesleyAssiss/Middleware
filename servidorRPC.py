import rpyc
from connector import ConnectionDB


class MeuServico(rpyc.Service):

    db = ConnectionDB()
    
    def on_connect(self, conn):
        print("connected")
    
    def exposed_select_one(self):
        resp = self.db.select_one()
        return resp
    
    def exposed_select_many(self):
        resp = self.db.select_many()
        return resp

    # def exposed_mudar_estado_atuador(self):
    #     return dados_do_sensor
    
    # def exposed_acompanhar_sensor(self):
    #     with dados_do_sensor_lock:
    #         if dados_do_sensor.empty:
    #             return dados_do_sensor.get()
        # return None

    def on_disconnect(self, conn):
        print("disconnect")


if __name__=="__main__":
    from rpyc.utils.server import ThreadedServer
    
    print('servidor on')

    t = ThreadedServer(MeuServico, port=18861)
    t.start()

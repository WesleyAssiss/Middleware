import redis

class ConnectionDB:

    def __init__(self) -> None:
        self.redis_connection = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        
    def insert(self, id, estado):
        resp = self.redis_connection.set(id, estado)
        if not resp:
            return 'Error'
        return 'Dado Inserido!'
        
    def select_many(self):
        all_keys = self.redis_connection.keys('*')

        all_values = self.redis_connection.mget(all_keys)
        if not all_values:
            return 'error'
        return zip(all_keys, all_values)

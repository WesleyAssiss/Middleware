import threading
from sub_controlador import inicia_loop

thread_sub = threading.Thread(target=inicia_loop)

thread_sub.start()

thread_sub.join()

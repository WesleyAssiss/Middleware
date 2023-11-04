import threading
import os
import subprocess


def inicia_programa(nome_arquivo):
    p = subprocess.Popen(["gnome-terminal"])


if __name__ == "__main__":

    arquivos = ['sub_controlador.py']

    processos = []
    for arquivo in arquivos:
        processos.append(threading.Thread(target=inicia_programa, args=(arquivo,)))
        # Ex: adicionar o porcesso `threading.Thread(target=inicia_programa, args=('x.py',))`

    for processo in processos:
        processo.start()

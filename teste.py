import sys
import subprocess

# def run_sub_controlador():

arquivo = 'sub_controlador.py'

processo = subprocess.Popen([sys.executable, arquivo])
subprocess.Popen.wait(processo)

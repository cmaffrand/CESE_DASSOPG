import json
from socket import socket, AF_INET, SOCK_DGRAM
import sys
import time
import os
import signal

class Cvsfile:
    
    def __init__(self):
        pass
            
    @staticmethod
    def load_csv(filename):
        listdic = []
        try:
            with open(filename,"r",encoding="utf-8") as f:
                for l in f:
                    aux = l.strip("\n")
                    aux_split = aux.split(",")
                    if aux_split[0] != "id":
                        try:
                            dic = { "id": int(aux_split[0]), "value1": float(aux_split[2]), "value2": float(aux_split[3]), "name": str(aux_split[1]) }
                            listdic.append(dic)
                        except Exception as e:
                            print(f"error: {e} type: {type(e)}")
                            print(f"Archivo '{filename}' mal conformado")                        
                return listdic
        except FileNotFoundError as e:
            print(f"error: {e} type: {type(e)}")
            print(f"No se pudo cargar el archivo: '{filename}'")
            exit()
        except Exception as e:
            print(f"error: {e} type: {type(e)}")
            exit()

    @staticmethod
    def csv_change(filename):
        global filetime
        temptime = os.stat(filename)[8]
        try:
            if temptime != filetime:
                filetime = temptime
                return False
            return True 
        except Exception as e:
            filetime = temptime
            return True
        
class Udpsend:
    
    def __init__(self,ip="localhost",port=10000):
        self.set_ip(ip)
        self.set_port(port)
        
    def set_ip(self,ip):
        self.__ip = ip
        
    def set_port(self,port):
        self.__port = port

    def send(self, msg):
        global iterations
        try: 
            iterations = iterations + 1
        except Exception as s:
            iterations = 1
        with socket(AF_INET, SOCK_DGRAM) as s:
            s.sendto(msg, (self.__ip, self.__port))
            print(f"Dato enviado a IP: {self.__ip} Puerto: {self.__port} - Iteracion: {iterations}")       
    
class Main:
    
    def __init__(self):
        pass      

    def main(self):
             
        # Lectura de configuracion 
        config = dict()
        with open('config.txt', 'r') as cfile:
            for line in cfile:
                cline = line.strip().split('=')
                config[cline[0]] = cline[1]
        filename = config['path'] + config['name']
        mode = config['mode']
        period = int(config['period'])
        # Atributos de entrada
        try:
            localport = int(config['localport'])
            pizarraAdd = config['pizarraAdd']
            pizarraPort = int(config['pizarraPort'])            
            p = Udpsend(pizarraAdd,pizarraPort)
            print("Iniciando puerto "+str(localport)+"...")
        except Exception as e:
            print(f"error: {e} type: {type(e)}")
            print("Configuracion incorrecta")
            exit(1)
        
        while True:
            # Levanta CSV
            datalistdic = Cvsfile.load_csv(filename) 
            # Pasa a string JSON
            datastr = json.dumps(datalistdic)
            # Pasa a Bytes
            databytes = datastr.encode('utf-8')            
            # Envio de datos
            p.send(databytes)           
            if mode == "filechange":
                #Implementacion por cambio en el archivo
                while (Cvsfile.csv_change(filename)):
                    time.sleep(1)
            elif mode == "periodic":
                #Implementacion periodica
                time.sleep(period)
            else:
                print("Error en la configuracion del modo")
                exit()
            
def handler(sig, frame):  
    print("Signal Number:", sig) 
    print(f"ParserService finalizado por el usuario")
    exit()     

# Manejo de Señal
signal.signal(signal.SIGINT, handler)
# Inicia el Main
m = Main()
m.main()


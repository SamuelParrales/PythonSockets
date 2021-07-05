
import socket
import json

def EnviarDatosSocket(numeros):
    
    #Creción de un socket TCP/IP
    newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Realizando la conexión con el servidor")
    newsocket.connect(('localhost', 25648))  # Se especifica la IP y el puerto a la que se va a enviar
    
    print("Conectado con el servidor")    
    msg = json.dumps(numeros)   #Esto se va a enviar al servidor en formato json
    print("Enviados datos al servidor")

    newsocket.send(msg.encode()) #El mensaje debe ser enviado codificado
    print("Esperando respuesta")

    respuesta = newsocket.recv(1024)  # Recibe hasta 1024

    print(respuesta.decode())
    newsocket.close()
 

print('Ingrese los datos a enviar al servidor\n')
base = input('Ingesa la base: ')
exponente = input('Ingresa el exponente: ' )

EnviarDatosSocket([base,exponente])
   
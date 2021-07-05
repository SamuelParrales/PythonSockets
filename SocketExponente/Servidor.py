
import socket 
import json



def elevarAlExponente(base,exponente):
    try:
        base = float(base)
        exponente = float(exponente)
        if((base==0)&(exponente<1)):
            return False
        
        return pow(base,exponente)
    
    except:
        print("Tipo de dato incorrecto") 
        return False
    
    
#Creando socket tcp/ip
newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.bind(('localhost', 25648)) #Se establece el puerto por el cual va escuchar
newsocket.listen(5) #Cantidad de peticiones que puede manejar

while True:
    print("Esperando nueva petición")
    conexion, addr = newsocket.accept()
    print("Nueva conexion establecida " + str(addr))
    peticion = conexion.recv(1024)
    
    numeros = json.loads(peticion.decode())  #Petición descodificada
    base = numeros[0]
    exponente = numeros[1]

    respuesta = elevarAlExponente(base,exponente)  #Para controlar excepciones
    if(respuesta==False):
        print('Error, la conexión se cerrará')
        conexion.close()
        continue

    respuesta = str(respuesta)

    conexion.send(respuesta.encode())  #La respuesta se envia codigicada
    
    print("Respuesta enviada al cliente")
    conexion.close()



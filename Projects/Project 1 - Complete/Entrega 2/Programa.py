import plantilla_archivos
import os

def Programa():
    nodes_number = input("Ingrese el numero de nodos: ")
    partition_number = input("Ingrese el numero de particiones por nodo: ")
    port = 5000
    #Copy files to the corresponding nodes
    for j in range(97, 97 + int(nodes_number)):
        #Folder creation
        name = f"server-{chr(j)}"
        os.mkdir(name)
        #Copy of the server.py file
        plantilla_archivos.server_file(name)
        #Copy of constants
        port = port+1
        plantilla_archivos.constants_file(name,port)
        #Copy of forDB
        plantilla_archivos.fortDB_file(name)
        if j >= 123: break 

    #Partition assignment
    plantilla_archivos.particiones(nodes_number,partition_number)

    return int(nodes_number), int(partition_number)
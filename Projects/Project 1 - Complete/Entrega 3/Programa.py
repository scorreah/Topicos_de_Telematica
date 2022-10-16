import plantilla_archivos
import os
import json

def Programa():
    nodes_number = input("Ingrese el numero de nodos: ")
    partition_number = input("Ingrese el numero de particiones por nodo: ")
    slaves_number = input("Ingrese el numero de esclavos por nodo: ")
    port = 5000
    #Copy files to the corresponding nodes
    for j in range(97, 97 + int(nodes_number)):
        slave_table = []
        slave_table_m = []
        #Folder creation
        name = f"server-{chr(j)}"
        os.mkdir(name)
        #Copy of the server.py file
        plantilla_archivos.server_file(name)
        #Copy of constants
        port = port+1
        master_port = port
        plantilla_archivos.constants_file(name,port)
        #Copy of forDB
        plantilla_archivos.fortDB_file(name)
        #Copy files to the correspoding slaves
        for i in range(int(slaves_number)):
            slave_name = f"slave{i+1}-{chr(j)}" 
            #Folder creation
            os.mkdir(slave_name)
            #Copy of the server.py file
            if i == 0:
                plantilla_archivos.server_file(slave_name)
            plantilla_archivos.server_slave_file(slave_name)
            #Copy of constants
            port = port+1
            plantilla_archivos.constants_file(slave_name,port)
            #Copy of forDB
            plantilla_archivos.fortDB_file(slave_name)
            #Append to the slave_diccionario
            slave_info = {"slave_name":slave_name,"slave_port":port}
            slave_table.append(slave_info)
            if i == 0:
                slave_name_m = slave_name
                slave_info = {"master_name":name,"port":master_port}
                slave_table_m.append(slave_info)
            else:
                slave_table_m.append(slave_info)
        #Save json file for master
        json.dump(slave_table, open(name+"/"+"slave_table", "w+"))
        #Save json file for slave 1
        json.dump(slave_table_m, open(slave_name_m+"/"+"slave_table", "w+"))
        if j >= 123: break 
    
    #Partition assignment per node and per slave
    plantilla_archivos.particiones(nodes_number,partition_number,slaves_number)

    return int(nodes_number), int(partition_number), int(slaves_number)
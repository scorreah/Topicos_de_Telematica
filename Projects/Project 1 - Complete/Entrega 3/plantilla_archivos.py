import re
import json 

def server_file(name):
    server = open("copiar/server.py")
    copia_Server = server.read()
    server.close()
    path = name+"/server.py"
    nuevo_Server = open(path,"w")
    nuevo_Server.write(copia_Server)
    nuevo_Server.close()

def server_slave_file(name):
    server = open("copiar/server_slave.py")
    copia_Server = server.read()
    server.close()
    path = name+"/server_slave.py"
    nuevo_Server = open(path,"w")
    nuevo_Server.write(copia_Server)
    nuevo_Server.close()

def constants_file(name,port):
    constants = open("copiar/constants.py")
    copia_constants = constants.read()
    constants.close()
    path = name+"/constants.py"
    nuevo_constants = open(path,"w")
    nuevo_constants.write(copia_constants)
    nuevo_constants.close()
    with open(path,"r+") as f1:
        contents = f1.read()
        pattern = re.compile(re.escape("PORT = 5000"))
        contents = pattern.sub("PORT = "+str(port),contents)
        f1.seek(0)
        f1.truncate()
        f1.write(contents)
    
def fortDB_file(name):
    fortDB = open("copiar/fortDB.py")
    copia_fortDB = fortDB.read()
    fortDB.close()
    path = name+"/fortDB.py"
    nuevo_fortDB = open(path,"w")
    nuevo_fortDB.write(copia_fortDB)
    nuevo_fortDB.close()

def particiones(nodes_number,partition_number,slave_number):
    for z in range(97, 97 +int(nodes_number)):
        for j in range(int(partition_number)):
            name = f"server-{chr(z)}"
            partition_name = f"{name}-{j}"
            path = name+"/"+partition_name
            json.dump({}, open(path, "w+"))
            for i in range(int(slave_number)):
                slave_name = f"slave{i+1}-{chr(z)}"
                partition_s_name = f"{slave_name}-{j}"
                slave_path = slave_name+"/"+partition_s_name
                json.dump({}, open(slave_path, "w+"))


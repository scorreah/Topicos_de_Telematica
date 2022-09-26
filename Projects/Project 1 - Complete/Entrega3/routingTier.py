from ast import Try
import hashlib
from logging import exception
import socket
import constants
import threading
import json

#Conexion del cliente
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = constants.IP_SERVER

def hash_position(name):
    encoded_name = name.encode("utf-8")
    hash_encoded_name = hashlib.sha1(encoded_name).hexdigest()

    return int(hash_encoded_name[:7],16)

def main():
    print("***********************************")
    print("Routing tier is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    routing_execution()

def routing_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)                                                                                #Python's socket class assigns an IP address and a port number to a socket instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                                 #Provides an application program with the means to control socket behavior
    print ('Socket is bind to address and port...')
    server_socket.listen(5)                                                                                             #This denotes maximum number of connections that can be queued for this socket by the operating system.
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()                                                      #Accepts an incoming connection request from a TCP client
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))     #It allows you to manage concurrent threads(tasks, function calls) doing work at the same time.
        client_thread.start() 

def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        data = client_connection.recv(constants.RECV_BUFFER_SIZE)
        request = data.split(b'\r\n\r\n')
        query = request[0].decode().split(' ')                                                                          #Method and file_name b"GET /cover.jpg HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n"
        method = query[0]

        print('---------------- REQUEST ----------------')
        print(request[0].decode())
        if method == constants.PUT or method == constants.GET:
            hash_value = hash_position(query[1]) 
            print(f"{hash_value} {type(hash_value)}")

        routing_table = json.loads(json.load(open("routing_table", "r")))                                                           #Access the rounting table 
        status = b""
        #PUT y GET METHOD
        if(method == constants.PUT or method == constants.GET):
            partition_name,node_name,port = rt_get(routing_table,hash_value)
            status = server_connection(port, data, partition_name, routing_table)
        #EXIT METHOD
        elif(method == constants.EXIT):
            status = b'bye'
            client_connection.sendall(status)
            break
        else:
            status = b'ERROR: Invalid command'
        client_connection.sendall(status)

    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

def server_connection(port, data, partition_name, routing_table):

    
    node_socket = socket.socket()  # instantiate
    try:
        node_socket.connect((constants.IP_SERVER, port))  # connect to the server

        message = data 
        load = f"LOAD {partition_name}"
        node_socket.sendall(load.encode())  # load message
        load_res = node_socket.recv(1024)  # receive response
        
        node_socket.sendall(data)  # Request message
        data = node_socket.recv(1024)  # receive response

        bye = "EXIT"
        node_socket.sendall(bye.encode()) # Exit message
        bye = node_socket.recv(1024)      # receive response

        print('Received from server: ' + data.decode())  # show in terminal
        
        node_socket.close()  # close the connection   

        return data

    except Exception as E:
        print('Master connection fails, redirecting service to a slaver server ...')
        for partition in routing_table:
            if partition_name == partition["partition_name"]:
                slave_partition = partition["slaves"][0]["slave_name"]
                slave_port = partition["slaves"][0]["port"]
                break
              
        node_socket.close()

        node_socket = socket.socket()  # instantiate
        node_socket.connect((constants.IP_SERVER, slave_port))  # connect to the slave server
        message = data 
        load = f"LOAD {slave_partition}"
        node_socket.sendall(load.encode())  # load message
        load_res = node_socket.recv(1024)  # receive response
        
        node_socket.sendall(data)  # Request message
        data = node_socket.recv(1024)  # receive response

        bye = "EXIT"
        node_socket.sendall(bye.encode()) # Exit message
        bye = node_socket.recv(1024)      # receive response

        print('Received from slave: ' + data.decode())  # show in terminal
        
        node_socket.close()  # close the connection   

        return data

        

def rt_get(routing_table,hash_value):
    cont = 0
    if(hash_value > routing_table[-1]["min_hash"]):
        partition_name = routing_table[-1]["partition_name"]
        node_name = routing_table[-1]["node_name"]
        port = routing_table[-1]["port"]
    else:    
        for i in routing_table:
            cont += 1
            if(hash_value < i["min_hash"]):                                                                    #Decide the partition to save the key
                partition_name = routing_table[cont-1]["partition_name"]
                node_name = routing_table[cont-1]["node_name"]
                port = routing_table[cont-1]["port"]
                break
        
    
    return partition_name,node_name,port


if __name__ == "__main__":
    main()



# ********************************************************************************************
    # Lab: Introduction to sockets
    # Course: Topicos de Telemática
    # MultiThread TCP-SocketServer
# ********************************************************************************************

# Import libraries for networking communication and concurrency...

import socket
import threading
import fortDB
import constants

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER
active_database = None

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    server_execution()

#Function to start server process...
def server_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)                                                                                #Python's socket class assigns an IP address and a port number to a socket instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                                 #Provides an application program with the means to control socket behavior
    print ('Socket is bind to address and port...')
    server_socket.listen(5)                                                                                             #This denotes maximum number of connections that can be queued for this socket by the operating system.
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()                                                      #Accepts an incoming connection request from a TCP client
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))     #It allows you to manage concurrent threads(tasks, function calls) doing work at the same time.
        client_thread.start()                                                                                           #Call the start() method of the Thread class to start the thread. 
    
# Handler for manage incomming clients conections...
def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        request = client_connection.recv(constants.RECV_BUFFER_SIZE).split(b'\r\n\r\n')
        query = request[0].decode().split(' ')                                                                          #Method and file_name b"GET /cover.jpg HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n"
        method = query[0]                                                                                               #Split the request to get the method and the file name to obtain
        
        print('---------------- REQUEST ----------------')
        print(request[0].decode())
        status = b""
    
        #CREATE
        if (method == constants.CREATE or method== constants.LOAD):
            #Creates the data base
            if len(query) == 2:
                db_name = query[1]
                active_database = fortDB.fortDB(db_name)
                status = """\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
                        FORT DB
                    """.encode()
            else: 
                status = b'ERROR: Invalid command'         
        #PUT
        elif(method == constants.PUT):
            if len(query) == 3:
                active_database.put(query[1], query[2])
                status = b'OK! put'
            else: 
                status = b'ERROR: Invalid command'    
        #GET
        elif(method == constants.GET):
            if len(query) == 2:
                status = active_database.get(query[1]).encode()
            else: 
                status = b'ERROR: Invalid command'    
        #DELETE
        elif( method == constants.DELETE):
            if len(query) == 2:
                active_database.delete(query[1])
                status = b'OK! delete'
        #PING
        elif(method == constants.PING):
            #pingMethod(client)
            status = active_database.ping()
        #RESET
        elif(method == constants.RESET):
            db_name = active_database.location
            active_database.resetdb()
            status = b'OK! reset '
            status += db_name.encode()
        #EXIT
        elif (method == constants.EXIT):
            status = b'bye'
            client_connection.sendall(status)
            break
        else:
            response = '400 BCMD\n\rmethod-Description: Bad method\n\r'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
        client_connection.sendall(status)    
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

                                                                                    
if __name__ == "__main__":
    main()
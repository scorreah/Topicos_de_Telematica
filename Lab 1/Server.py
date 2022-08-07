# ********************************************************************************************
    # Project: Mini Server API Sockets
    # Course: ST0263 - Tópicos especiales en telemática
    # MultiThread TCP-SocketServer
    # Author: Simon Correa
# ********************************************************************************************

# Import libraries for networking communication and concurrency...

import socket
import threading
import constants
import methods
import time
import decode

# Defining a socket object...
# AF_INET define la familia(tipo) de direcciones como ipv4
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Define la direccion del servidor
server_address = constants.IP_SERVER


def main():
    print("***********************************"*2)
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Do you want to specify the port or choose default port? (Select a number)")
    print("1. Default Port")
    print("2. Specify Port")
    try:
        option = int(input(""))
        if option == 1:
            port = constants.PORT
        else:
            try:
                port = int(input("Type the port below: "))
            except:
                print("Port unknown, the default port has been chosen")
                port = constants.PORT
                
    except:
        print("Option unknown, the default port has been chosen")
        port = constants.PORT
    print("Port:", port)
    print("Do you want to show original or decoded request and response? (Write the number)")
    print("1. Original request & response")
    print("2. Decoded request & response")
    print("3. Both")
    try:
        global format 
        format = int(input(""))
        if format != 1 and format != 2 and format != 3:
            print("Default option chosen (1)")
            format = 1
    except:
        print("Default option chosen (1)")
        format = 1
        
    server_execution(port)
    
# Handler for manage incomming clients conections...

def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        # Mensaje de Request
        data_recevived = b''
        while True:
            datos = client_connection.recv(constants.RECV_BUFFER_SIZE)
            if (len(datos.split(b'\r\n\r\n')) > 1):
                data_recevived = data_recevived + datos.split(b'\r\n\r\n')[0]
                break
            data_recevived = data_recevived + datos
            time.sleep(0.1)
        remote_string = data_recevived.split(b'\r\n\r\n') 
        header = remote_string[0].decode(constants.ENCONDING_FORMAT)
        if len(remote_string) > 1:
            data = remote_string[1]
        else:
            data = ''
        remote_command = header.split()
        command = remote_command[0]
        print (f'Data received from: {client_address[0]}:{client_address[1]}')
        if format == 2 or format == 3:
            decode.request(header)
        
        if (command == constants.GET):
            response = methods.get(header, data, format)
            client_connection.sendall(response)
            is_connected = False
        
        else:
            response = '400 BCMD\n\rCommand-Description: Bad command\n\r'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

#Function to start server process...
def server_execution(port):
    # Tupla ip - puerto
    tuple_connection = (server_address, port)
    # Colocamos el socket visible en privado
    server_socket.bind(tuple_connection)
    # Definimos la configuracion del socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    # Especificamos al socket tener en cola no mas de 5 solicitudes por conexion
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        # Objeto socket, ip-puerto
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    pass


if __name__ == "__main__":
    main()
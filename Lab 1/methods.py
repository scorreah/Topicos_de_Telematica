import datetime


def get(r_header, r_data, format, web_root):
    string_list = r_header.split(" ")
    method = string_list[0]
    requesting_file = string_list[1]
    if format == 1:
        print('*'*51)
        print(' '*21, 'REQUEST', ' '*21)
        print(f'{r_header}\r\n')
    elif format == 3:
        print('-'*51)
        print(' '*21, 'ORIGINAL', ' '*21)
        print(f'{r_header}\r\n')


    myfile = requesting_file.split("?")[0]
    myfile = myfile.lstrip("/") # Remueve ese caracter
    myfile = myfile.replace("%20", " ")
    if(myfile == "" or myfile == "/"):
        myfile = "index.html"

    myfile = web_root + myfile
    try:
        # Lee en formato byte
        file = open(myfile, 'rb')
        response = file.read()
        file_len = len(response)
        file.close()

        dec_header = ''
        dec_header += 'HTTP Version: 1.1\r\n'
        dec_header += 'Status Code: 200 OK\r\n'

        header = 'HTTP/1.1 200 OK\r\n'

        x = datetime.datetime.now()
        dec_header += f'Date and Time: {x.strftime("%a, %d %b %Y %X %Z")}\r\n'
        header += f'Date: {x.strftime("%a, %d %b %Y %X %Z")}\r\n'

        server = 'Python-Sockets/1.0 (Ubuntu)'
        dec_header += f"Server Information, Version and O.S.: Python-Sockets 1.0 (Ubuntu)\r\n"
        header += f'Server: {server}\r\n'

        header += f'Content-Length: {file_len}\r\n'

        if myfile.endswith('.jpg') or myfile.endswith('jpeg'):
            mimetype = 'image/jpeg'
        elif (myfile.endswith('.gif')):
            mimetype = 'image/gif'
        elif (myfile.endswith('.csv')):
            mimetype = 'text/csv'
        elif (myfile.endswith('.css')):
            mimetype = 'text/css'
        elif (myfile.endswith('.json')):
            mimetype = 'application/json'
        elif (myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        else: 
            mimetype = 'text/html'
        dec_header += "Content and File Type: " + str(mimetype.replace('/', ' ')) + "\r\n"
        header += 'Content-Type: ' + str(mimetype) + '\r\n\r\n'
    except Exception as e:
        dec_header = ''
        dec_header += 'HTTP Version: 1.1\r\n'
        dec_header += 'Status Code: 404 Not Found\r\n'

        header = 'HTTP/1.1 404 Not Found \r\n\r\n'
        x = datetime.datetime.now()
        dec_header += f'Date and Time: {x.strftime("%a, %d %b %Y %X %Z")}\r\n'
        header += f'Date: {x.strftime("%a, %d %b %Y %X %Z")}\r\n'

        server = 'Python-Sockets/1.0 (Ubuntu)'
        dec_header += "Server Information, Version and O.S.: Python-Sockets 1.0 (Ubuntu)\r\n"
        header += f'Server: {server}\r\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

    if format == 1:
        print('*'*51)
        print(' '*21, 'RESPONSE', ' '*21)
        print(header)
    elif format == 2:
        print('*'*51)
        print(' '*21, 'RESPONSE', ' '*21)
        print(' '*20, '(DECODED)', ' '*20)
        print(dec_header)
    else:
        print('*'*51)
        print(' '*21, 'RESPONSE', ' '*21)
        print(' '*20, '(DECODED)', ' '*20)
        print(dec_header)
        print('-'*51)
        print(' '*20, 'ORIGINAL', ' '*20)
        print(header)
    
    final_response = header.encode('utf-8') + response
    return final_response


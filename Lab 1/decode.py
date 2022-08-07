def request(header):
    lines = header.split("\r\n")

    #Start Line
    # Analize
    start_line = lines[0].split()
    method = start_line[0]
    url = start_line[1]
    version = start_line[2]
    # Decode
    print('*'*51)
    print(' '*21, 'REQUEST', ' '*21)
    print(' '*20, '(DECODED)', ' '*20)
    print(f'Method: {method}')
    print(f'Resource (URL): {url}')
    print(f'HTTP Version: {version}')

    #Headers
    for n in range(1, len(lines)):
        line = lines[n].split(":", 1)
        key = line[0]
        value = line[1]
        if key == "Host":
            print(f'Domain (Host): {value}')
        elif key == "Connection":
            if value == "keep-alive":
                value = "Keep Connection Open"
            else:
                value = "Close Connection After Finished"
            print(f'Network Connection: {value}')
        elif key == "Referer":
            print(f'Previous Domain: {value}')
        elif key == "Content-Encoding":
            print(f'Compression Algorithms: {value}')
        elif key == "Accept-Encoding":
            print(f'Compression Algorithms: {value}')
        elif key == "Content-Length":
            print(f'Content Length: {value} Bytes')
        elif key == "sec-ch-ua":
            value = value.replace('\"', '')
            value = value.replace(';', ' ')
            value = value.replace('v=', '')
            print(f'User Agent Branding and Version: {value}')
        elif key == "sec-ch-ua-platform":
            value = value.replace('\"', '')
            print(f'User Agent Operating System: {value}')
        elif key == "Sec-Fetch-Dest":
            print(f'Request Destination (Resource Type): {value}')

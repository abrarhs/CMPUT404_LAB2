import socket

BYTES_TO_READ = 4096

def get(host,port):
    # created our request
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b'\n\n'

    # created out socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # we sent data on your socket
    s.connect((host, port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)

    # listen for responses
    response = s.recv(BYTES_TO_READ)
    while len(response) > 0 :
        print(response)
        response = s.recv(BYTES_TO_READ)
    
    s.close()

# call get function defined above on google.com on port 80.
get("www.google.com",80)


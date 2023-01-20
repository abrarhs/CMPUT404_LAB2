# CMPUT404-LAB2
Lab 2 
1. sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
2. The main difference between  server and client sockets are that server sockets need to bind host address and port address together. Another difference is that client sockets are able to connect to a different host server.
3. s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1). The SO_REUSEADDR flag instructs the kernel to reuse the local socket without waiting for the time to expire.
4. Connected by ('127.0.0.1', 56327)
5. Foobar
6. https://github.com/abrarhs/CMPUT404_LAB2

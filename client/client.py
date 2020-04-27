import socket
port = 9999
host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
s = b'Hello'
sock.send(s)

import socket
from flask import Flask
app = Flask(__name__)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

sock.bind((host, port))
sock.listen(5)
sock.setblocking(0)
@app.route('/')
def hello_world():
'''    try:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        conn.close()
        return data
    except BlockingIOError:
        return 'hi'''
    return "hello"


if __name__=='__main__':
    app.run()

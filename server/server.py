import socket
import zlib, base64


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

file = open('yougotmail.txt', "wb")
txt_chunk = client_socket.recv(2048)  # stream-based protocol

while txt_chunk:
    file.write(txt_chunk)
    txt_chunk = client_socket.recv(2048)

file.close()
client_socket.close()


file1=open('yougotmail.txt', 'r')
text=file1.read()
file1.close()

code=base64.b64encode(zlib.compress(text.encode('utf-8'),9))
code=code.decode('utf-8')

f=open('compressed.txt', 'w')
f.write(code)
f.close()
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1

file = open('1.txt', 'rb')
txt_data = file.read(2048)

while txt_data:
    client.send(txt_data)
    txt_data = file.read(2048)

file.close()
client.close()
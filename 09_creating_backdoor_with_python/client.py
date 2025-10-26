import socket

ip_address = '127.0.0.1'
port = 8080

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((ip_address, port))

message = "Client Successfully Connected.\n"
connection.sendto(message.encode(), (ip_address, port))

received_message = connection.recv(1024)
print(received_message.decode())

connection.close()

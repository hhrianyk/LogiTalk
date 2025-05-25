import socket
import threading

name = input("Для підключення на сервер введіть своє імя:")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.tcp.eu.ngrok.io', 15746))
print("Клієнт запустився")
client_socket.send(name.encode())

print(client_socket.recv(1024).decode())

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

threading.Thread(target=send_message).start()

while True:
    try:
        print(client_socket.recv(1024).decode())
    except:
        break




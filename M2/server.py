import socket

# Створення серверного сокету, що використовує протокол IPv4 (AF_INET) і TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язка сокету до локальної адреси (localhost) та порту 12345
server_socket.bind(('localhost', 12346))

# Виведення повідомлення про очікування на підключення клієнта
print("Чекаю на клієнта")

# Сервер починає слухати вхідні підключення (до 10 одночасних клієнтів)
server_socket.listen(100)

# Встановлення неблокуючого режиму для серверного сокету
server_socket.setblocking(False)

# Список для зберігання підключених клієнтів
clients = []

while True:
    try:
        # Прийняття підключення від клієнта (неблокуючий режим)
        connect, addres = server_socket.accept()
        print("Клієнт підключився:", addres)

        # Відправка привітального повідомлення новому клієнту
        connect.send("Привіт новий супер користувач".encode())

        # Отримання імені клієнта
        client_name = connect.recv(1024).decode()
        print("НОВИЙ КОРИСТУВА:",client_name)
        # Встановлення неблокуючого режиму для клієнтського сокету
        connect.setblocking(False)

        # Додавання клієнта та його імені до списку підключених клієнтів
        clients.append([connect, client_name])

    except:
        # Якщо не вдається прийняти підключення (наприклад, немає нових підключень), пропускаємо
        pass

    # Проходимо по всіх підключених клієнтах
    for client in clients:
        try:
            # Отримуємо повідомлення від клієнта
            message = client[0].recv(1024).decode().strip()

            # Передаємо це повідомлення всім іншим клієнтам, крім того, що надіслав його
            for c in clients:
                if client != c:
                    c[0].send(f'{client[1]}: {message}'.encode())

        except BlockingIOError:
            # Якщо сокет не має нових даних (немає повідомлень від клієнта), ігноруємо помилку
            pass
        except:
            # Якщо виникла помилка (ймовірно, клієнт відключився)
            print(f'Клієнт {client[1]} відключився.')
            # Закриваємо сокет клієнта
            client[0].close()
            # Видаляємо клієнта з списку підключених
            clients.remove(client)

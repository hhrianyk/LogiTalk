from socket import *
# Створюємо серверний сокет (TCP)
server_socket = socket(AF_INET, SOCK_STREAM)
# Прив'язуємо сокет до локальної адреси (localhost) і порту 52346
server_socket.bind(('localhost', 12346))
# Встановлюємо серверний сокет у режим прослуховування, дозволяючи до 5 підключень у черзі
server_socket.listen(5)
server_socket.setblocking(0)
clients = []

while True:
   try:
       # Приймаємо нове з'єднання (у неблокуючому режимі)
       connection, address = server_socket.accept()
       connection.setblocking(0)  # Робимо з'єднання також неблокуючим
       # Отримуємо ім'я клієнта при підключенні
       name_client = connection.recv(1024).decode().strip()
       if name_client:  # Якщо ім'я не порожнє
           # Відправляємо клієнту привітальне повідомлення
           connection.send(f'Вітаю {name_client} в консольному чаті!'.encode())
           # Додаємо клієнта у список у форматі [socket, ім'я]
           clients.append([connection, name_client])
   except:
       pass  # Ігноруємо помилки, що виникають при відсутності нових підключень
   # Проходимося по списку клієнтів
   for client in clients[:]:  # Копія списку для безпечного видалення
       try:
           # Отримуємо повідомлення від клієнта
           message = client[0].recv(1024).decode().strip()
           # Передаємо повідомлення всім іншим клієнтам
           for c in clients:
               if client != c:  # Не надсилаємо повідомлення тому ж клієнту, який його відправив
                   c[0].send(f'{client[1]}: {message}'.encode())
       except BlockingIOError:
           pass  # Ігноруємо помилку, яка виникає при відсутності даних у неблокуючому режимі
       except:
           # Якщо сталася помилка (ймовірно, клієнт відключився)
           print(f'Клієнт {client[1]} відключився.')
           client[0].close()  # Закриваємо сокет клієнта
           clients.remove(client)  # Видаляємо клієнта зі списку

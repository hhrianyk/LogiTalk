from socket import *  # Імпортуємо всі необхідні функції з модуля socket для роботи з мережею
import threading  # Імпортуємо модуль threading для роботи з потоками

# Створюємо клієнтський сокет (TCP/IP)
client_socket = socket(AF_INET, SOCK_STREAM)
name = input("Введіть ім'я: ")
client_socket.connect(('localhost', 12346))
client_socket.send(name.encode())
# Функція для відправлення повідомлень серверу
def send_message():
    while True:  # Безкінечний цикл для постійного введення повідомлень
        client_message = input()  # Отримуємо введене повідомлення від користувача

        # Відправляємо повідомлення серверу
        client_socket.send(client_message.encode())
# Запускаємо окремий потік для функції send_message, щоб він працював незалежно
threading.Thread(target=send_message).start()
# Основний цикл для отримання повідомлень від сервера
while True:
    try:
        # Отримуємо повідомлення від сервера (не більше 1024 байти), декодуємо та прибираємо зайві пробіли
        message = client_socket.recv(1024).decode().strip()
        # Якщо отримане повідомлення не порожнє, виводимо його у консоль
        if message:
            print(message)
    except:
        # Якщо виникла помилка (наприклад, сервер розірвав з'єднання), виходимо з циклу
        break

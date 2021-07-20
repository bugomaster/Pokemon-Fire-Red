import socket
import threading


def broadcast(msg):
    for connection in clients:
        connection.send(msg.encode())


def handle_client(c, addr):
    while True:
        try:
            msg = c.recv(1024)
        except:
            c.shutdown(socket.SHUT_RDWR)
            clients.remove(c)

            print(f"{username_lookup[c]} left")
            broadcast(f"S{str(username_lookup[c])}EL")

            break

        if msg.decode() != '':
            for connection in clients:
                if connection != c:
                    connection.send(msg)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

clients = []

s.bind((host, port))
s.listen(100)


username_lookup = {}
names = []
while True:
    c, addr = s.accept()

    username = c.recv(1024).decode()
    names.append(username)
    print(f"{username} connected")
    broadcast(f"S{username}EJ")
    c.send((f"@{names}E").encode())
    username_lookup[c] = username

    clients.append(c)

    threading.Thread(target=handle_client,
                     args=(c, addr,)).start()

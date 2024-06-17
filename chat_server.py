import socket
import threading

def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')

        if not data:
            print(f"Connection from {addr} closed.")
            break

        print(f"Received message from {addr}: {data}")

        # Broadcast the message to all connected clients
        broadcast(data, addr)

    client_socket.close()

def broadcast(message, sender_addr):
    for client in clients:
        if client != sender_addr:
            try:
                clients[client].send(message.encode('utf-8'))
            except:
                continue

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

print("Server listening on port 12345")

clients = {}

while True:
    client_socket, addr = server.accept()
    clients[addr] = client_socket

    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()

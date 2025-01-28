import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12388))

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())
        if message.lower() == 'bye':
            break
        reply = client_socket.recv(1088).decode()
        print(f"Server: {reply}")
        if reply.lower() == 'bye':
            break

    client_socket.close()

start_client()
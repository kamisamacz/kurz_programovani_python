import socket

def get_weather_response(location):
    return f"V {location} je chladno."

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12388))
    server_socket.listen()

    while True:
        print("Server waiting for connection...")
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")

        while True:
            message = client_socket.recv(1088).decode()
            if not message or message.lower() == 'bye':
                break
            print(f"Client: {message}")

            if message.lower().startswith('pocasi '):
                location = message[7:].strip()
                reply = get_weather_response(location)
            else:
                reply = input("Reply (type 'bye' to end): ")

            client_socket.sendall(reply.encode())
            if reply.lower() == 'bye':
                break

        client_socket.close()
        print("Connection closed, waiting for new participant...")

start_server()

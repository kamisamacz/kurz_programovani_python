import socket
import threading
import tkinter as tk

# Funkce pro zobrazení zpráv na serveru
def display_message(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

# Funkce pro zpracování klientů
def handle_client(client_socket, address):
    nickname = client_socket.recv(1024).decode('utf-8')
    display_message(f"{nickname} ({address[0]}:{address[1]}) se připojil k chatu.")
    broadcast(f"{nickname} se připojil k chatu!", client_socket)
    clients[client_socket] = nickname

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                display_message(f"{nickname}: {message}")
                broadcast(f"{nickname}: {message}", client_socket)
        except:
            display_message(f"{nickname} opustil chat.")
            broadcast(f"{nickname} opustil chat.", client_socket)
            clients.pop(client_socket)
            client_socket.close()
            break

# Funkce pro odeslání zprávy všem klientům
def broadcast(message, exclude_socket=None):
    for client in clients:
        if client != exclude_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.pop(client)

# Funkce pro přijetí nových klientů
def accept_clients():
    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

# Inicializace GUI serveru
root = tk.Tk()
root.title("Server Chat")

chat_frame = tk.Frame(root)
chat_frame.pack()

chat_box = tk.Text(chat_frame, state=tk.DISABLED, width=50, height=20)
chat_box.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

# Spuštění serveru
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen()

clients = {}
threading.Thread(target=accept_clients, daemon=True).start()
display_message("Server spuštěn. Čekám na připojení...")

root.mainloop()

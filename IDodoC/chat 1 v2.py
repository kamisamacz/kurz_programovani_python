import socket
import threading
import tkinter as tk
from tkinter import simpledialog

# Funkce pro příjem a zobrazení zpráv v GUI
def display_message(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

# Funkce pro zpracování klientů (serverová část)
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

# Funkce pro odeslání zprávy všem klientům (serverová část)
def broadcast(message, exclude_socket=None):
    for client in clients:
        if client != exclude_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.pop(client)

# Funkce pro přijetí nových klientů (serverová část)
def accept_clients():
    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True).start()

# Funkce pro příjem zpráv (klientská část)
def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            display_message(message)
        except:
            display_message("[DISCONNECT] Připojení ukončeno.")
            break

# Funkce pro odesílání zpráv (klientská část)
def send_message():
    message = f"{nickname}: {message_input.get()}"
    conn.send(message.encode('utf-8'))
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Já: " + message_input.get() + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    message_input.delete(0, tk.END)

# Zjištění, zda běží server
def is_server_running():
    test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        test_socket.connect(('127.0.0.1', 12345))
        test_socket.close()
        return True
    except:
        return False

# Inicializace GUI
root = tk.Tk()
root.title("Chat aplikace")

chat_frame = tk.Frame(root)
chat_frame.pack()

chat_box = tk.Text(chat_frame, state=tk.DISABLED, width=50, height=20)
chat_box.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(chat_frame, command=chat_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

message_input = tk.Entry(root, width=40)
message_input.pack()

send_button = tk.Button(root, text="Odeslat", command=send_message)
send_button.pack()

# Rozhodnutí mezi serverem a klientem
if is_server_running():
    # Připojení jako klient
    nickname = simpledialog.askstring("Připojení", "Zadejte svůj nick:", parent=root)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('127.0.0.1', 12345))
    conn.send(nickname.encode('utf-8'))

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Připojeno k serveru\n")
    chat_box.config(state=tk.DISABLED)

    # Spuštění vlákna pro příjem zpráv
    threading.Thread(target=receive_messages, daemon=True).start()
else:
    # Spuštění jako server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen()

    clients = {}
    threading.Thread(target=accept_clients, daemon=True).start()
    display_message("Server spuštěn. Čekám na připojení...")

root.mainloop()

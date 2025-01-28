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
def send_message(event=None):
    message = f"{nickname}: {message_input.get(1.0, tk.END).strip()}"
    conn.send(message.encode('utf-8'))
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Já: " + message_input.get(1.0, tk.END).strip() + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    message_input.delete(1.0, tk.END)

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

# Nastavení pozice a velikosti okna
window_width = 360
window_height = 500
window_x = 390  # Nastavení X-pozice
window_y = 10  # Nastavení Y-pozice
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

if is_server_running():
    # Zajištění dialogového okna na vrchu
    root.withdraw()  # Skryj hlavní okno do doby, než bude zadán nick
    nickname = simpledialog.askstring("Připojení", "Zadejte svůj nick:", parent=root)
    root.deiconify()  # Znovu zobraz hlavní okno po zadání nicku
    root.title(f"App2 uživatel: - {nickname}")
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('127.0.0.1', 12345))
    conn.send(nickname.encode('utf-8'))

    # Okno chatu
    chat_box_frame = tk.Frame(root)
    chat_box_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    chat_box = tk.Text(chat_box_frame, state=tk.DISABLED, height=15, wrap=tk.WORD, bg="#f9f9f9", font=("Arial", 10))
    chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(chat_box_frame, command=chat_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_box.config(yscrollcommand=scrollbar.set)

    # Pole pro zadání zprávy
    input_frame = tk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=5)

    message_input = tk.Text(input_frame, height=3, wrap=tk.WORD, font=("Arial", 10))
    message_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    message_input.bind("<Return>", lambda event: (send_message(), "break"))

    input_scrollbar = tk.Scrollbar(input_frame, command=message_input.yview)
    input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    message_input.config(yscrollcommand=input_scrollbar.set)

    # Tlačítko pro odeslání zprávy
    send_button = tk.Button(root, text="Odeslat", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 10))
    send_button.pack(pady=5)

    # Spuštění vlákna pro příjem zpráv
    threading.Thread(target=receive_messages, daemon=True).start()
else:
    # Spuštění jako server
    root.title("Chat Server")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen()

    clients = {}
    threading.Thread(target=accept_clients, daemon=True).start()

root.mainloop()

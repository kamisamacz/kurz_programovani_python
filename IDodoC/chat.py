import socket
import threading
import tkinter as tk
from tkinter import simpledialog

# Funkce pro příjem zpráv
def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            chat_box.config(state=tk.NORMAL)
            chat_box.insert(tk.END, message + "\n")
            chat_box.config(state=tk.DISABLED)
            chat_box.see(tk.END)
        except:
            print("[DISCONNECT] Připojení ukončeno.")
            break

# Funkce pro odesílání zpráv
def send_message():
    message = f"{nickname}: {message_input.get()}"
    conn.send(message.encode('utf-8'))
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Já: " + message_input.get() + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    message_input.delete(0, tk.END)

# Inicializace GUI
root = tk.Tk()
root.title("P2P Chatovací aplikace")

nickname = simpledialog.askstring("Připojení", "Zadejte svůj nick:", parent=root)

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

# Volba režimu: Hostitel nebo Klient
mode = simpledialog.askstring("Režim", "Zadejte režim (host/klient):", parent=root)

if mode.lower() == "host":
    # Hostitel: Naslouchá připojení od klienta
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(1)
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Čekám na připojení...\n")
    chat_box.config(state=tk.DISABLED)
    conn, addr = server_socket.accept()
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Klient připojen z {addr}\n")
    chat_box.config(state=tk.DISABLED)
else:
    # Klient: Připojuje se k hostiteli
    host_ip = simpledialog.askstring("Připojení", "Zadejte IP hostitele:", parent=root)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host_ip, 12345))
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Připojeno k hostiteli\n")
    chat_box.config(state=tk.DISABLED)

# Spuštění vlákna pro příjem zpráv
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

root.mainloop()

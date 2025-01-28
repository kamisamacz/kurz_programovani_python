import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Připojení k databázi
conn_db = sqlite3.connect("alltime.db")
cur = conn_db.cursor()

# Vytvoření tabulky v alltime.db (pokud neexistuje)
cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
""")
conn_db.commit()

# Funkce pro získání celé historie chatu
def get_chat_history():
    cur.execute("SELECT sender, message, timestamp FROM messages ORDER BY id ASC")
    return cur.fetchall()

# Funkce pro zobrazení historie chatu v GUI
def display_chat_history():
    chat_tree.delete(*chat_tree.get_children())  # Smazání stávajícího obsahu
    chat_history = get_chat_history()
    for row in chat_history:
        chat_tree.insert("", "end", values=row)

# Funkce pro smazání celé databáze s potvrzením
def delete_all():
    confirm_1 = messagebox.askyesno("Confirm Deletion", "Opravdu chcete smazat celou historii chatu?")
    if confirm_1:
        confirm_2 = messagebox.askyesno("Confirm Again", "Jste si opravdu jistí? Tato akce je nevratná.")
        if confirm_2:
            cur.execute("DELETE FROM messages")
            conn_db.commit()
            display_chat_history()
            messagebox.showinfo("Deletion Complete", "Všechny zprávy byly úspěšně smazány.")

# Funkce pro automatické obnovení historie chatu a odpočtu
def auto_refresh(countdown=15):
    if countdown > 0:
        countdown_label.config(text=f"Obnova za: {countdown} s")
        root.after(1000, auto_refresh, countdown - 1)
    else:
        display_chat_history()
        auto_refresh(15)

# Inicializace GUI aplikace
root = tk.Tk()

# Nastavení pozice a velikosti okna
window_width = 600
window_height = 1010
window_x = 1137
window_y = 10
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.title("Chat History Viewer")

# Horní rám pro tlačítka a odpočet
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, pady=10)

countdown_label = tk.Label(top_frame, text="", font=("Arial", 12))
countdown_label.pack(side=tk.LEFT, padx=10)

refresh_button = tk.Button(top_frame, text="Refresh Now", command=display_chat_history, width=15, font=("Arial", 10))
refresh_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(top_frame, text="Delete All", command=delete_all, width=15, font=("Arial", 10), bg="#f44336", fg="white")
delete_button.pack(side=tk.RIGHT, padx=10)

# Dolní rám pro stromovou tabulku
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.BOTH, expand=True)

columns = ("Sender", "Message", "Timestamp")
chat_tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

for col in columns:
    chat_tree.heading(col, text=col)
    chat_tree.column(col, anchor=tk.CENTER, width=200)

chat_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Přidání svislého posuvníku
scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=chat_tree.yview)
chat_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Spuštění automatického obnovení historie chatu
auto_refresh()

root.mainloop()

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Připojení k databázím
conn_db = sqlite3.connect("history.db")
cur = conn_db.cursor()

conn_alltime = sqlite3.connect("alltime.db")
cur_alltime = conn_alltime.cursor()

# Vytvoření tabulek, pokud neexistují
cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
""")
conn_db.commit()

cur_alltime.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL
);
""")
conn_alltime.commit()


# Funkce pro zálohování dat z `history.db` do `alltime.db`
def backup_to_alltime():
    cur.execute("SELECT sender, message, timestamp FROM messages")
    messages = cur.fetchall()
    cur_alltime.executemany("INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)", messages)
    conn_alltime.commit()


# Funkce pro získání statistik z databáze
def get_statistics():
    cur.execute("""
    SELECT sender, COUNT(*) AS message_count, SUM(LENGTH(message)) AS total_characters, MAX(timestamp) AS last_message_time
    FROM messages
    GROUP BY sender
    """)
    return cur.fetchall()


# Funkce pro zobrazení statistik v GUI
def display_statistics():
    # Záloha dat při každém načtení statistik
    backup_to_alltime()

    stats_tree.delete(*stats_tree.get_children())
    stats = get_statistics()
    for i, (sender, message_count, total_characters, last_message_time) in enumerate(stats):
        stats_tree.insert("", "end", values=(sender, message_count, total_characters, last_message_time))


# Funkce pro resetování databáze
def reset_database():
    # Přesun dat z `history.db` do `alltime.db`
    backup_to_alltime()

    # Vymazání dat z `history.db`
    cur.execute("DELETE FROM messages")
    conn_db.commit()

    # Aktualizace GUI
    stats_tree.delete(*stats_tree.get_children())
    messagebox.showinfo("Reset Database", "Database has been reset and data moved to alltime.db.")


# Funkce pro automatické obnovení statistik a zobrazení odpočtu
def auto_refresh(countdown=15):
    if countdown > 0:
        countdown_label.config(text=f"Obnova za: {countdown} s")
        root.after(1000, auto_refresh, countdown - 1)
    else:
        display_statistics()
        auto_refresh(15)


# Inicializace GUI aplikace
root = tk.Tk()

# Nastavení pozice a velikosti okna
window_width = 650
window_height = 470
window_x = 480  # Nastavení X-pozice
window_y = 550  # Nastavení Y-pozice
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
root.title("Chat Statistics")

# Horní rám pro tlačítka a odpočet
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, pady=10)

refresh_button = tk.Button(top_frame, text="Load Statistics", command=display_statistics, width=20)
refresh_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(top_frame, text="Reset Database", command=reset_database, width=20)
reset_button.pack(side=tk.RIGHT, padx=10)

countdown_label = tk.Label(top_frame, text="")
countdown_label.pack(side=tk.BOTTOM, pady=5)

# Dolní rám pro stromovou tabulku
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.BOTH, expand=True)

columns = ("Sender", "Message Count", "Total Characters", "Last Message Time")
stats_tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")

for col in columns:
    stats_tree.heading(col, text=col)
    stats_tree.column(col, anchor=tk.CENTER, width=150)

stats_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Přidání svislého posuvníku
scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=stats_tree.yview)
stats_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Spuštění automatického obnovení statistik
auto_refresh()

root.mainloop()

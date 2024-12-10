import time

# Fronty podle priorit: vysoka (2), stredni (1), nizka (0)
queues = {2: [], 1: [], 0: []}

# Seznam pro ukladani statistik
statistics = []


def add_request(user, priority):
    """Prida pozadavek do fronty podle priority."""
    if priority not in queues:
        print("Neplatna priorita! Pouzijte 0 (nizka), 1 (stredni) nebo 2 (vysoka).")
        return
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    queues[priority].append(user)
    statistics.append({"user": user, "time": timestamp, "priority": priority})
    print(f"Pozadavek od uzivatele '{user}' pridan do fronty s prioritou {priority}.")


def process_request():
    """Zpracuje pozadavek z fronty s nejvyssi prioritou."""
    for priority in sorted(queues.keys(), reverse=True):
        if queues[priority]:
            user = queues[priority].pop(0)
            print(f"Zpracovava se pozadavek od uzivatele '{user}' s prioritou {priority}.")
            return
    print("Zadne pozadavky ve fronte.")


def show_statistics():
    """Zobrazi vsechny statistiky pozadavku."""
    print("\n=== Statistiky pozadavku ===")
    for record in statistics:
        print(f"Uzivatel: {record['user']}, Cas: {record['time']}, Priorita: {record['priority']}")
    print("============================")


# Hlavni smycka programu
while True:
    print("\n--- Server Request Queue ---")
    print("1. Pridat pozadavek")
    print("2. Zpracovat pozadavek")
    print("3. Zobrazit statistiky")
    print("4. Konec")

    choice = input("Vyberte akci: ")
    if choice == "1":
        user = input("Zadejte jmeno uzivatele: ")
        priority = int(input("Zadejte prioritu (0 = nizka, 1 = stredni, 2 = vysoka): "))
        add_request(user, priority)
    elif choice == "2":
        process_request()
    elif choice == "3":
        show_statistics()
    elif choice == "4":
        print("Konec programu.")
        break
    else:
        print("Neplatna volba, zkuste to znovu.")

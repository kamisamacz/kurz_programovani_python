# seznam uzivatelu
users = {}


def add_user():
    name = input("zadej jmeno a prijmeni: ")
    height = int(input("zadej vysku noveho uzivatele (v cm): "))
    users[name] = {'height': height}
    print(f"hrac {name} s vyskou {height} cm byl pridan.")

    # Otevřete soubor v režimu "a" pro připojení dat na konec souboru
    with open("databazehracu.txt", "a") as f:
        f.write(f"{name}, {height}\n")

def edit_user():
    display_users()
    name = input("Zadejte jméno hrace, pro editaci: ")
    if name in users:
        # zmena jmena
        new_name = input("zadejte jmeno (blank pro ponechani): ")
        if new_name:
            # akt. edit.
            users[new_name] = users.pop(name)
            name = new_name  # update jmena

        # zmena vysky
        height = int(input("Zadejte novou výšku uživatele (v cm): "))
        users[name]['height'] = height
        print(f"udaje hrace byly aktualizovany: Jméeo - {name}, vyska - {height} cm.")
    else:
        print("spatne jmeno.")


def display_users():
    """if users:
        print()
        print("soupiska hracu:")
        for name, data in users.items():
            print(f"jmeno: {name}, vyska: {data['height']} cm")



    else:
        print()
        print("zatím nikdo nebyl pridan")"""

    with open("databazehracu.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")


def display_users_nej():
    if users:
        print("\nsoupiska hracu (od longra po prcky):")
        # lambda
        sorted_users = sorted(users.items(), key=lambda x: x[1]['height'], reverse=True)

        for name, data in sorted_users:
            print(f"jmeno: {name}, vyska: {data['height']} cm")
    else:
        print("\nnikdo dnes nehraje.")


def menu():
    while True:
        print("\nMenu:")
        print("1. add hrac")
        print("2. edit hrace")
        print("3. soupiska hracu")
        print("4. pro nej longra")
        print("5. pro konec app")

        choice = input("vyber (1-4): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            edit_user()
        elif choice == '3':
            display_users()
        elif choice == '4':
            display_users_nej()
        elif choice == '5':
            print("neplecha ukoncena.")
            break
        else:
            print("one more time bro.")


# Spuštění menu
menu()

import json

def ulozit_objednavku(objednavka):
    print("Ukládám objednávku do souboru...")
    try:
        with open('data/orders.json', 'a') as f:
            json.dump(objednavka, f)
            f.write('\n')
        print("Objednávka uložena.")
    except Exception as e:
        print(f"Chyba při ukládání objednávky: {e}")

def nacist_objednavky():
    print("Načítám objednávky ze souboru...")
    try:
        with open('data/orders.json', 'r') as f:
            objednavky = []
            for line in f:
                objednavky.append(json.loads(line))
        print("Objednávky načteny.")
        return objednavky
    except FileNotFoundError:
        print("Soubor s objednávkami neexistuje.")
        return []
    except Exception as e:
        print(f"Chyba při načítání objednávek: {e}")
        return []
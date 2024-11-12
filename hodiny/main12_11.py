FILE_PATH = "test.ca0"
FILE_PATH4 = "vetsi.4"

zdroj = input("zadej slovo")
if len(zdroj) > 4:
    with open(FILE_PATH, "a") as f:
        f.write(f"{zdroj}\n")

# Výpis souboru test:
print("Výpis souboru test:")
print()

# Otevření souboru pro čtení a vypsání jeho obsahu
with open(FILE_PATH, "r") as f:
    data = f.read()

print(data)

print("\nZkopírování slov delších než 4:")

# Otevření souboru pro čtení
with open(FILE_PATH, "r") as f:
    lines = f.readlines()

# Iterace přes každý řádek a zpracování jednotlivých slov
for line in lines:
    words = line.split()  # Splitnutí řádku na jednotlivá slova
    for word in words:
        if len(word) > 4:  # Kontrola, zda je slovo delší než 4 znaky
            with open(FILE_PATH4, "a") as f:
                f.write(f"{word}\n")  # Zapsání slova do souboru

# Čtení a výpis souboru FILE_PATH4
with open(FILE_PATH4, "r") as f:
    data4 = f.read()

print("\nData zkopírovaná do souboru 'vetsi.4':")
print(data4)

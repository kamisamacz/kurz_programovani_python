print("Zadej postupne dve cisla u kterych chces zjistit nejvetsi spolecny delitel.")
print("prvni cislo?:")
a = int(input())
print("druhe cislo?:")
b = int(input())
def nsd(a, b):
    if b == 0:
        print(f"Prubeh rekurze: {a}/{b} = {a}")
        return a  # end nsd
    else:
        print(f"Prubeh rekurze: {a}/{b} = {a % b}")
        return nsd(b, a % b)  # rekurze


vysledek = nsd(a, b)
print(f"Výsledek, tedy největší společný dělitel je: {vysledek}")
#clovicku pokud jsi dosel az jsem tak mrkni
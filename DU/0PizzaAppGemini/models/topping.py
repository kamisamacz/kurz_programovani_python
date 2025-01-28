class Topping:
    def __init__(self, nazev, cena):
        print(f"Vytvářím topping {nazev}...")
        self.nazev = nazev
        self.cena = cena

    def __str__(self):
        return f"{self.nazev} ({self.cena} Kč)"
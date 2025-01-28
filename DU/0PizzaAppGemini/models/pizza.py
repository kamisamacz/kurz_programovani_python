class Pizza:
    def __init__(self, nazev, cena, ingredience):
        print(f"Vytvářím pizzu {nazev}...")
        self.nazev = nazev
        self.cena = cena
        self.ingredience = ingredience

    def __str__(self):
        return f"{self.nazev} ({self.cena} Kč): {', '.join(self.ingredience)}"
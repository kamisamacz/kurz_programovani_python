class Payment:
    def __init__(self, typ_platby, castka):
        print("Vytvářím novou platbu...")
        self.typ_platby = typ_platby
        self.castka = castka

    def __str__(self):
        return f"Platba: {self.typ_platby}, {self.castka} Kč"
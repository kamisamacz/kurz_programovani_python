class Sales:
    def __init__(self, datum, trzby):
        print(f"Vytvářím záznam tržeb pro {datum}...")
        self.datum = datum
        self.trzby = trzby

    def __str__(self):
        return f"Tržby za {self.datum}: {self.trzby} Kč"
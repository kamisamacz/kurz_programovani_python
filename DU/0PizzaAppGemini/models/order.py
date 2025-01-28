import datetime

class Order:
    def __init__(self, velikost, adresa, salami, pepperoni,  # ... další náplně ...
                 cas_objednavky=None):
        print("Vytvářím novou objednávku...")
        self.velikost = velikost
        self.adresa = adresa
        self.salami = salami
        self.pepperoni = pepperoni
        # ... inicializace dalších náplní ...
        self.cas_objednavky = cas_objednavky or datetime.datetime.now()

    def __str__(self):
        return f"Objednávka z {self.cas_objednavky}: {self.velikost}, {self.adresa}, " \
               f"salami={self.salami}, pepperoni={self.pepperoni}"  # ... další náplně ...

    def to_dict(self):
        return {
            "velikost": self.velikost,
            "adresa": self.adresa,
            "salami": self.salami,
            "pepperoni": self.pepperoni,
            # ... další náplně ...
            "cas_objednavky": self.cas_objednavky.strftime("%Y-%m-%d %H:%M:%S")
        }import datetime

class Order:
    def __init__(self, velikost, adresa, salami, pepperoni,  # ... další náplně ...
                 cas_objednavky=None):
        print("Vytvářím novou objednávku...")
        self.velikost = velikost
        self.adresa = adresa
        self.salami = salami
        self.pepperoni = pepperoni
        # ... inicializace dalších náplní ...
        self.cas_objednavky = cas_objednavky or datetime.datetime.now()

    def __str__(self):
        return f"Objednávka z {self.cas_objednavky}: {self.velikost}, {self.adresa}, " \
               f"salami={self.salami}, pepperoni={self.pepperoni}"  # ... další náplně ...

    def to_dict(self):
        return {
            "velikost": self.velikost,
            "adresa": self.adresa,
            "salami": self.salami,
            "pepperoni": self.pepperoni,
            # ... další náplně ...
            "cas_objednavky": self.cas_objednavky.strftime("%Y-%m-%d %H:%M:%S")
        }
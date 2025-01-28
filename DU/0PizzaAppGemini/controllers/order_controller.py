from models.order import Order
from utils import ulozit_objednavku

class OrderController:
    def __init__(self):
        print("Vytvářím OrderController...")

    def zpracovat_objednavku(self, velikost, adresa, salami, pepperoni,  # ... další náplně ...
                            ):
        print("Zpracovávám objednávku...")
        objednavka = Order(velikost, adresa, salami, pepperoni,  # ... další náplně ...
                          )
        ulozit_objednavku(objednavka.to_dict())
        # Zde můžete přidat další logiku, například:
        # - výpočet ceny objednávky
        # - generování ID objednávky
        # - odeslání emailu s potvrzením objednávky
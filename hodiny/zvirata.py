class Animal:
    def __init__(self, druh):
        self.druh = druh

    def sayhello(self):
        print(f"Ahoj, já jsem {self.druh}")

class H_animal(Animal):
    def __init__(self, druh, name):
        # Inicializace základní třídy pomocí `super()`
        super().__init__(druh)
        self.name = name

    def name_info(self):
        print(f"Jmenuji se {self.name} a jsem {self.druh}")

# Vytvoření instance H_animal
w1 = H_animal("prase", "Toník")
w2 = H_animal("Pes", "Rollo")
# Volání metod
w1.sayhello()
w1.name_info()
w2.sayhello()
w2.name_info()
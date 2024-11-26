# zarizeni
class Zarizeni:
    def __init__(self, nazev, vyrobce, vykon):
        self.nazev = nazev
        self.vyrobce = vyrobce
        self.vykon = vykon  #v W

    def zapnout(self):
        print(f"{self.nazev} od výrobce {self.vyrobce} je zapnuto.")

    def vypnout(self):
        print(f"{self.nazev} od výrobce {self.vyrobce} je vypnuto.")

    def informace(self):
        print(f"Zařízení: {self.nazev}, Výrobce: {self.vyrobce}, Výkon: {self.vykon} W")

# (Kávovar)
class Kavovar(Zarizeni):
    def __init__(self, nazev, vyrobce, vykon, pocet_poharu):
        super().__init__(nazev, vyrobce, vykon)
        self.pocet_poharu = pocet_poharu  #pocet salku

    def priprav_kavu(self):
        print(f"{self.nazev} připravuje {self.pocet_poharu} pohárů kávy.")

# mixer
class Mix(Zarizeni):
    def __init__(self, nazev, vyrobce, vykon, objem):
        super().__init__(nazev, vyrobce, vykon)
        self.objem = objem  # objem
    def mixuj(self):
        print(f"{self.nazev} mixuje. Objem nádoby: {self.objem} l.")

# mlynek maso
class Mlynek(Zarizeni):
    def __init__(self, nazev, vyrobce, vykon, druhy_mleti):
        super().__init__(nazev, vyrobce, vykon)
        self.druhy_mleti = druhy_mleti  # seznam nastaveni

    def mlec_maso(self, druh):
        if druh in self.druhy_mleti:
            print(f"{self.nazev} mele maso na způsob: {druh}.")
        else:
            print(f"{self.nazev} neumí mlít maso na způsob: {druh}.")


#v provozu
# set
kavovar = Kavovar("Espresso Max", "DeLonghi", 1450, 2)
mixer = Mix("Smoothie xxl", "Philips", 800, 1.5)
mlynek = Mlynek("Pomelu i nohu", "Diepotato", 1200, ["jemné", "hrubé", "střední"])



kavovar.informace()
kavovar.zapnout()
kavovar.priprav_kavu()
kavovar.vypnout()


mixer.informace()
mixer.zapnout()
mixer.mixuj()
mixer.vypnout()


mlynek.informace()
mlynek.zapnout()
mlynek.mlec_maso("jemné")
mlynek.mlec_maso("velmi jemné")  # Tento způsob mletí není dostupný
mlynek.vypnout()


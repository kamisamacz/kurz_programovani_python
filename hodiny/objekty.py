class people:
    def __init__(self,jmeno, vyska, vaha, vek, stav):
        self.jmeno = jmeno
        self.vyska = vyska
        self.vaha = vaha
        self.vek = vek
        self.stav = stav

    def rande(self):
        self.stav = "zadany"
        print(f"{self.jmeno} sel na rande a je {self.stav}")
        print()

    def nerande(self):
        self.stav = "po rozschodu"
        print(f"{self.jmeno} mel s ni problem, a je {self.stav}")
        print()

patrik = people("Patrik",169, 98, 34, "nezadany")

print("Patrik:")
print(patrik.vyska, " ",patrik.vaha, "",patrik.vek, "",patrik.stav)

patrik.rande()
print("Patrik:")
print(patrik.vyska, " ",patrik.vaha, "",patrik.vek, "",patrik.stav)
patrik.nerande()
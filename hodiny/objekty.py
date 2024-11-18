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
    def stari(self):
        self.vek = self.vek * 2
patrik = people("Patrik",169, 98, 34, "nezadany")
magda = people("Magda",169, 58, 20, "nezadany")

print("Patrik:")
print(patrik.vyska, " ",patrik.vaha, "",patrik.vek, "",patrik.stav)

patrik.rande()
print("Patrik:")
print(patrik.vyska, " ",patrik.vaha, "",patrik.vek, "",patrik.stav)
patrik.nerande()
if patrik.stav == magda.stav:
    jebacka = magda.vaha + patrik.vaha
    print("splnili podminku por jebacku")

else:
    print("nejebalo se")

a = patrik.vek + patrik.vek

print("dvojnasobny vek bude: ",a)
magda.rande()
patrik.rande()
if patrik.stav == magda.stav:
    jebacka = magda.vaha + patrik.vaha
    print("splnili podminku por jebacku")

else:
    print("nejebalo se")
print("patrikova postel unesla: ", jebacka)
rozdil = abs(patrik.vek - magda.vek)
print("veky rozdil je:",rozdil)
if rozdil >10:
    print("najdi si uz sratsi vole")
magda.patrik.rande()
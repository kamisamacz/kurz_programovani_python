#objekty a dedicnost
class Human:
    def __init__(self,name):
        self.name = name

    def sayhello(self):
        print(f"Ahoj, ja jsem {self.name}")


class Worker(Human):
    def __init__(self, name, position):
        Human.__init__(self, name)
        self.position = position

    def say_pos(self):
        print(f"praciji na pozici {self.position}")

w1 = Worker("PATRIK","skolnik")

w1.sayhello()
w1.say_pos()
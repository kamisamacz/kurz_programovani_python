#objekty a dedicnost
class Human:
    def __init__(self,name):
        self.name = name

        def sayhello(self):
            print(f"Ahoj, ja jsem {self.name}")


class Worker(human):
    def __init__(self, name, position):
        Human.__init__(self, name)
        self.position = position

        def say_pos(self)
            print(f"praciji na pozici {self.position}")

w1 = Worker("PTRIK")
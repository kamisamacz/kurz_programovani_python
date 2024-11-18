"""Implementujte tridu Car. V polich tridy by mely byt ulozeny nasledujici udaje:
model, rok vydani, vyrobce, objem motoru, barva, cena.
Implementujte metody tridy pro vstup a vystup dat,
zajistete pristup k jednotlivym polim prostrednictvim metod tridy."""


class Car:
    def __init__(self, model=None, year=None, manufacturer=None, engine_capacity=None, color=None, price=None):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Zapis model: ")
        self.year = int(input("Zapis rok vyroby: "))
        self.manufacturer = input("Zapis vyrobce: ")
        self.engine_capacity = int(input("Objem motoru (ccm): "))
        self.color = input("Zapis barvu: ")
        self.price = float(input("Zapis cenu: "))

    def display_data(self):
        print(f"Model: {self.model}")
        print(f"Rok vydani: {self.year}")
        print(f"Vyrobce: {self.manufacturer}")
        print(f"Objem motoru: {self.engine_capacity} ccm")
        print(f"Barva: {self.color}")
        print(f"Cena: {self.price:.2f} Kc")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year


# Funkce pro menu
def menu():
    cars = []

    while True:
        print("\n--- Menu aut ---")
        print("1. Pridat auto")
        print("2. Seznam aut")
        print("3. Editace auta")
        print("4. Konec")

        choice = input("Zvol (1-4): ")

        if choice == "1":
            print("\nPridani noveho auta...")
            car = Car()
            car.input_data()
            cars.append(car)
            print("Auto bylo uspesne pridano!")

        elif choice == "2":
            if not cars:
                print("\nNejsou zapsana zadna auta.")
            else:
                print("\nSeznam aut:")
                for idx, car in enumerate(cars, start=1):
                    print(f"\nAuto #{idx}:")
                    car.display_data()

        elif choice == "3":
            if not cars:
                print("\nNejsou dostupna zadna auta k editaci.")
            else:
                print("\nSeznam aut:")
                for idx, car in enumerate(cars, start=1):
                    print(f"{idx}. {car.get_model()} ({car.get_year()})")

                try:
                    car_index = int(input("\nZadej cislo auta k editaci: ")) - 1
                    if 0 <= car_index < len(cars):
                        print("\nUprava detailu auta...")
                        cars[car_index].input_data()
                        print("Detaily auta byly uspesne aktualizovany!")
                    else:
                        print("Neplatne cislo auta!")
                except ValueError:
                    print("Zadej prosim platne cislo!")

        elif choice == "4":
            print("Ukoncuji program. Nashledanou!")
            break

        else:
            print("Neplatna volba! Vyber cislo mezi 1-4.")


# Spusteni aplikace
if __name__ == "__main__":
    menu()

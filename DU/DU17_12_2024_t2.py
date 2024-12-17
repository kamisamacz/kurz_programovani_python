import json
import pickle

class Car:
    def __init__(self, brand, model, year, mileage):
        # Nastaveni zakladnich vlastnosti auta
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def to_json(self):
        # Prevede objekt auta na JSON
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        # Vytvori auto z JSON dat
        data = json.loads(json_data)
        return cls(data['brand'], data['model'], data['year'], data['mileage'])

    def to_pickle(self):
        # Prevede auto na Pickle (binarni data)
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        # Vytvori auto z Pickle dat
        return pickle.loads(pickle_data)

    def __str__(self):
        # Vrati popis auta, aby se dal hezky vypsat
        return f"{self.brand} {self.model} ({self.year}) - {self.mileage} km"


# Tady ukazu, jak to funguje
if __name__ == "__main__":
    # Vytvoreni noveho auta

    car = Car("Skoda", "120", 1975, 150000)


    # Ulozeni do JSON
    json_data = car.to_json()
    print("Ulozeno do JSON:", json_data)
    new_car_from_json = Car.from_json(json_data)
    print("Nacteno z JSON:", new_car_from_json)

    # Ulozeni do Pickle
    pickle_data = car.to_pickle()
    print("Ulozeno do Pickle:", pickle_data)
    new_car_from_pickle = Car.from_pickle(pickle_data)
    print("Nacteno z Pickle:", new_car_from_pickle)

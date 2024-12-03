# dek pro zaokrouhleni
def round_values(func):
    def wrapper(data):
        print("Zaokrouhleno na tisice...")
        for record in data:
            record["Prijmy"] = round(record["Prijmy"], -3)
            record["Vydaje"] = round(record["Vydaje"], -3)
            record["Zisk"] = round(record["Zisk"], -3)
        return func(data)
    return wrapper

# Dekorator pro %
def calculate_profit_percentage(func):
    def wrapper(data):
        print("Pridavam % zisk...")
        for record in data:
            prijmy = record["Prijmy"]
            zisk = record["Zisk"]
            record["ZiskProcenta"] = round((zisk / prijmy) * 100, 2) if prijmy else 0
        return func(data)
    return wrapper

# fce pro dekoraci
@round_values
@calculate_profit_percentage
def display_financial_statements(data):
    print("Zdekorovana financni data:")
    for record in data:
        print(record)

# data
financial_data = [
    {"Rok": 2023, "Prijmy": 123456, "Vydaje": 98765, "Zisk": 24691},
    {"Rok": 2024, "Prijmy": 654321, "Vydaje": 654321, "Zisk": 0},
    {"Rok": 2025, "Prijmy": 789012, "Vydaje": 456789, "Zisk": 332223},
]

# start
print("Neupraveno:")
print(financial_data)
print()
print("Upraveno:")
display_financial_statements(financial_data)

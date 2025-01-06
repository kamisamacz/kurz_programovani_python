class Pizza:
    def __init__(self, name, size, price, ingredients=None):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients if ingredients else []

    def __str__(self):
        return f"{self.size} {self.name} Pizza - {self.price} Kč\nIngredients: {', '.join(self.ingredients)}"

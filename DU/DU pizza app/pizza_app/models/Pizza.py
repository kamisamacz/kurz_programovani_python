class Pizza:
    def __init__(self, name, size, price, ingredients=None):
        """
        Vytvoření instance pizzy.
        :param name: Název pizzy.
        :param size: Velikost pizzy (např. "Small", "Medium", "Large").
        :param price: Cena pizzy.
        :param ingredients: Seznam ingrediencí (výchozí prázdný seznam).
        """
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients if ingredients else []

    def add_ingredient(self, ingredient):
        """Přidá ingredienci k pizze."""
        self.ingredients.append(ingredient)

    def __str__(self):
        """Vrací textovou reprezentaci pizzy."""
        return f"{self.size} {self.name} Pizza - {self.price} Kč\nIngredients: {', '.join(self.ingredients)}"

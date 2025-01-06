class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizzas = []
        self.total_price = 0

    def add_pizza(self, pizza):
        """Přidá pizzu do objednávky a aktualizuje celkovou cenu."""
        self.pizzas.append(pizza)
        self.total_price += pizza['price']  # Cena by měla být součástí objektu pizza.

    def __str__(self):
        """Vrátí textovou reprezentaci objednávky."""
        pizzas_str = '\n'.join([f"- {pizza['name']} ({pizza['ingredients']})" for pizza in self.pizzas])
        return f"Objednávka pro: {self.customer_name}\n{pizzas_str}\nCelková cena: {self.total_price} Kč"

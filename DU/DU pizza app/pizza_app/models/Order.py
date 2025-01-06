class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.pizzas = []
        self.total_price = 0

    def add_pizza(self, pizza):
        """Přidá pizzu do objednávky a aktualizuje celkovou cenu."""
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def remove_pizza(self, pizza_name):
        """Odstraní pizzu z objednávky podle jejího názvu."""
        for pizza in self.pizzas:
            if pizza.name == pizza_name:
                self.pizzas.remove(pizza)
                self.total_price -= pizza.price
                break

    def __str__(self):
        """Vrací textovou reprezentaci objednávky."""
        pizzas_str = '\n'.join([str(pizza) for pizza in self.pizzas])
        return f"Order for {self.customer_name}:\n{pizzas_str}\nTotal Price: {self.total_price} Kč"

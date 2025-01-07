from pizza_app.models.Order import Order

class UserController:
    def __init__(self, shared_data):
        self.shared_data = shared_data

    def create_order(self, name, base, extras):
        if not name.strip():
            print("Chyba: Jméno nesmí být prázdné.")
            return
        order = Order(name=name, base=base, extras=extras)
        self.shared_data.save_order(order)
        print(f"Objednávka vytvořena: {order}")

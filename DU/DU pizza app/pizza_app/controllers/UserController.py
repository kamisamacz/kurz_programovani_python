class UserController:
    def __init__(self, view):
        self.view = view
        self.orders = []
        print("Inicializuji UserController...")
        self.view.start_button.bind(on_press=self.start_order)

    def start_order(self, instance):
        """Zahájí proces objednávky."""
        print("Kliknuto na tlačítko 'Vytvořit objednávku'.")
        self.view.show_order_form(self.create_order)

    def create_order(self, instance):
        """Vytvoří objednávku pizzy."""
        base = "Pomodoro" if self.view.base_pomodoro.active else "Smetanový"
        extras = []
        if self.view.extra_cheese.active:
            extras.append("extra sýr")
        if self.view.extra_ham.active:
            extras.append("extra šunka")

        order = f"Pizza Hawaii ({base}, {', '.join(extras) or 'bez přídavků'})"
        self.orders.append(order)
        print(f"Vytvořená objednávka: {order}")
        self.view.show_order_list(self.orders, self.start_order)

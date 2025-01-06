from pizza_app.models.SharedData import SharedData

class AdminController:
    def __init__(self, view):
        self.view = view
        self.update_orders()

    def update_orders(self):
        """Načte objednávky ze sdílených dat."""
        orders = SharedData.get_orders()
        self.view.update_order_list(orders)

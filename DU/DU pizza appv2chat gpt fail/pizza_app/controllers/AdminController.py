from pizza_app.models.OrderStorage import OrderStorage

class AdminController:
    @staticmethod
    def add_time_to_order(order_id):
        orders = OrderStorage.load_orders()
        for order in orders:
            if order["id"] == order_id:
                order["status"] = "Extra Time Added"
                print(f"Přidán čas k objednávce {order_id}")
        OrderStorage.save_orders(orders)

    @staticmethod
    def cancel_order(order_id):
        orders = OrderStorage.load_orders()
        for order in orders:
            if order["id"] == order_id:
                order["status"] = "Cancelled"
                print(f"Objednávka {order_id} zrušena.")
        OrderStorage.save_orders(orders)

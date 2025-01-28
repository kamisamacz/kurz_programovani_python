from pizza_app.models.OrderStorage import OrderStorage

class WorkerController:
    @staticmethod
    def mark_order_as_done(order_id):
        orders = OrderStorage.load_orders()
        for order in orders:
            if order["id"] == order_id:
                order["status"] = "Completed"
                print(f"Objednávka {order_id} označena jako hotová.")
        OrderStorage.save_orders(orders)

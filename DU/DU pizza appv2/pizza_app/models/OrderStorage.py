
import json
from threading import Lock

class OrderStorage:
    _file_path = "orders.json"
    _lock = Lock()

    @staticmethod
    def load_orders():
        """Load orders from the JSON file."""
        with OrderStorage._lock:
            try:
                with open(OrderStorage._file_path, "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_orders(orders):
        """Save orders to the JSON file."""
        with OrderStorage._lock:
            with open(OrderStorage._file_path, "w") as file:
                json.dump(orders, file, indent=4)

    @staticmethod
    def add_order(order):
        """Add a new order and save it."""
        with OrderStorage._lock:
            orders = OrderStorage.load_orders()
            orders.append(order)
            OrderStorage.save_orders(orders)

    @staticmethod
    def update_order(order_id, update_data):
        """Update an order by its ID."""
        with OrderStorage._lock:
            orders = OrderStorage.load_orders()
            for order in orders:
                if order["id"] == order_id:
                    order.update(update_data)
            OrderStorage.save_orders(orders)

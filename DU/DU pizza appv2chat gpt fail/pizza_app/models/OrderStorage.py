import json
import os
from threading import Lock

class OrderStorage:
    _file_path = "orders.json"
    _lock = Lock()

    @staticmethod
    def load_orders():
        with OrderStorage._lock:
            try:
                if not os.path.exists(OrderStorage._file_path):
                    print(f"[ORDER STORAGE] No file found at {OrderStorage._file_path}. Creating new.")
                    return []
                with open(OrderStorage._file_path, "r") as file:
                    print(f"[ORDER STORAGE] Loading orders from {OrderStorage._file_path}.")
                    return json.load(file)
            except Exception as e:
                print(f"[ORDER STORAGE] Error loading orders: {e}")
                return []

    @staticmethod
    def save_orders(orders):
        with OrderStorage._lock:
            with open(OrderStorage._file_path, "w") as file:
                json.dump(orders, file, indent=4)
                print(f"[ORDER STORAGE] Orders saved to {OrderStorage._file_path}.")

    @staticmethod
    def add_order(order):
        with OrderStorage._lock:
            orders = OrderStorage.load_orders()
            orders.append(order)
            OrderStorage.save_orders(orders)
            print(f"[ORDER STORAGE] Order added: {order}")

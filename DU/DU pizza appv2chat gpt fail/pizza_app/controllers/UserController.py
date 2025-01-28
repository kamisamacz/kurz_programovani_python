from pizza_app.models.OrderStorage import OrderStorage
from pizza_app.models.Order import Order
from datetime import datetime
import uuid

class UserController:
    @staticmethod
    def create_order(pizza, extras, payment_method):
        order_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order = Order(
            id=order_id,
            pizza=pizza,
            extras=extras,
            payment_method=payment_method,
            timestamp=timestamp
        )
        OrderStorage.add_order(order.to_dict())
        print(f"Vytvořena objednávka: {order.to_dict()}")
        return order_id

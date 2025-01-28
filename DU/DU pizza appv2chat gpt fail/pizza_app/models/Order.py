class Order:
    def __init__(self, id, pizza, extras, payment_method, timestamp, status="Pending"):
        self.id = id
        self.pizza = pizza
        self.extras = extras
        self.payment_method = payment_method
        self.timestamp = timestamp
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "pizza": self.pizza,
            "extras": self.extras,
            "payment_method": self.payment_method,
            "timestamp": self.timestamp,
            "status": self.status
        }

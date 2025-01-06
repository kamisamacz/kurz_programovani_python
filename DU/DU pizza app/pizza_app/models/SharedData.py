class SharedData:
    orders = []  # Sdílený seznam objednávek

    @classmethod
    def add_order(cls, order):
        cls.orders.append(order)

    @classmethod
    def get_orders(cls):
        return cls.orders

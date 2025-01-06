class Sales:
    _instance = None  # Singleton instance

    def __new__(cls):
        """Zajištění, že existuje pouze jedna instance třídy Sales."""
        if cls._instance is None:
            cls._instance = super(Sales, cls).__new__(cls)
            cls._instance.total_sales = 0
            cls._instance.orders = []
        return cls._instance

    def add_order(self, order):
        """Přidá objednávku do seznamu a aktualizuje celkové tržby."""
        self.orders.append(order)
        self.total_sales += order.total_price

    def get_sales_summary(self):
        """Vrací textový přehled prodejů."""
        return f"Total Sales: {self.total_sales} Kč\nOrders Processed: {len(self.orders)}"

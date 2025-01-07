from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from pizza_app.models.OrderStorage import OrderStorage


class AdminView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.orders_list = BoxLayout(orientation="vertical", size_hint_y=None)
        self.orders_list.bind(minimum_height=self.orders_list.setter("height"))

        scroll_view = ScrollView(size_hint=(1, None), height=500)
        scroll_view.add_widget(self.orders_list)
        self.add_widget(scroll_view)

        self.refresh_button = Button(
            text="Aktualizovat seznam", size_hint=(1, 0.1), on_press=self.update_orders
        )
        self.add_widget(self.refresh_button)

        self.update_orders()

    def update_orders(self, *args):
        self.orders_list.clear_widgets()
        orders = OrderStorage.load_orders()

        for order in orders:
            if not order.get("completed") and not order.get("canceled"):
                order_box = BoxLayout(size_hint_y=None, height=50)

                order_details = Label(
                    text=f"Objednávka: {order['pizza']} ({order['payment']})",
                    size_hint_x=0.6,
                )
                extend_button = Button(
                    text="Přidat 5 min",
                    size_hint_x=0.2,
                    on_press=lambda btn, oid=order["id"]: self.extend_time(oid),
                )
                cancel_button = Button(
                    text="Zrušit",
                    size_hint_x=0.2,
                    on_press=lambda btn, oid=order["id"]: self.cancel_order(oid),
                )

                order_box.add_widget(order_details)
                order_box.add_widget(extend_button)
                order_box.add_widget(cancel_button)

                self.orders_list.add_widget(order_box)

    def extend_time(self, order_id):
        print(f"Přidání 5 minut k objednávce ID {order_id}")
        # V tomto případě je potřeba implementovat logiku pro přidání času
        # například ukládání zbývajícího času.

    def cancel_order(self, order_id):
        print(f"Rušení objednávky ID {order_id}")
        OrderStorage.update_order(order_id, {"canceled": True})
        self.update_orders()

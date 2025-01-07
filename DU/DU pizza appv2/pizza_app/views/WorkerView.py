from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from pizza_app.models.SharedData import SharedData
from pizza_app.models.OrderStorage import OrderStorage


class WorkerView(BoxLayout):
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
            if not order.get("completed"):
                order_box = BoxLayout(size_hint_y=None, height=50)

                time_label = Label(
                    text=f"Čas: {order['timestamp']}", size_hint_x=0.3
                )
                order_details = Label(
                    text=f"Pizza: {order['pizza']}, Platba: {order['payment']}",
                    size_hint_x=0.5,
                )
                done_button = Button(
                    text="Hotovo",
                    size_hint_x=0.2,
                    on_press=lambda btn, oid=order["id"]: self.complete_order(oid),
                )

                order_box.add_widget(time_label)
                order_box.add_widget(order_details)
                order_box.add_widget(done_button)

                self.orders_list.add_widget(order_box)

    def complete_order(self, order_id):
        OrderStorage.update_order(order_id, {"completed": True})
        self.update_orders()

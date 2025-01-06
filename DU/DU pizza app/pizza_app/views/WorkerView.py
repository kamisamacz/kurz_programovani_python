from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import order_storage

class WorkerView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=20, **kwargs)
        print("Inicializuji WorkerView...")

        self.title_label = Label(
            text="[b]Seznam objednávek[/b]",
            font_size=18,
            markup=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            halign="center"
        )
        self.add_widget(self.title_label)

        self.orders_list = BoxLayout(orientation="vertical", size_hint=(1, 0.9))
        self.add_widget(self.orders_list)

        self.load_orders()

    def load_orders(self):
        self.orders_list.clear_widgets()
        orders = order_storage.load_orders()
        for order in orders:
            self.orders_list.add_widget(Label(
                text=f"{order['pizza']} pro {order['name']}",
                font_size=14,
                color=(1, 1, 1, 1)
            ))

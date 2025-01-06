from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class AdminView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Hlavní layout
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Nadpis
        self.title = Label(
            text="Admin Panel - Správa objednávek",
            font_size=16,
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.title)

        # Seznam objednávek
        self.order_list = BoxLayout(orientation='vertical', size_hint=(1, 0.7))
        self.layout.add_widget(self.order_list)

        self.add_widget(self.layout)

    def update_order_list(self, orders):
        """Aktualizuje seznam objednávek."""
        self.order_list.clear_widgets()
        for order in orders:
            order_label = Label(text=f"Objednávka: {order}", font_size=14)
            self.order_list.add_widget(order_label)

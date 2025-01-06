from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class WorkerView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Nadpis
        self.title = Label(
            text="WORKER",
            font_size=24,
            bold=True,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title)

        # Seznam objednávek
        self.order_list = Label(
            text="Order List: \n- Pizza 1 (Time left: 25 min)\n- Pizza 2 (Time left: 15 min)",
            size_hint=(1, 0.8)
        )
        self.layout.add_widget(self.order_list)

        self.add_widget(self.layout)

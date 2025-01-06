from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class UserView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Nadpis
        self.title = Label(
            text="Objednávka pizzy",
            font_size=24,
            color=(0, 1, 0, 1),  # Světle zelený text
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title)

        # Shrnutí objednávky
        self.order_summary = Label(
            text="Order Summary: ",
            size_hint=(1, 0.5)
        )
        self.layout.add_widget(self.order_summary)

        # Tlačítko pro kontaktování admina
        self.contact_button = Button(
            text="Contact Admin",
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.contact_button)

        self.add_widget(self.layout)

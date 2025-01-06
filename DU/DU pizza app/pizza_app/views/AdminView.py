from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class AdminView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Nadpis
        self.title = Label(
            text="ADMIN PANEL",
            font_size=24,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.title)

        # Tlačítko pro změnu priority
        self.priority_button = Button(text="Change Priority", size_hint=(1, 0.2))
        self.layout.add_widget(self.priority_button)

        # Tlačítko pro zrušení objednávky
        self.cancel_button = Button(text="Cancel Order", size_hint=(1, 0.2))
        self.layout.add_widget(self.cancel_button)

        # Tlačítko pro prodloužení času na přípravu
        self.extend_time_button = Button(text="Extend Preparation Time", size_hint=(1, 0.2))
        self.layout.add_widget(self.extend_time_button)

        self.add_widget(self.layout)

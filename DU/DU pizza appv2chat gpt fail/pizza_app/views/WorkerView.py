from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class WorkerView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10

        self.add_widget(Button(text="Process Orders", size_hint_y=None, height=50))
        print("[WORKERVIEW] View initialized.")

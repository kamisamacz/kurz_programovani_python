from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class WorkerView(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # BoxLayout pro tlačítka
        button_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5, "y": 0.05},
            spacing=20,
        )
        button_layout.add_widget(Button(text="Mark Done", size_hint=(None, None), size=(140, 40)))

        self.add_widget(button_layout)

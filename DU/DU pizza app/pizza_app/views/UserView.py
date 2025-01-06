from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import order_storage

class UserView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=20, **kwargs)
        print("Inicializuji UserView...")

        # Nastavení pozadí
        with self.canvas:
            Color(rgb=(0.267, 0.267, 0.267))  # Barva #444444
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Nadpis
        self.title_label = Label(
            text="[b]Pizza Objednávka[/b]",
            font_size=18,
            markup=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1),
            halign="center"
        )
        self.add_widget(self.title_label)

        # Pole pro zadání jména
        self.name_input = TextInput(
            hint_text="Zadejte jméno",
            font_size=14,
            size_hint=(0.33, None),  # Třetinová šířka
            height=40,
            multiline=False,
            pos_hint={"x": 0.0}  # Zarovnané doleva
        )
        self.add_widget(self.name_input)

        # Dynamický obsah
        self.dynamic_content = BoxLayout(orientation="vertical", size_hint=(1, 0.6))
        self.add_widget(self.dynamic_content)

        # Seznam již objednaných pizz
        self.orders_list = BoxLayout(orientation="vertical", size_hint=(1, 0.2))
        self.add_widget(self.orders_list)

        # Vykreslení formuláře pro výběr ingrediencí
        self.show_order_form()

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def show_order_form(self):
        """Zobrazí formulář pro vytvoření pizzy."""
        self.dynamic_content.clear_widgets()

        options = [
            ("Pomodoro základ", "base_pomodoro", [115/255, 115/255, 115/255, 1]),  # Barva #737373
            ("Smetanový základ", "base_cream", [140/255, 140/255, 140/255, 1]),   # Barva #8c8c8c
            ("Extra sýr", "extra_cheese", [115/255, 115/255, 115/255, 1]),        # Barva #737373
            ("Extra šunka", "extra_ham", [140/255, 140/255, 140/255, 1]),         # Barva #8c8c8c
        ]

        for label_text, option_name, rgba_color in options:
            row = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, None), height=50)
            with row.canvas.before:
                Color(*rgba_color)
                row.rect = Rectangle(size=row.size, pos=row.pos)
                row.bind(size=self._update_row_rect, pos=self._update_row_rect)

            label = Label(
                text=label_text,
                font_size=16,
                color=(1, 1, 1, 1),
                size_hint=(0.8, 1),
                halign="left",
                valign="middle"
            )
            label.bind(size=label.setter('text_size'))

            row.add_widget(label)

            checkbox = CheckBox(group="base" if "base" in option_name else None)
            if option_name == "base_pomodoro":
                checkbox.active = True  # Defaultně aktivní
            setattr(self, option_name, checkbox)
            row.add_widget(checkbox)

            self.dynamic_content.add_widget(row)

        submit_button = Button(
            text="Potvrdit objednávku",
            font_size=14,
            background_normal="",
            background_color=(0.102, 0.102, 0.102, 1),  # Barva #1a1a1a
            size_hint=(0.5, None),
            height=40,
            pos_hint={"center_x": 0.5}
        )
        submit_button.bind(on_press=self.submit_order)
        self.dynamic_content.add_widget(submit_button)

    def _update_row_rect(self, instance, value):
        instance.rect.size = instance.size
        instance.rect.pos = instance.pos

    def submit_order(self, instance):
        base = "Pomodoro" if self.base_pomodoro.active else "Smetanový"
        extras = []
        if self.extra_cheese.active:
            extras.append("extra sýr")
        if self.extra_ham.active:
            extras.append("extra šunka")

        name = self.name_input.text.strip()
        if not name:
            print("Chyba: Jméno není zadáno!")
            return

        order = {
            "name": name,
            "pizza": f"Hawaii ({base}, {', '.join(extras) or 'bez přídavků'})"
        }
        order_storage.save_order(order)

        self.orders_list.add_widget(Label(
            text=f"{order['pizza']} pro {order['name']}",
            font_size=14,
            color=(1, 1, 1, 1)
        ))
        self.show_order_form()

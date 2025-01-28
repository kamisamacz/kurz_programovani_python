import json
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner


class UserView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = [10, 10, 10, 10]

        # Input fields
        self.name_input = TextInput(hint_text="Your Name", size_hint_y=None, height=40)
        self.add_widget(self.name_input)

        self.pizza_spinner = Spinner(
            text="Select Pizza",
            values=["Hawaii", "Pepperoni", "Margherita"],
            size_hint_y=None,
            height=40,
        )
        self.add_widget(self.pizza_spinner)

        self.base_label = Label(text="Choose Base:")
        self.add_widget(self.base_label)

        self.base_pomodoro = CheckBox(group="base")
        self.base_smetana = CheckBox(group="base")
        self.add_widget(Label(text="Pomodoro Base", size_hint_y=None, height=30))
        self.add_widget(self.base_pomodoro)
        self.add_widget(Label(text="Smetana Base", size_hint_y=None, height=30))
        self.add_widget(self.base_smetana)

        self.extras_label = Label(text="Extras:")
        self.add_widget(self.extras_label)

        self.ham_checkbox = CheckBox()
        self.cheese_checkbox = CheckBox()
        self.ananas_checkbox = CheckBox()

        self.add_widget(Label(text="Extra Ham", size_hint_y=None, height=30))
        self.add_widget(self.ham_checkbox)
        self.add_widget(Label(text="Extra Cheese", size_hint_y=None, height=30))
        self.add_widget(self.cheese_checkbox)
        self.add_widget(Label(text="Extra Pineapple", size_hint_y=None, height=30))
        self.add_widget(self.ananas_checkbox)

        self.payment_spinner = Spinner(
            text="Payment Method",
            values=["Cash", "Card"],
            size_hint_y=None,
            height=40,
        )
        self.add_widget(self.payment_spinner)

        # Create Order button
        self.create_order_button = Button(
            text="Create Order", size_hint_y=None, height=50, on_press=self.create_order
        )
        self.add_widget(self.create_order_button)

    def create_order(self, instance):
        print("[USER] Attempting to create an order...")
        name = self.name_input.text
        pizza = self.pizza_spinner.text
        base = "Pomodoro" if self.base_pomodoro.active else "Smetana" if self.base_smetana.active else None
        extras = {
            "ham": self.ham_checkbox.active,
            "cheese": self.cheese_checkbox.active,
            "ananas": self.ananas_checkbox.active,
        }
        payment = self.payment_spinner.text

        if not name or not pizza or not base or not payment:
            print("[USER] Error: Missing required fields.")
            return

        order = {
            "name": name,
            "pizza": pizza,
            "base": base,
            "extras": extras,
            "payment": payment,
            "status": "Pending",
        }

        # Save order to file
        try:
            with open("orders.json", "a") as f:
                json.dump(order, f)
                f.write("\n")
            print("[USER] Order created successfully:", order)
        except Exception as e:
            print("[USER] Error saving order:", e)

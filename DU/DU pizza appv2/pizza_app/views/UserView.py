from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import order_storage
import datetime

class UserView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Input pro jméno uživatele
        self.add_widget(Label(text="Vaše jméno:", size_hint=(1, 0.1)))
        self.name_input = TextInput(hint_text="Zadejte vaše jméno")
        self.add_widget(self.name_input)

        # Výběr pizzy
        self.add_widget(Label(text="Název pizzy:", size_hint=(1, 0.1)))
        self.pizza_name_input = TextInput(hint_text="Zadejte název pizzy")
        self.add_widget(self.pizza_name_input)

        # Výběr základu (Pomodoro/Smetana)
        self.add_widget(Label(text="Základ:", size_hint=(1, 0.1)))
        self.base_spinner = Spinner(text="Pomodoro", values=["Pomodoro", "Smetana"])
        self.add_widget(self.base_spinner)

        # Přídavky (šunka navíc, extra sýr)
        self.add_widget(Label(text="Přídavky:", size_hint=(1, 0.1)))
        self.ham_checkbox = CheckBox()
        self.add_widget(BoxLayout(size_hint=(1, 0.1)).add_widget(Label(text="Šunka navíc")).add_widget(self.ham_checkbox))
        self.cheese_checkbox = CheckBox()
        self.add_widget(BoxLayout(size_hint=(1, 0.1)).add_widget(Label(text="Extra sýr")).add_widget(self.cheese_checkbox))

        # Výběr platby
        self.add_widget(Label(text="Způsob platby:", size_hint=(1, 0.1)))
        self.payment_spinner = Spinner(text="Hotově", values=["Hotově", "Kartou"])
        self.add_widget(self.payment_spinner)

        # Tlačítko pro odeslání objednávky
        self.submit_button = Button(text="Odeslat objednávku", size_hint=(1, 0.2))
        self.submit_button.bind(on_press=self.submit_order)
        self.add_widget(self.submit_button)

        # Status label
        self.status_label = Label(text="", size_hint=(1, 0.1))
        self.add_widget(self.status_label)

    def submit_order(self, instance):
        # Načíst data z inputů
        name = self.name_input.text.strip()
        pizza_name = self.pizza_name_input.text.strip()
        base = self.base_spinner.text
        extras = []
        if self.ham_checkbox.active:
            extras.append("Šunka navíc")
        if self.cheese_checkbox.active:
            extras.append("Extra sýr")
        payment = self.payment_spinner.text
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Validace dat
        if not name or not pizza_name:
            self.status_label.text = "Vyplňte všechna povinná pole!"
            print("Uživatelská chyba: Chybí povinné údaje!")
            return

        # Vytvořit objednávku
        order = {
            "id": timestamp,  # Unikátní ID na základě času
            "name": name,
            "pizza": pizza_name,
            "base": base,
            "extras": extras,
            "payment": payment,
            "timestamp": timestamp,
            "status": "Zpracovává se",
        }

        # Uložit objednávku
        order_storage.OrderStorage.add_order(order)
        print(f"Objednávka vytvořena: {order}")

        # Potvrzení pro uživatele
        self.status_label.text = "Objednávka odeslána!"
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', ''), 3)

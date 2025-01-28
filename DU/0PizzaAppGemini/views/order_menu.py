from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

class OrderMenuApp(App):
    def build(self):
        print("Vytvářím OrderMenuApp...")
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Objednávka pizzy:')
        layout.add_widget(label)

        self.size_spinner = Spinner(
            text='Vyberte velikost',
            values=('Malá', 'Střední', 'Velká')
        )
        layout.add_widget(self.size_spinner)

        self.address_input = TextInput(
            multiline=True,
            hint_text="Zadejte adresu"
        )
        layout.add_widget(self.address_input)

        self.salami_checkbox = CheckBox(label='Salami')
        layout.add_widget(self.salami_checkbox)

        self.pepperoni_checkbox = CheckBox(label='Pepperoni')
        layout.add_widget(self.pepperoni_checkbox)

        # ... další náplně ...

        order_button = Button(text='Objednat')
        order_button.bind(on_press=self.objednat)
        layout.add_widget(order_button)

        return layout

    def objednat(self, instance):
        print("Zpracovávám objednávku...")
        velikost = self.size_spinner.text
        adresa = self.address_input.text
        salami = self.salami_checkbox.active
        pepperoni = self.pepperoni_checkbox.active
        # ... získání hodnot z dalších checkboxů ...

        print(f"Objednávka: velikost={velikost}, adresa={adresa}, salami={salami}, pepperoni={pepperoni}")
        # Zde bude implementována logika pro uložení objednávky
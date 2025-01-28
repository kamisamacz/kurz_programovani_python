from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class AdminMenuApp(App):
    def build(self):
        print("Vytvářím AdminMenuApp...")
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Admin Menu:')
        layout.add_widget(label)

        zobrazit_objednavky_button = Button(text='Zobrazit objednávky')
        zobrazit_objednavky_button.bind(on_press=self.zobrazit_objednavky)
        layout.add_widget(zobrazit_objednavky_button)

        return layout

    def zobrazit_objednavky(self, instance):
        print("Zobrazuji objednávky...")
        # Zde bude implementována logika pro zobrazení objednávek
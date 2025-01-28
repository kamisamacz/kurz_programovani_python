from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainMenuApp(App):
    def build(self):
        print("Vytvářím MainMenuApp...")
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Hlavní menu:')
        layout.add_widget(label)

        objednat_pizzu_button = Button(text='Objednat pizzu')
        objednat_pizzu_button.bind(on_press=self.objednat_pizzu)
        layout.add_widget(objednat_pizzu_button)

        historie_objednavek_button = Button(text='Historie objednávek')
        historie_objednavek_button.bind(on_press=self.historie_objednavek)
        layout.add_widget(historie_objednavek_button)

        konec_button = Button(text='Konec')
        konec_button.bind(on_press=self.ukoncit_aplikaci)
        layout.add_widget(konec_button)

        return layout

    def objednat_pizzu(self, instance):
        print("Otevírám formulář pro objednání pizzy...")
        # Zde bude implementována logika pro otevření formuláře

    def historie_objednavek(self, instance):
        print("Zobrazuji historii objednávek...")
        # Zde bude implementována logika pro zobrazení historie objednávek

    def ukoncit_aplikaci(self, instance):
        print("Ukončuji aplikaci...")
        App.get_running_app().stop()
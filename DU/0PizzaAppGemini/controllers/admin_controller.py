from views.admin_menu import AdminMenuApp
from utils import nacist_objednavky
from kivy.uix.label import Label


class AdminController:
    def __init__(self):
        print("Vytvářím AdminController...")
        self.admin_menu = AdminMenuApp()
        self.admin_menu.admin_controller = self  # propojení s AdminMenuApp

    def run(self):
        print("Spouštím AdminMenuApp...")
        self.admin_menu.run()

    def zobrazit_objednavky(self, instance):
        print("Načítám objednávky pro zobrazení...")
        objednavky = nacist_objednavky()

        # Vytvoření layoutu pro zobrazení objednávek
        layout = self.admin_menu.root_window.children[0]  # Získání hlavního layoutu
        layout.clear_widgets()  # Vyčištění stávajícího obsahu

        if objednavky:
            for objednavka in objednavky:
                label = Label(text=str(objednavka))
                layout.add_widget(label)
        else:
            layout.add_widget(Label(text="Žádné objednávky k zobrazení."))
from views.main_menu import MainMenuApp
from views.order_menu import OrderMenuApp
from views.admin_menu import AdminMenuApp
from controllers.admin_controller import AdminController

class MainController:
    def __init__(self):
        print("Vytvářím MainController...")
        self.main_menu = MainMenuApp()
        self.order_menu = OrderMenuApp()
        self.admin_controller = AdminController()  # Vytvoření instance AdminController

    def run(self):
        print("Spouštím MainMenuApp...")
        self.main_menu.run()

    def objednat_pizzu(self):
        print("Otevírám formulář pro objednání pizzy...")
        self.order_menu.run()

    def zobrazit_historii_objednavek(self):
        print("Zobrazuji historii objednávek...")
        self.admin_controller.run()  # Spuštění AdminMenuApp přes AdminController
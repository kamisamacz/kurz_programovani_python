from kivy.app import App
from kivy.core.window import Window
from pizza_app.views.UserView import UserView
from pizza_app.views.WorkerView import WorkerView
from pizza_app.views.AdminView import AdminView
import threading


# Nastavení velikosti a pozice jednotlivých oken
def set_window_properties(app_name):
    if app_name == "UserApp":
        Window.size = (300, 600)  # Šířka x výška
        Window.top = 50
        Window.left = 10
    elif app_name == "WorkerApp":
        Window.size = (300, 600)
        Window.top = 50
        Window.left = 320
    elif app_name == "AdminApp":
        Window.size = (400, 600)
        Window.top = 50
        Window.left = 730


# Definice aplikací
class UserApp(App):
    def build(self):
        print("[USER] User App loaded successfully.")
        set_window_properties("UserApp")
        return UserView()


class WorkerApp(App):
    def build(self):
        print("[WORKER] Worker App loaded successfully.")
        set_window_properties("WorkerApp")
        return WorkerView()


class AdminApp(App):
    def build(self):
        print("[ADMIN] Admin App loaded successfully.")
        set_window_properties("AdminApp")
        return AdminView()


# Funkce pro paralelní spuštění aplikací
def run_user_app():
    UserApp().run()


def run_worker_app():
    WorkerApp().run()


def run_admin_app():
    AdminApp().run()


if __name__ == "__main__":
    print("[MAIN] Launching all apps...")

    # Spuštění všech aplikací ve vláknech
    user_thread = threading.Thread(target=run_user_app)
    worker_thread = threading.Thread(target=run_worker_app)
    admin_thread = threading.Thread(target=run_admin_app)

    user_thread.start()
    worker_thread.start()
    admin_thread.start()

    user_thread.join()
    worker_thread.join()
    admin_thread.join()

from kivy.app import App
from pizza_app.views.AdminView import AdminView


class AdminApp(App):
    def build(self):
        print("[ADMIN] Admin App loaded successfully.")
        return AdminView()


if __name__ == "__main__":
    print("[ADMIN] Launching Admin App...")
    AdminApp().run()

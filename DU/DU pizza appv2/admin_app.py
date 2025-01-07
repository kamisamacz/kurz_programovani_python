from kivy.app import App
from pizza_app.views.AdminView import AdminView

class AdminApp(App):
    def build(self):
        self.title = "Admin Panel"
        print("[DEBUG] AdminApp initialized")
        return AdminView()

if __name__ == "__main__":
    AdminApp().run()

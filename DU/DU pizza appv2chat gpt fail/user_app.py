from kivy.app import App
from pizza_app.views.UserView import UserView


class UserApp(App):
    def build(self):
        print("[USER] User App loaded successfully.")
        return UserView()


if __name__ == "__main__":
    print("[USER] Launching User App...")
    UserApp().run()

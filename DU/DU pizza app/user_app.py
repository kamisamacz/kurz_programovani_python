from kivy.app import App
from pizza_app.views.UserView import UserView

class UserApp(App):
    def build(self):
        print("Spouštím uživatelskou aplikaci...")
        return UserView()

if __name__ == "__main__":
    UserApp().run()

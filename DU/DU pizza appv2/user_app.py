from kivy.app import App
from pizza_app.views.UserView import UserView

class UserApp(App):
    def build(self):
        self.title = "User Panel"
        print("[DEBUG] UserApp initialized")
        return UserView()

if __name__ == "__main__":
    UserApp().run()

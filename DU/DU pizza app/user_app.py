from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pizza_app.views.UserView import UserView

class UserApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserView(name='user'))
        return sm

if __name__ == "__main__":
    UserApp().run()
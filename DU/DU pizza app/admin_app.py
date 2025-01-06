from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pizza_app.views.AdminView import AdminView

class AdminApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AdminView(name='admin'))
        return sm

if __name__ == "__main__":
    AdminApp().run()
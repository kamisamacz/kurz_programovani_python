from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pizza_app.views.AdminView import AdminView
from pizza_app.controllers.AdminController import AdminController

class AdminApp(App):
    def build(self):
        view = AdminView(name='admin')
        controller = AdminController(view)

        sm = ScreenManager()
        sm.add_widget(view)
        return sm

if __name__ == "__main__":
    AdminApp().run()

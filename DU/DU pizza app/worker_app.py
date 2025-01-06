from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from pizza_app.views.WorkerView import WorkerView

class WorkerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WorkerView(name='worker'))
        return sm

if __name__ == "__main__":
    WorkerApp().run()
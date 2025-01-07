from kivy.app import App
from pizza_app.views.WorkerView import WorkerView

class WorkerApp(App):
    def build(self):
        self.title = "Worker Panel"
        print("[DEBUG] WorkerApp initialized")
        return WorkerView()

if __name__ == "__main__":
    WorkerApp().run()

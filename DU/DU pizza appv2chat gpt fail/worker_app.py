from kivy.app import App
from pizza_app.views.WorkerView import WorkerView


class WorkerApp(App):
    def build(self):
        print("[WORKER] Worker App loaded successfully.")
        return WorkerView()


if __name__ == "__main__":
    print("[WORKER] Launching Worker App...")
    WorkerApp().run()

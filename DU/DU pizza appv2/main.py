from multiprocessing import Process
from kivy.config import Config
from admin_app import AdminApp
from user_app import UserApp
from worker_app import WorkerApp

def start_user_app():
    Config.set("graphics", "width", "375")
    Config.set("graphics", "height", "650")
    Config.set("graphics", "position", "custom")
    Config.set("graphics", "left", "570")
    Config.set("graphics", "top", "45")
    print("[DEBUG] Starting UserApp...")
    UserApp().run()

def start_admin_app():
    Config.set("graphics", "width", "500")
    Config.set("graphics", "height", "650")
    Config.set("graphics", "position", "custom")
    Config.set("graphics", "left", "10")
    Config.set("graphics", "top", "45")
    print("[DEBUG] Starting AdminApp...")
    AdminApp().run()

def start_worker_app():
    Config.set("graphics", "width", "375")
    Config.set("graphics", "height", "650")
    Config.set("graphics", "position", "custom")
    Config.set("graphics", "left", "980")
    Config.set("graphics", "top", "45")
    print("[DEBUG] Starting WorkerApp...")
    WorkerApp().run()

if __name__ == "__main__":
    p1 = Process(target=start_user_app)
    p2 = Process(target=start_admin_app)
    p3 = Process(target=start_worker_app)
    p1.start()
    p2.start()
    p3.start()

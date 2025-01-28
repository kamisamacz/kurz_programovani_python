import controllers.main_controller

if __name__ == "__main__":
    print("Spouštím aplikaci...")
    app = controllers.main_controller.MainController()
    app.run()
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind actions from the view to controller methods
        self.view.contact_button.bind(on_press=self.contact_admin)

    def contact_admin(self, instance):
        # Example logic for contacting the admin
        print("Admin contacted for order cancellation.")

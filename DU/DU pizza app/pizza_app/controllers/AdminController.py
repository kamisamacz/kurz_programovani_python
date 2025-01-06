class AdminController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind actions from the view to controller methods
        self.view.priority_button.bind(on_press=self.change_priority)
        self.view.cancel_button.bind(on_press=self.cancel_order)
        self.view.extend_time_button.bind(on_press=self.extend_time)

    def change_priority(self, instance):
        # Example logic for changing priority
        print("Priority changed!")

    def cancel_order(self, instance):
        # Example logic for canceling an order
        print("Order cancelled!")

    def extend_time(self, instance):
        # Example logic for extending preparation time
        print("Preparation time extended!")

from pizza_app.models.SharedData import SharedData

class WorkerController:
    def __init__(self, view):
        self.view = view
        self.update_tasks()

    def update_tasks(self):
        """Načte úkoly ze sdílených dat."""
        tasks = SharedData.get_orders()
        self.view.update_task_list(tasks)

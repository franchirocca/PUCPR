class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {'description': description, 'completed': False}
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            return self.tasks[index]
        return None

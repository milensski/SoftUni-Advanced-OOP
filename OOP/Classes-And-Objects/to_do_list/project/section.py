from task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            t = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        t.complete()
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = list(filter(lambda t: t.completed == True, self.tasks))
        for task in removed_tasks:
            self.tasks.remove(task)
        return f"Cleared {len(removed_tasks)} tasks."

    def view_section(self):
        tasks = '\n'.join([f'{task.details()}' for task in self.tasks])
        return f"Section {self.name}: {tasks}"


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
section.complete_task(second_task)
print(section.clean_section())
print(section.view_section())

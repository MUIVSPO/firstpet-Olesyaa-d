tasks = {}

def add_task(task_name):
    if task_name not in tasks:
        tasks[task_name] = False
        print(f"Задача '{task_name}' добавлена.")
    else:
        print(f"Задача '{task_name}' уже существует.")

def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Задача '{task_name}' отмечена как выполненная.")
    else:
        print(f"Задача '{task_name}' не найдена.")

def list_tasks(status=None):
    if status not in [None, 'done', 'not_done']:
        print("Недопустимый статус. Используйте 'done' или 'not_done'")
        return

    for task, completed in tasks.items():
        if status == 'done' and completed:
            print(f"[✔] {task}")
        elif status == 'not_done' and not completed:
            print(f"[ ] {task}")
        elif status is None:
            print(f"[✔] {task}" if completed else f"[ ] {task}")
add_task("прийти на пару")
add_task("сдать проет")
complete_task("прийти на пару")

print("\nВсе задачи:")
list_tasks()

print("\nВыполненные задачи:")
list_tasks('done')

print("\nНевыполненные задачи:")
list_tasks('not_done')

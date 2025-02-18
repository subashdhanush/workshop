tasks = []
while True:
    task = input("Add a task (or type 'done'): ")
    if task == 'done':
        break
    tasks.append(task)
print("Your tasks:", tasks)

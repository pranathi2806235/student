tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == '2':
        print("Your Tasks:")
        for i, t in enumerate(tasks):
            print(i, t)

    elif choice == '3':
        for i, t in enumerate(tasks):
            print(i, t)

        index = int(input("Enter index to delete: "))
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted")
        else:
            print("Invalid index")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        branch = input("Enter branch: ")

        students.append({"name": name, "roll": roll, "branch": branch})

    elif choice == '2':
        for s in students:
            print(s)

    elif choice == '3':
        r = input("Enter roll to search: ")
        found = False
        for s in students:
            if s["roll"] == r:
                print(s)
                found = True
        if not found:
            print("Not found")

    elif choice == '4':
        r = input("Enter roll to delete: ")
        for s in students:
            if s["roll"] == r:
                students.remove(s)
                print("Deleted")
                break

    elif choice == '5':
        break

    else:
        print("Invalid choice")
todos = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            existing_todo = todos[number]
            new_todo = input("Enter new todo: ").capitalize()
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Invalid command. Please try again.")

print("Goodbye!")

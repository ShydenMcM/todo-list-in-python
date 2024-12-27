todos = []

while True:
    user_action = input("Type add, show or exit: ").strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Invalid command. Please try again.")

print("Goodbye!")

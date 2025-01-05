todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for index, item in enumerate(todos):
                print(f"[{index + 1}]-: {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            existing_todo = todos[number]
            new_todo = input("Enter new todo: ").capitalize()
            todos[number] = new_todo
            print(f"Replaced {existing_todo} with {new_todo}")
        case "complete":
            number = int(input("Number of the todo to complete: "))
            print(f"{todos[number-1]} has been completed so it has been removed.")
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Invalid command. Please try again.")

print("Goodbye!")

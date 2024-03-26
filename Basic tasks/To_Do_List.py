class Todo:
    def __init__(self, my_todos, idx, completed=False):
        self.my_todo = my_todos
        self.idx = idx
        self.completed = completed

    def __str__(self):
        return f"{self.idx} - {self.my_todo} - Completed : {self.completed}"

    def change_completed(self):
        self.completed = True


def check_choice(num):
    while num not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid choice.")
        num = input("")
    return num


def load_todos():
    todos = []
    with open("todos.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            todo = line.split(" - ")
            todo = Todo(
                todo[1], int(todo[0]), True if todo[2] == "True" else False
            )
            todos.append(todo)
    return todos


def save_todos(todos):
    with open("todos.txt", "w") as f:
        for todo in todos:
            f.write(f"{todo.idx} - {todo.my_todo} - {todo.completed}\n")



if __name__ == "__main__":
    try:
        todo_list = load_todos()
    except FileNotFoundError:
        todo_list = []
    index = 1
    while True:
        print("Welcome to your to do list")
        print("Here are your options:")
        print("1 - Add to do")
        print("2 - Remove to do")
        print("3 - View to do list")
        print("4 - Complete to do")
        print("5 - View completed to do list")
        print("6 - Exit")
        print("Please enter your choice:")

        choice = input('')
        choice = check_choice(choice)

        if choice == "1":
            print("Please enter your to do to add:")
            todo = input()
            my_todo = Todo(todo, index)
            todo_list.append(my_todo)
            index += 1

        elif choice == "2":
            print("Please enter the number of the to do to remove:")
            number = input()
            while not number.isdigit():
                print("Please enter a valid number")
                number = input()
            number = int(number)
            for todo in todo_list:
                if todo.idx == number:
                    todo_list.remove(todo)
                    break
            else:
                print("No to do found with this id")

        elif choice == "3":
            if not todo_list:
                print("No to do's found")
            else:
                for todo in todo_list:
                    if not todo.completed:
                        print(todo)
        elif choice == "4":
            print("Please enter the number of the completed to do:")
            number = input()
            while not number.isdigit():
                print("Please enter a valid number")
                number = input()
            number = int(number)
            for todo in todo_list:
                if todo.idx == number:
                    todo.change_completed()
                    break
            else:
                print("No to do found with this id")

        elif choice == "5":
            if not todo_list:
                print("No to do's found")
            else:
                for todo in todo_list:
                    if todo.completed:
                        print(todo)

        elif choice == "6":
            print("Thanks for using the to do list. Goodbye!")
            save_todos(todo_list)
            break
        else:
            print("Please enter a valid choice")
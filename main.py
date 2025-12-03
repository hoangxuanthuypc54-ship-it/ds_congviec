from guizero import App, TextBox, ListBox, PushButton, Text

file = "todo.txt"

def doc_file():
    listbox.clear()
    with open("todo.txt", "r") as file:
        for line in file:
            listbox.append(line.strip())

def add_item():
    if textbox.value:
        listbox.append(textbox.value)
        with open(file, "a") as file:
            file.write(textbox.value + "\n")

def delete_item():
    listbox.remove(listbox.value)

    with open("todo.txt", "w") as file:
        for item in listbox.items:
            file.write(item + "\n")
        
app = App(title="todo list")

Text(app, "nhap viec can lam:")

textbox = TextBox(app, width=32)

PushButton(app, text="them viec", command=add_item)


PushButton(app, text="xoa viec", command=delete_item)

listbox = ListBox(app, width=200, height=100)

doc_file()

app.display()

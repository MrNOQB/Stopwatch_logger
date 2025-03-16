from variables import task_list
from tkinter.messagebox import askyesno

def submit(user_input, selected_task, list_of_tasks, message_label):
    user_entry = user_input.entry.get().strip()

    if not user_entry:
        message_label.label.configure(text_color="red", text="You can't add \n an empty space!")
        return

    if user_entry.lower() in (task.lower() for task in task_list.keys()):
        message_label.label.configure(text_color="red", text="Task already inputted!")
        return

    task_list[user_entry] = "00:00:00"
    selected_task.listbox.configure(values=list(task_list.keys()))

    list_of_tasks.textbox.configure(state="normal")
    list_of_tasks.textbox.insert("end", f"{user_entry}:\n    {task_list[user_entry]}\n\n")
    list_of_tasks.textbox.configure(state="disabled")

    user_input.entry.delete(0, "end")
    message_label.label.configure(text_color="red", text="")

def limit_input(text_var, message_label):
    txt = text_var.get().strip()
    text_var.set(txt[:20])

    if len(txt) > 20:
        message_label.label.configure(text="You can only input \n twenty characters!", text_color="red")


def clear_tasks(list_of_tasks, selected_task, message_label):
    if not task_list:
        message_label.label.configure(text_color="red", text="List is already clear!")
        return

    user_answer = askyesno(title="Clearing all tasks", message="Are you sure you want to clear all tasks?")
    if user_answer:
        task_list.clear()
        selected_task.listbox.configure(values=[])

        list_of_tasks.textbox.configure(state="normal")
        list_of_tasks.textbox.delete("1.0", "end")
        list_of_tasks.textbox.configure(state="disabled")

        message_label.label.configure(text_color="red", text="")


def delete_task(selected_task, list_of_tasks, message_label):
    selected = selected_task.listbox.get()

    if not selected:
        message_label.label.configure(text_color="red", text="No item is selected!")
        return


    if selected in task_list:
        del task_list[selected]


    selected_task.listbox.configure(values=list(task_list.keys()))
    selected_task.listbox.set("")


    list_of_tasks.textbox.configure(state="normal")
    list_of_tasks.textbox.delete("1.0", "end")
    for task, time in task_list.items():
        list_of_tasks.textbox.insert("end", f"{task}:\n    {time}\n\n")
    list_of_tasks.textbox.configure(state="disabled")

    message_label.label.configure(text_color="red", text="")
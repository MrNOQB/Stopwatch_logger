import variables
from tkinter.messagebox import askyesno

def submit(user_input, selected_task, list_of_tasks, message_label):
    user_entry = user_input.entry.get().strip()

    if not user_entry:
        message_label.label.configure(text_color="red", text="You can't add \n an empty space!")
        return

    if user_entry.lower() in (task.lower() for task in variables.task_list.keys()):
        message_label.label.configure(text_color="red", text="Task already inputted!")
        return


    variables.task_list[user_entry] = "00:00:00"

    variables.original_task_order.append(user_entry)

    selected_task.listbox.configure(values=list(variables.original_task_order))

    list_of_tasks.textbox.configure(state="normal")
    list_of_tasks.textbox.delete("1.0", "end")


    for task in variables.original_task_order:
        time = variables.task_list[task]
        list_of_tasks.textbox.insert("end", f"\n{task}:\n{time}\n\n")

    list_of_tasks.textbox.configure(state="disabled")

    user_input.entry.delete(0, "end")
    message_label.label.configure(text_color="red", text="")

def limit_input(text_var, message_label):
    txt = text_var.get().strip()
    text_var.set(txt[:20])

    if len(txt) > 20:
        message_label.label.configure(text="You can only input \n twenty characters!", text_color="red")

def clear_tasks(list_of_tasks, selected_task, message_label):
    if not variables.task_list:
        message_label.label.configure(text_color="red", text="List is already clear!")
        return

    user_answer = askyesno(title="Clearing all tasks", message="Are you sure you want to clear all tasks?")
    if user_answer:
        variables.task_list.clear()
        variables.original_task_order.clear()

        selected_task.listbox.configure(values=[])
        selected_task.listbox.set("")

        list_of_tasks.textbox.configure(state="normal")
        list_of_tasks.textbox.delete("1.0", "end")
        list_of_tasks.textbox.configure(state="disabled")

        message_label.label.configure(text_color="red", text="")

def delete_task(selected_task, list_of_tasks, message_label):
    selected = selected_task.listbox.get()

    if not selected:
        message_label.label.configure(text_color="red", text="No item is selected!")
        return

    if selected in variables.task_list:
        del variables.task_list[selected]

    if selected in variables.original_task_order:
        variables.original_task_order.remove(selected)
    selected_task.listbox.configure(values=list(variables.task_list.keys()))
    selected_task.listbox.set("")

    list_of_tasks.textbox.configure(state="normal")
    list_of_tasks.textbox.delete("1.0", "end")


    for task in variables.original_task_order:
        if task in variables.task_list:
            time = variables.task_list[task]
            list_of_tasks.textbox.insert("end", f"{task}:\n    {time}\n\n")

    list_of_tasks.textbox.configure(state="disabled")
    message_label.label.configure(text_color="red", text="")

def get_total_seconds(time_string):
    hours, minutes, seconds = map(int, time_string.split(":"))
    return (hours * 3600) + (minutes * 60) + seconds

def convert_seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def update_task_time(selected, current_time_in_seconds):
    if selected in variables.task_list:
        total_seconds = get_total_seconds(variables.task_list[selected])
        total_seconds += current_time_in_seconds
        variables.task_list[selected] = convert_seconds_to_hms(total_seconds)
def refresh_task_list_display(list_of_tasks):
    list_of_tasks.textbox.configure(state="normal")
    list_of_tasks.textbox.delete("1.0", "end")


    for task in variables.original_task_order:
        if task in variables.task_list:
            time = variables.task_list[task]
            list_of_tasks.textbox.insert("end", f"\n{task}:\n{time}\n\n")

    list_of_tasks.textbox.configure(state="disabled")

def reset_stopwatch():
    variables.one_tenth_of_a_second = 0
    variables.seconds = 0
    variables.minutes = 0
    variables.hours = 0
    variables.running = False

def save_time(selected_task, message_label, list_of_tasks):
    is_zero2 = (variables.hours == 0 and variables.minutes == 0 and
               variables.seconds == 0)


    selected = selected_task.listbox.get()

    print(selected)

    current_time_in_seconds =  variables.seconds + (variables.minutes * 60 ) + (variables.hours * 3600)

    if not selected:

        message_label.label.configure(text_color="red", text="No task is selected!")
        return
    elif is_zero2:
        message_label.label.configure(text_color="red", text="No enough time to save!")
        return

    message_label.label.configure(text_color="red", text="")
    update_task_time(selected, current_time_in_seconds)
    refresh_task_list_display(list_of_tasks)
    reset_stopwatch()


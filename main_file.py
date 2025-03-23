from variables import formatted_tasks
from gui import *
from stopwatch import start, stop, reset
import variables
from utils import submit, limit_input, clear_tasks, delete_task, save_time
from variables import task_list


def start_button_disappear():
    start_button.button.place_forget()
    stop_button.button.place(x=70, y=320)
def start_button_appear():
    start_button.button.place(x=70, y=320)
    stop_button.button.place_forget()


last_time_text = ""
last_small_time_text = ""
last_states = {}

def update_buttons():
    global last_states

    is_zero = (variables.hours == 0 and variables.minutes == 0 and
               variables.seconds == 0 and variables.one_tenth_of_a_second == 0)

    buttons = [
        (save_button.button, variables.running or is_zero),
        (reset_button.button, is_zero)
    ]

    for button, condition in buttons:
        new_state = "disabled" if condition else "normal"
        new_color = ("gray30", "gray10") if condition else "#1f6aa5"

        if last_states.get(button) != new_state:
            button.configure(state=new_state, fg_color=new_color)
            last_states[button] = new_state
def update_gui():
    global last_time_text, last_small_time_text

    new_time_text = f'{variables.hours:02}:{variables.minutes:02}:{variables.seconds:02}'
    new_small_time_text = f'.{variables.one_tenth_of_a_second:02}'

    if new_time_text != last_time_text:
        clock_label.label.configure(text=new_time_text)
        last_time_text = new_time_text

    if new_small_time_text != last_small_time_text:
        small_clock_label.label.configure(text=new_small_time_text)
        last_small_time_text = new_small_time_text

    update_buttons()

    gui.window.after(10, update_gui)


gui = MainWindow()
text_var = StringVar()
welcome_label = Labels(gui.window, "Input your task here!", ("Candara", 32), 10, 10)
message_label = Labels(gui.window, "", ('Impact', 22), 260, 60)
user_input = Entries(gui.window, 245, ("Terminal", 20), 10, 60)
user_input.entry.configure(textvariable=text_var)
text_var.trace_add("write", lambda *args: limit_input(text_var, message_label))
submit_button = Buttons(gui.window, "Submit", 70, ('Arial', 30) , 30, 100)
submit_button.button.configure(command=lambda: submit(user_input, selected_task, list_of_tasks, message_label))
selected_task = ComboBoxes(gui.window, 490, 10, list(task_list.keys()))
list_of_tasks = ReadOnlyTextBox(gui.window, 442, 50, formatted_tasks, 195, 200)
list_of_tasks.textbox.configure(font=("Terminal", 18))
clear_button = Buttons(gui.window, "Clear all", 90, ('Arial', 17), 508, 290)
clear_button.button.configure(command=lambda: clear_tasks(list_of_tasks, selected_task, message_label))
delete_button = Buttons(gui.window, "Delete selected task", 110, ('Arial', 18), 467, 254)
delete_button.button.configure(command=lambda: delete_task(selected_task, list_of_tasks, message_label))
stop_button = ImageButton(gui.window, '', 80, 80, 1000, 1000, 'pausebuttonimage.png', lambda :[stop(),start_button_appear()])
start_button = ImageButton(gui.window, '', 80, 80, 70, 320, 'playbuttonimg.png',  lambda: [start(), start_button_disappear()])
reset_button = ImageButton(gui.window, '', 40, 40, 170, 360, 'resetbutton2.png',  lambda : [reset(), start_button_appear()])

save_button = ImageButton(gui.window, '', 40, 40, 10, 360, 'save__image.png', lambda: [save_time(selected_task, message_label, list_of_tasks)])
clock_label = Labels(gui.window, f'{variables.hours:02}:{variables.minutes:02}:{variables.seconds:02}', ('Impact', 70), 10, 220)
small_clock_label = Labels(gui.window, f'.{variables.one_tenth_of_a_second:02}', ('Impact', 40), 264, 249)

if __name__ == '__main__':
    update_gui()
    gui.window.mainloop()
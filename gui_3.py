from main_1 import *
from stopwatch_2 import start, stop, reset
import variables
from utils_4 import submit, limit_input, clear_tasks, delete_task
from variables import task_list

#Body!!! you are so close to finishing this shit! next time
#add a save time button, that saves stopwatch time to selected task
#and updayes the time in text box!
#after that works, now move everything to a data base! prob json file!
#so that after you open the application again, your tasks and times are stil there!
def start_button_disappear():
    start_button.button.place_forget()
    stop_button.button.place(x=70, y=320)
def start_button_appear():
    start_button.button.place(x=70, y=320)
    stop_button.button.place_forget()
def update_gui():
    clock_label.label.configure(text=f'{variables.hours:02}:{variables.minutes:02}:{variables.seconds:02}')
    small_clock_label.label.configure(text=f'.{variables.one_tenth_of_a_second:02}')

    is_zero = (variables.hours == 0 and variables.minutes == 0 and
               variables.seconds == 0 and variables.one_tenth_of_a_second == 0)

    current_state = reset_button.button.cget("state")

    if is_zero and current_state != "disabled":
        reset_button.button.configure(state="disabled", fg_color=("gray30", "gray10"))
    elif not is_zero and current_state != "normal":
        reset_button.button.configure(state="normal", fg_color=("#1f6aa5"))

    gui.window.after(10, update_gui)


gui = MainWindow()
text_var = StringVar()
welcome_label = Labels(gui.window, "Input your task here!", ("Candara", 32), 10, 10)
message_label = Labels(gui.window, "", ('Impact', 22), 240, 60)
user_input = Entries(gui.window, 220, ("Terminal", 20), 10, 60)
user_input.entry.configure(textvariable=text_var)
text_var.trace_add("write", lambda *args: limit_input(text_var, message_label))
submit_button = Buttons(gui.window, "Submit", 70, ('Arial', 30) , 30, 100)
submit_button.button.configure(command=lambda: submit(user_input, selected_task, list_of_tasks, message_label))
selected_task = ComboBoxes(gui.window, 490, 10, task_list)
list_of_tasks = ReadOnlyTextBox(gui.window, 460, 50, task_list, 195, 200)
list_of_tasks.textbox.configure(font=("Terminal", 18))
clear_button = Buttons(gui.window, "Clear all", 90, ('Arial', 17), 508, 290)
clear_button.button.configure(command=lambda: clear_tasks(list_of_tasks, selected_task, message_label))
delete_button = Buttons(gui.window, "Delete selected task", 110, ('Arial', 18), 467, 254)
delete_button.button.configure(command=lambda: delete_task(selected_task, list_of_tasks, message_label))
stop_button = ImageButton(gui.window, '', 80, 80, 1000, 1000, 'pausebuttonimage.png', lambda :[stop(),start_button_appear()])
start_button = ImageButton(gui.window, '', 80, 80, 70, 320, 'playbuttonimg.png',  lambda: [start(), start_button_disappear()])
reset_button = ImageButton(gui.window, '', 40, 40, 170, 360, 'resetbutton2.png',  lambda : [reset(), start_button_appear()])

clock_label = Labels(gui.window, f'{variables.hours:02}:{variables.minutes:02}:{variables.seconds:02}', ('Impact', 70), 10, 220)
small_clock_label = Labels(gui.window, f'.{variables.one_tenth_of_a_second:02}', ('Impact', 40), 264, 249)

if __name__ == '__main__':
    update_gui()
    gui.window.mainloop()
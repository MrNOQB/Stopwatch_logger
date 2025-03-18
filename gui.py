from customtkinter import *
from PIL import Image


class MainWindow:
    def __init__(self):
        self.window =  CTk()
        self.window.geometry("640x420")
        self.window.title('Stop_Watch_Logger')
        self.window.resizable(False,False)
        set_appearance_mode("dark")

class Labels:
    def __init__(self,window, text, font, x, y):
        self.label = CTkLabel(window, text=text, font=font)
        self.label.place(x=x,y=y)


class Entries:
    def __init__(self, window, width, font, x, y):
        self.entry = CTkEntry(window, width=width, font=font)
        self.entry.place(x=x, y=y)

class Buttons:
    def __init__(self, window, text, width, font, x, y):
        self.button = CTkButton(window, text=text, width=width, font=font)
        self.button.place(x=x, y=y)


class ComboBoxes:
    def __init__(self, window,  x, y, item_list):
        self.listbox = CTkComboBox(
            window, values= item_list, state='readonly')
        self.listbox.place(x=x, y=y)

class ReadOnlyTextBox:
    def __init__(self, window, x, y, list_items, width, height):
        self.textbox = CTkTextbox(window, width=width, height=height)
        self.textbox.place(x=x, y=y)


        for item in list_items:
            self.textbox.insert("end", item + "\n")


        self.textbox.configure(state="disabled")

class ImageButton:
    def __init__(self, window, text, width, height, x, y, image_path, command):
        pil_image = Image.open(image_path)

        ctk_image = CTkImage(light_image=pil_image, size=(width, height))

        self.button = CTkButton(window, text=text, image=ctk_image, border_width=0, height=30, width=30, command=command)
        self.button.place(x=x, y=y)




import tkinter
from tkinter import PhotoImage

import file_IO
import constants

class Start:
    file_instance = None
    # Window element
    window_element = None
    # Canvas element for logo
    canvas_element = None
    # Input fields
    website_label = None
    website_text_area = None
    email_label = None
    email_text_area = None
    password_label = None
    password_text_area = None
    # Buttons
    generate_password_button = None
    add_entry_button = None

    def __init__(self):
        self.init_ui()
        self.init_file()
        # self.file_instance.write_into_file("test","test","test")

    def init_ui(self):
        print("Start here")
        self.window_element = tkinter.Tk()
        self.window_element.title(constants.TITLE)
        self.window_element.config(background=constants.BACKGROUND_COLOR, padx=10, pady=50)
        self.init_canvas()



    def init_canvas(self):
        self.canvas_element = tkinter.Canvas(width=200, height=200, background=constants.BACKGROUND_COLOR, highlightthickness=0)
        logo_img = PhotoImage(file="images/")
        self.canvas_element.create_image(100, 100, image=logo_img)
        self.canvas_element.grid(row=0, column=1)


    def init_file(self):
        self.file_instance = file_IO.FileIO()

    def enter_data(self):
        website = ""
        email = ""
        password = ""
        self.file_instance.write_into_file(website=website, email=email, password=password)
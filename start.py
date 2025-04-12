import tkinter
from tkinter import PhotoImage, ttk, Scrollbar
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
    message_label = None
    email_text_area = None
    password_label = None
    password_text_area = None
    # Buttons
    generate_password_button = None
    add_entry_button = None

    table = None
    table_data = []

    def __init__(self):
        self.init_file()
        self.table_data = self.file_instance.return_file_data()
        self.init_ui()
        self.init_input_fields()
        self.create_table()
        self.init_canvas()

    def init_ui(self):
        self.window_element = tkinter.Tk()
        self.window_element.title(constants.TITLE)
        self.window_element.config(background=constants.BACKGROUND_COLOR, padx=10, pady=50)

    def init_input_fields(self):
        # Text labels
        self.website_label = tkinter.Label(text="Website*", fg=constants.TEXT_COLOR,
                                           background=constants.BACKGROUND_COLOR,
                                           font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        self.website_label.grid(row=1, column=0)
        self.email_label = tkinter.Label(text="Email*", fg=constants.TEXT_COLOR,
                                        background=constants.BACKGROUND_COLOR,
                                        font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        self.email_label.grid(row=2, column=0)
        self.password_label = tkinter.Label(text="Password*", fg=constants.TEXT_COLOR,
                                        background=constants.BACKGROUND_COLOR,
                                        font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        self.password_label.grid(row=3, column=0)
        self.message_label = tkinter.Label(text="", fg=constants.TEXT_COLOR,
                                        background=constants.BACKGROUND_COLOR,
                                        font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        self.message_label.grid(row=5, column=1)

        # Buttons
        self.generate_password_button = tkinter.Button(text="Generate Password", width=15,
                                           command=self.generate_password, highlightthickness=0)
        self.generate_password_button.grid(row=3, column=2)
        self.add_entry_button = tkinter.Button(text='Add', width=10,
                                            command=self.enter_data, highlightthickness=0)
        self.add_entry_button.grid(row=4, column=1)

        # Text area
        self.website_text_area = tkinter.Text(self.window_element, height=1, width=30)
        self.website_text_area.grid(row=1, column=1, padx=50, pady=5)
        self.email_text_area = tkinter.Text(self.window_element, height=1, width=30)
        self.email_text_area.grid(row=2, column=1, padx=50, pady=5)
        self.password_text_area = tkinter.Text(self.window_element, height=1, width=30)
        self.password_text_area.grid(row=3, column=1, padx=50, pady=5)

    def init_canvas(self):
        try:
            self.canvas_element = tkinter.Canvas(self.window_element, width=200, height=150, background = constants.BACKGROUND_COLOR, highlightthickness = 0)
            logo_img = PhotoImage(file="images/logo.png")
            self.canvas_element.create_image(100, 75, image=logo_img)
            self.canvas_element.grid(row=0, column=1)
            self.window_element.mainloop()
        except tkinter.TclError as e:
            print(f"Error loading image: {e}")

    def init_file(self):
        self.file_instance = file_IO.FileIO()

    def enter_data(self):
        website = self.website_text_area.get("1.0", tkinter.END).strip()
        email = self.email_text_area.get("1.0", tkinter.END).strip()
        password = self.password_text_area.get("1.0", tkinter.END).strip()
        if website != "" and email != "" and password != "":
            self.file_instance.write_into_file(website=website, email=email, password=password)
            self.website_text_area.delete("1.0", tkinter.END)
            self.email_text_area.delete("1.0", tkinter.END)
            self.password_text_area.delete("1.0", tkinter.END)
            self.message_label.config(text="Added")
            self.table_data = self.file_instance.return_file_data()
            self.create_table()
        else:
            self.message_label.config(text="Please enter valid data")

    def delete_data(self, u_id):
        self.file_instance.delete_using_u_id(u_id)
        self.table_data = self.file_instance.return_file_data()
        self.create_table()

    def generate_password(self):
        password_data = self.file_instance.generate_password()
        self.password_text_area.delete("1.0", tkinter.END)
        self.password_text_area.insert(tkinter.END, password_data)

    def copy_to_clipboard(self, event):
        widget = event.widget
        try:
            selected_text = widget.cget("text")
            self.window_element.clipboard_clear()
            self.window_element.clipboard_append(selected_text)
            self.window_element.update()
            self.message_label.config(text=f"Copied: {selected_text}")
        except tkinter.TclError:
            pass  # Click might occur on empty padding

    def create_table(self):
        table_data = self.table_data
        column_width = 190
        # Headers
        header_frame = tkinter.Frame(self.window_element, background=constants.BACKGROUND_COLOR)
        header_frame.grid(row=6, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        header_frame.grid_columnconfigure(0, minsize=column_width)
        header_frame.grid_columnconfigure(1, minsize=column_width)
        header_frame.grid_columnconfigure(2, minsize=column_width)

        website_header = tkinter.Label(header_frame, text="Website", fg=constants.TEXT_COLOR,
                                       background=constants.BACKGROUND_COLOR,
                                       font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        website_header.grid(row=0, column=0, padx=10, pady=2, sticky="w")

        email_header = tkinter.Label(header_frame, text="Email", fg=constants.TEXT_COLOR,
                                     background=constants.BACKGROUND_COLOR,
                                     font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        email_header.grid(row=0, column=1, padx=10, pady=2, sticky="w")

        password_header = tkinter.Label(header_frame, text="Password", fg=constants.TEXT_COLOR,
                                        background=constants.BACKGROUND_COLOR,
                                        font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE, "bold"))
        password_header.grid(row=0, column=2, padx=10, pady=2, sticky="w")

        # Table Frame and Scrollbar
        table_frame = tkinter.Frame(self.window_element, background=constants.BACKGROUND_COLOR)
        table_frame.grid(row=7, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        table_canvas = tkinter.Canvas(table_frame, background=constants.BACKGROUND_COLOR, highlightthickness=0)
        table_canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(table_frame, orient="vertical", command=table_canvas.yview)
        scrollbar.pack(side="right", fill="y")

        table_canvas.configure(yscrollcommand=scrollbar.set)
        table_canvas.bind('<Configure>', lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

        self.table = tkinter.Frame(table_canvas, background=constants.BACKGROUND_COLOR)
        table_canvas.create_window((0, 0), window=self.table, anchor="nw")

        # Configure column widths in the table frame
        self.table.grid_columnconfigure(0, minsize=column_width)
        self.table.grid_columnconfigure(1, minsize=column_width)
        self.table.grid_columnconfigure(2, minsize=column_width)

        for i, row_dict in enumerate(table_data):
            website_label = tkinter.Label(self.table, text=row_dict["website"], fg=constants.TEXT_COLOR,
                                          background=constants.BACKGROUND_COLOR,
                                          font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE),
                                          wraplength=column_width * 0.9,
                                          # Allow a little less than full width for padding
                                          justify="left")
            website_label.grid(row=i, column=0, padx=10, pady=2, sticky="ew")
            website_label.bind("<Button-1>", self.copy_to_clipboard)
            website_label.config(cursor="hand2")

            email_label = tkinter.Label(self.table, text=row_dict["email"], fg=constants.TEXT_COLOR,
                                        background=constants.BACKGROUND_COLOR,
                                        font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE),
                                        wraplength=column_width * 0.9,
                                        justify="left")
            email_label.grid(row=i, column=1, padx=10, pady=2, sticky="ew")
            email_label.bind("<Button-1>", self.copy_to_clipboard)
            email_label.config(cursor="hand2")

            password_label = tkinter.Label(self.table, text=row_dict["password"], fg=constants.TEXT_COLOR,
                                           background=constants.BACKGROUND_COLOR,
                                           font=(constants.FONT_NAME, constants.TEXT_FONT_SIZE),
                                           wraplength=column_width * 0.9,
                                           justify="left")
            password_label.grid(row=i, column=2, padx=10, pady=2, sticky="ew")
            password_label.bind("<Button-1>", self.copy_to_clipboard)
            password_label.config(cursor="hand2")
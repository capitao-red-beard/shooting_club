import tkinter as tk
from tkinter import ttk
import database


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popup_new_user():
    popup = tk.Tk()
    popup.wm_title("Create a New User")

    label_first_name = ttk.Label(popup, text="First Name:").grid(row=0, column=0)
    entry_first_name = ttk.Entry(popup, width=15).grid(row=0, column=1)

    label_last_name = ttk.Label(popup, text="Last Name:").grid(row=1, column=0)
    entry_last_name = ttk.Entry(popup, width=15).grid(row=1, column=1)

    label_user_type = ttk.Label(popup, text="User Type:").grid(row=2, column=0)
    default_value = tk.StringVar(popup)
    default_value.set("select")
    option_menu_user_type = tk.OptionMenu(popup, default_value, "Regular", "Super", "Admin").grid(row=2, column=1)

    label_licence_number = ttk.Label(popup, text="Licence Number:").grid(row=3, column=0)
    entry_licence_number = ttk.Entry(popup, width=15).grid(row=3, column=1)

    label_email = ttk.Label(popup, text="Email:").grid(row=4, column=0)
    entry_email = ttk.Entry(popup, width=15).grid(row=4, column=1)

    label_password = ttk.Label(popup, text="Password:").grid(row=5, column=0)
    entry_password = ttk.Entry(popup, show="*", width=15).grid(row=5, column=1)

    button_submit = ttk.Button(popup, text="Submit").grid(row=6, column=0)
    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=6, column=1)

    popup.pack()
    popup.mainloop()


class ShootingClub(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="logo_16_16.ico")
        tk.Tk.wm_title(self, "Shooting Club")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New User", command=lambda: popup_new_user())
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = ShootingClub()
app.geometry("1280x720")
app.mainloop()

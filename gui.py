import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popup_new_user():
    popup = tk.Tk()
    popup.wm_title("Create a New User")

    label_first_name = ttk.Label(popup, text="First Name:").grid(row=0, column=0)
    value_first_name = tk.StringVar()
    entry_first_name = ttk.Entry(popup, textvariable=value_first_name, width=15).grid(row=0, column=1)

    label_last_name = ttk.Label(popup, text="Last Name:").grid(row=1, column=0)
    value_last_name = tk.StringVar()
    entry_last_name = ttk.Entry(popup, textvariable=value_last_name, width=15).grid(row=1, column=1)

    label_user_type = ttk.Label(popup, text="User Type:").grid(row=2, column=0)
    options = ("Regular", "Admin")
    value_user_type = tk.StringVar(popup)
    value_user_type.set("Select")
    option_menu_user_type = ttk.OptionMenu(popup, value_user_type, options[0], *options).grid(row=2, column=1)

    label_licence_number = ttk.Label(popup, text="Licence Number:").grid(row=3, column=0)
    value_licence_number = tk.StringVar()
    entry_licence_number = ttk.Entry(popup, textvariable=value_licence_number, width=15).grid(row=3, column=1)

    label_email = ttk.Label(popup, text="Email:").grid(row=4, column=0)
    value_email = tk.StringVar()
    entry_email = ttk.Entry(popup, textvariable=value_email, width=15).grid(row=4, column=1)

    label_password = ttk.Label(popup, text="Password:").grid(row=5, column=0)
    value_password = tk.StringVar()
    entry_password = ttk.Entry(popup, show="*", textvariable=value_password, width=15).grid(row=5, column=1)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=6, column=0)

    def clicked():
        result = database.execute_sql('INSERT OR IGNORE INTO user VALUES (' + "'" + value_first_name.get() + "', "
                                      + "'" + value_last_name.get() + "', "
                                      + "'" + value_user_type.get() + "', "
                                      + "'" + value_licence_number.get() + "', "
                                      + "'" + value_email.get() + "', "
                                      + "'" + value_password.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new user into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: CODE=DBF-NU")
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=6, column=1)

    popup.mainloop()


def popup_new_weapon():
    popup = tk.Tk()
    popup.wm_title("Add a New Weapon")

    label_weapon = ttk.Label(popup, text="Weapon Type:").grid(row=0, column=0)

    value = tk.StringVar()
    entry_weapon = ttk.Entry(popup, width=15, textvariable=value).grid(row=0, column=1)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=2, column=0)

    def clicked():
        result = database.execute_sql('INSERT OR IGNORE INTO weapon VALUES (' + "'" + value.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new weapon into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: CODE=DBF-NW")
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=2, column=1)

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

        file_menu.add_command(label="New Weapon", command=lambda: popup_new_weapon())

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=quit, accelerator="Ctrl+Q")

        menu_bar.add_cascade(label="File", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (MainMenu, ScorePage, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Submit a Score", command=lambda: controller.show_frame(ScorePage))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class ScorePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Score Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Score Page", command=lambda: controller.show_frame(ScorePage))
        button2.pack()


app = ShootingClub()
app.geometry("1280x720")
app.mainloop()

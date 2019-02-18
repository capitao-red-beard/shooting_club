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

    label_user_type = ttk.Label(popup, text="Gebruikerstype:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
    options = ("Standaard", "Beheerder")
    value_user_type = tk.StringVar(popup)
    value_user_type.set("Select")
    option_menu_user_type = ttk.OptionMenu(popup, value_user_type, options[0], *options)\
        .grid(row=0, column=1, padx=5, pady=5)

    label_first_name = ttk.Label(popup, text="Voornaam:").grid(row=1, column=0, padx=5, pady=5, sticky="W")
    value_first_name = tk.StringVar()
    entry_first_name = ttk.Entry(popup, textvariable=value_first_name, width=20).grid(row=1, column=1, padx=5, pady=5)

    label_infix = ttk.Label(popup, text="Tussenvoegsel:").grid(row=2, column=0, padx=5, pady=5, sticky="W")
    value_infix = tk.StringVar()
    entry_infix = ttk.Entry(popup, textvariable=value_infix, width=20).grid(row=2, column=1, padx=5, pady=5)

    label_surname = ttk.Label(popup, text="Familienaam:").grid(row=3, column=0, padx=5, pady=5, sticky="W")
    value_surname = tk.StringVar()
    entry_surname = ttk.Entry(popup, textvariable=value_surname, width=20).grid(row=3, column=1, padx=5, pady=5)

    label_date_of_birth = ttk.Label(popup, text="Geboorte Datum:").grid(row=4, column=0, padx=5, pady=5, sticky="W")
    value_date_of_birth = tk.StringVar()
    entry_date_of_birth = ttk.Entry(popup, textvariable=value_date_of_birth, width=20)\
        .grid(row=4, column=1, padx=5, pady=5)

    label_address = ttk.Label(popup, text="Adres:").grid(row=5, column=0, padx=5, pady=5, sticky="W")
    value_address = tk.StringVar()
    entry_address = ttk.Entry(popup, textvariable=value_address, width=20).grid(row=5, column=1, padx=5, pady=5)

    label_city = ttk.Label(popup, text="Woonplaats:").grid(row=6, column=0, padx=5, pady=5, sticky="W")
    value_city = tk.StringVar()
    entry_city = ttk.Entry(popup, textvariable=value_city, width=20).grid(row=6, column=1, padx=5, pady=5)

    label_post_code = ttk.Label(popup, text="Postcode:").grid(row=7, column=0, padx=5, pady=5, sticky="W")
    value_post_code = tk.StringVar()
    entry_post_code = ttk.Entry(popup, textvariable=value_post_code, width=20).grid(row=7, column=1, padx=5, pady=5)

    label_telephone_number = ttk.Label(popup, text="Telefoonnummer:").grid(row=8, column=0, padx=5, pady=5, sticky="W")
    value_telephone_number = tk.StringVar()
    entry_telephone_number = ttk.Entry(popup, textvariable=value_telephone_number, width=20)\
        .grid(row=8, column=1, padx=5, pady=5)

    label_email_address = ttk.Label(popup, text="Email Adres:").grid(row=9, column=0, padx=5, pady=5, sticky="W")
    value_email_address = tk.StringVar()
    entry_email_address = ttk.Entry(popup, textvariable=value_email_address, width=20)\
        .grid(row=9, column=1, padx=5, pady=5)

    label_password = ttk.Label(popup, text="Wachtwoord:").grid(row=10, column=0, padx=5, pady=5, sticky="W")
    value_password = tk.StringVar()
    entry_password = ttk.Entry(popup, show="*", textvariable=value_password, width=20)\
        .grid(row=10, column=1, padx=5, pady=5)

    label_knsa_licence_number = ttk.Label(popup, text="KNSA Licentienummer:")\
        .grid(row=11, column=0, padx=5, pady=5, sticky="W")
    value_knsa_licence_number = tk.StringVar()
    entry_knsa_licence_number = ttk.Entry(popup, textvariable=value_knsa_licence_number, width=20)\
        .grid(row=11, column=1, padx=5, pady=5)

    label_date_of_membership = ttk.Label(popup, text="Datum van Lidmaatschap Ingang:")\
        .grid(row=12, column=0, padx=5, pady=5, sticky="W")
    value_date_of_membership = tk.StringVar()
    entry_date_of_membership = ttk.Entry(popup, textvariable=value_date_of_membership, width=20)\
        .grid(row=12, column=1, padx=5, pady=5)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=13, column=0, padx=10, pady=20)

    def clicked():
        if value_user_type.get() == 'Beheerder':
            user_type = '0'
        else:
            user_type = '1'

        result = database.execute_sql('INSERT OR IGNORE INTO user VALUES ('
                                      + "'" + user_type + "', "
                                      + "'" + value_first_name.get() + "', "
                                      + "'" + value_infix.get() + "', "
                                      + "'" + value_surname.get() + "', "
                                      + "'" + value_date_of_birth.get() + "', "
                                      + "'" + value_address.get() + "', "
                                      + "'" + value_city.get() + "', "
                                      + "'" + value_post_code.get() + "', "
                                      + "'" + value_telephone_number.get() + "', "
                                      + "'" + value_email_address.get() + "', "
                                      + "'" + value_password.get() + "', "
                                      + "'" + value_knsa_licence_number.get() + "', "
                                      + "'" + value_date_of_membership.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new user into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: CODE=DBF-NU")
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=13, column=1, padx=10, pady=20)

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

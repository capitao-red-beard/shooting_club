import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popup_new_user():
    popup = tk.Tk()
    popup.wm_title("Nieuw Lid")

    label_user_type = ttk.Label(popup, text="Gebruikerstype:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    options = ("Standaard", "Beheerder")
    value_user_type = tk.StringVar(popup)
    value_user_type.set("Select")
    option_menu_user_type = ttk.OptionMenu(popup, value_user_type, options[0], *options)\
        .grid(row=0, column=1, padx=5, pady=2)

    label_forename = ttk.Label(popup, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_forename = tk.StringVar()
    entry_forename = ttk.Entry(popup, textvariable=value_forename, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_infix = ttk.Label(popup, text="Tussenvoegsel:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_infix = tk.StringVar()
    entry_infix = ttk.Entry(popup, textvariable=value_infix, width=20).grid(row=2, column=1, padx=5, pady=2)

    label_surname = ttk.Label(popup, text="Familienaam:").grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_surname = tk.StringVar()
    entry_surname = ttk.Entry(popup, textvariable=value_surname, width=20).grid(row=3, column=1, padx=5, pady=2)

    label_date_of_birth = ttk.Label(popup, text="Geboorte Datum (YYYY-MM-DD):")\
        .grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth = tk.StringVar()
    entry_date_of_birth = ttk.Entry(popup, textvariable=value_date_of_birth, width=20)\
        .grid(row=4, column=1, padx=5, pady=2)

    label_address = ttk.Label(popup, text="Adres:").grid(row=5, column=0, padx=5, pady=2, sticky="W")
    value_address = tk.StringVar()
    entry_address = ttk.Entry(popup, textvariable=value_address, width=20).grid(row=5, column=1, padx=5, pady=2)

    label_city = ttk.Label(popup, text="Woonplaats:").grid(row=6, column=0, padx=5, pady=5, sticky="W")
    value_city = tk.StringVar()
    entry_city = ttk.Entry(popup, textvariable=value_city, width=20).grid(row=6, column=1, padx=5, pady=2)

    label_post_code = ttk.Label(popup, text="Postcode:").grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_post_code = tk.StringVar()
    entry_post_code = ttk.Entry(popup, textvariable=value_post_code, width=20).grid(row=7, column=1, padx=5, pady=2)

    label_telephone_number = ttk.Label(popup, text="Telefoonnummer:").grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number = tk.StringVar()
    entry_telephone_number = ttk.Entry(popup, textvariable=value_telephone_number, width=20)\
        .grid(row=8, column=1, padx=5, pady=2)

    label_email_address = ttk.Label(popup, text="Email Adres:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_email_address = tk.StringVar()
    entry_email_address = ttk.Entry(popup, textvariable=value_email_address, width=20)\
        .grid(row=9, column=1, padx=5, pady=2)

    label_password = ttk.Label(popup, text="Wachtwoord:").grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_password = tk.StringVar()
    entry_password = ttk.Entry(popup, show="*", textvariable=value_password, width=20)\
        .grid(row=10, column=1, padx=5, pady=2)

    label_knsa_licence_number = ttk.Label(popup, text="KNSA Licentienummer:")\
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number = tk.StringVar()
    entry_knsa_licence_number = ttk.Entry(popup, textvariable=value_knsa_licence_number, width=20)\
        .grid(row=11, column=1, padx=5, pady=2)

    label_date_of_membership = ttk.Label(popup, text="Datum van Lidmaatschap Ingang (YYYY-MM-DD):")\
        .grid(row=12, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership = tk.StringVar()
    entry_date_of_membership = ttk.Entry(popup, textvariable=value_date_of_membership, width=20)\
        .grid(row=12, column=1, padx=5, pady=2)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked())\
        .grid(row=13, column=0, padx=120, pady=15)

    def clicked():
        if value_user_type.get() == 'Beheerder':
            user_type = '0'
        else:
            user_type = '1'

        result = database.execute_sql('INSERT OR IGNORE INTO member ('
                                      + "'" + user_type + "', "
                                      + "'" + value_forename.get() + "', "
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
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=13, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_new_weapon():
    popup = tk.Tk()
    popup.wm_title("Nieuw Wapen")

    label_weapon = ttk.Label(popup, text="Wapen:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_weapon = tk.StringVar()
    entry_weapon = ttk.Entry(popup, textvariable=value_weapon, width=20).grid(row=0, column=1, padx=5, pady=2)

    label_user_type = ttk.Label(popup, text="Eigenaar Wapen:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    result = database.execute_sql('SELECT knsa_licence_number, first_name, infix, surname FROM user;')
    options = ()
    value_user_type = tk.StringVar(popup)
    value_user_type.set("Select")
    option_menu_user_type = ttk.OptionMenu(popup, value_user_type, options[0], *options)\
        .grid(row=0, column=1, padx=5, pady=2)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=2, column=0, padx=10, pady=15)

    def clicked():
        result = database.execute_sql('INSERT OR IGNORE INTO weapon VALUES (' + "'" + value_weapon.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new weapon into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=2, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_new_ammunition():
    popup = tk.Tk()
    popup.wm_title("Nieuwe Munitie")

    label_type = ttk.Label(popup, text="Munitie Type:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type = tk.StringVar()
    entry_type = ttk.Entry(popup, textvariable=value_type, width=20).grid(row=0, column=1, padx=5, pady=2)

    label_price = ttk.Label(popup, text="Munitie Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price = tk.StringVar()
    entry_price = ttk.Entry(popup, textvariable=value_price, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_stock = ttk.Label(popup, text="Munitie Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock = tk.StringVar()
    entry_stock = ttk.Entry(popup, textvariable=value_stock, width=20).grid(row=2, column=1, padx=5, pady=2)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=3, column=0, padx=10, pady=15)

    def clicked():
        result = database.execute_sql('INSERT OR IGNORE INTO ammunition ('
                                      'ammunition_type, '
                                      'price, '
                                      'stock'
                                      ') VALUES ('
                                      + "'" + value_type.get() + "', "
                                      + "'" + value_price.get() + "', "
                                      + "'" + value_stock.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information",
                                message="Successfully entered a new ammunition type into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_new_card():
    popup = tk.Tk()
    popup.wm_title("Nieuwe Kaart")

    label_score_card = ttk.Label(popup, text="Kaart Type:").grid(row=0, column=0, padx=5, pady=2, sticky="W")

    value_score_card = tk.StringVar()
    entry_score_card = ttk.Entry(popup, textvariable=value_score_card, width=20) \
        .grid(row=0, column=1, padx=5, pady=2)

    label_price = ttk.Label(popup, text="Kaart Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price = tk.StringVar()
    entry_price = ttk.Entry(popup, textvariable=value_price, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_stock = ttk.Label(popup, text="Kaart Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock = tk.StringVar()
    entry_stock = ttk.Entry(popup, textvariable=value_stock, width=20).grid(row=2, column=1, padx=5, pady=2)

    button_submit = ttk.Button(popup, text="Submit", command=lambda: clicked()).grid(row=3, column=0, padx=10, pady=15)

    def clicked():
        result = database.execute_sql('INSERT OR IGNORE INTO ammunition ('
                                      'card_type, '
                                      'price, '
                                      'stock'
                                      ') VALUES ('
                                      + "'" + value_ammunition.get() + "', "
                                      + "'" + value_price.get() + "', "
                                      + "'" + value_stock.get() + "'" + ');')

        if result == 'success':
            messagebox.showinfo(title="Information",
                                message="Successfully entered a new ammunition type into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()

    button_cancel = ttk.Button(popup, text="Cancel", command=popup.destroy).grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


class ShootingClub(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="logo_16_16.ico")
        tk.Tk.wm_title(self, "Schietvereniging - Prinses Juliana")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label="Nieuw Lid", command=lambda: popup_new_user())

        file_menu.add_command(label="Nieuw Wapen", command=lambda: popup_new_weapon())

        file_menu.add_command(label="Nieuwe Munitie", command=lambda: popup_new_ammunition())

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=quit, accelerator="Ctrl+Q")

        menu_bar.add_cascade(label="File", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (MainMenu, ScorePage, FinancePage):

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

        button2 = ttk.Button(self, text="Finance Page", command=lambda: controller.show_frame(FinancePage))
        button2.pack()


class ScorePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Score Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Finance Page", command=lambda: controller.show_frame(FinancePage))
        button2.pack()


class FinancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Finance Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button2 = ttk.Button(self, text="Score Page", command=lambda: controller.show_frame(ScorePage))
        button2.pack()


app = ShootingClub()
app.geometry("1080x720")
app.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popup_user_settings():
    popup = tk.Tk()
    popup.wm_title("Nieuw Lid")

    label_user_type = ttk.Label(popup, text="Gebruikerstype:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    options = ("Standaard", "Beheerder")
    value_user_type = tk.StringVar(popup)
    value_user_type.set("Select")
    option_menu_user_type = ttk.OptionMenu(popup, value_user_type, options[0], *options)\
        .grid(row=0, column=1, padx=5, pady=2)

    label_forename = ttk.Label(popup, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_forename = tk.StringVar(popup)
    entry_forename = ttk.Entry(popup, textvariable=value_forename, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_infix = ttk.Label(popup, text="Tussenvoegsel:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_infix = tk.StringVar(popup)
    entry_infix = ttk.Entry(popup, textvariable=value_infix, width=20).grid(row=2, column=1, padx=5, pady=2)

    label_surname = ttk.Label(popup, text="Familienaam:").grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_surname = tk.StringVar(popup)
    entry_surname = ttk.Entry(popup, textvariable=value_surname, width=20).grid(row=3, column=1, padx=5, pady=2)

    label_date_of_birth = ttk.Label(popup, text="Geboorte Datum (YYYY-MM-DD):")\
        .grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth = tk.StringVar(popup)
    entry_date_of_birth = ttk.Entry(popup, textvariable=value_date_of_birth, width=20)\
        .grid(row=4, column=1, padx=5, pady=2)

    label_address = ttk.Label(popup, text="Adres:").grid(row=5, column=0, padx=5, pady=2, sticky="W")
    value_address = tk.StringVar(popup)
    entry_address = ttk.Entry(popup, textvariable=value_address, width=20).grid(row=5, column=1, padx=5, pady=2)

    label_city = ttk.Label(popup, text="Woonplaats:").grid(row=6, column=0, padx=5, pady=5, sticky="W")
    value_city = tk.StringVar(popup)
    entry_city = ttk.Entry(popup, textvariable=value_city, width=20).grid(row=6, column=1, padx=5, pady=2)

    label_post_code = ttk.Label(popup, text="Postcode:").grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_post_code = tk.StringVar(popup)
    entry_post_code = ttk.Entry(popup, textvariable=value_post_code, width=20).grid(row=7, column=1, padx=5, pady=2)

    label_telephone_number = ttk.Label(popup, text="Telefoonnummer:").grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number = tk.StringVar(popup)
    entry_telephone_number = ttk.Entry(popup, textvariable=value_telephone_number, width=20)\
        .grid(row=8, column=1, padx=5, pady=2)

    label_email_address = ttk.Label(popup, text="Email Adres:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_email_address = tk.StringVar(popup)
    entry_email_address = ttk.Entry(popup, textvariable=value_email_address, width=20)\
        .grid(row=9, column=1, padx=5, pady=2)

    label_password = ttk.Label(popup, text="Wachtwoord:").grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_password = tk.StringVar(popup)
    entry_password = ttk.Entry(popup, show="*", textvariable=value_password, width=20)\
        .grid(row=10, column=1, padx=5, pady=2)

    label_knsa_licence_number = ttk.Label(popup, text="KNSA Licentienummer:")\
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number = tk.StringVar(popup)
    entry_knsa_licence_number = ttk.Entry(popup, textvariable=value_knsa_licence_number, width=20)\
        .grid(row=11, column=1, padx=5, pady=2)

    label_date_of_membership = ttk.Label(popup, text="Datum van Lidmaatschap Ingang (YYYY-MM-DD):")\
        .grid(row=12, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership = tk.StringVar(popup)
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


# popup for the settings of firearm settings
def popup_firearm_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Vuurwapen Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    # creation of the new tab
    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuw")

    label_type_new = ttk.Label(tab_new, text="Type vuurwapen:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_new = tk.StringVar(tab_new)
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20).grid(row=0, column=1, padx=5, pady=2)

    label_users_new = ttk.Label(tab_new, text="Eigenaar:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    options = users
    value_users_new = tk.StringVar(tab_new)
    value_users_new.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_new, value_users_new, options[0], *options) \
        .grid(row=1, column=1, padx=5, pady=2)

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new())\
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_new():
        print('Clicked')

        '''if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuwe munitietype in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_new)
        popup.destroy()'''

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy)\
        .grid(row=2, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk")

    label_existing_edit = ttk.Label(tab_edit, text="Vuurwapen te bewerken:")\
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    firearms = database.execute_sql('''SELECT owner, type FROM firearm;''')
    options = firearms
    value_existing_edit = tk.StringVar(tab_edit)
    value_existing_edit.set("Select")
    option_menu_existing_edit = ttk.OptionMenu(tab_edit, value_existing_edit, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    label_type_edit = ttk.Label(tab_edit, text="Nieuw type:")\
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit = value_existing_edit
    entry_type_edit = ttk.Entry(tab_edit, textvariable=value_type_edit, width=20)\
        .grid(row=1, column=1, padx=5, pady=2)

    label_users_edit = ttk.Label(tab_edit, text="Nieuwe eigenaar:")\
        .grid(row=2, column=0, padx=5, pady=2, sticky="W")
    options = users
    value_users_edit = tk.StringVar(tab_edit)
    value_users_edit.set("Select")
    option_menu_users_edit = ttk.OptionMenu(tab_edit, value_users_edit, options[0], *options) \
        .grid(row=2, column=1, padx=5, pady=2)

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # if the submit button is clicked then we will need to check which value is filled,
    # based on this we need to either, get stock value, add it to the new value and submit it
    # or update the price of the ammunition and submit it
    def clicked_edit():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy)\
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Vuurwapen te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    options = firearms
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


# popup for the settings of ammunition
def popup_ammunition_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Munitie Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    # creation of the new tab
    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuwe")

    label_type_new = ttk.Label(tab_new, text="Type munitie:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_new = tk.StringVar(tab_new)
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20).grid(row=0, column=1, padx=5, pady=2)

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.StringVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.StringVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20).grid(row=2, column=1, padx=5, pady=2)

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new())\
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        print('Clicked')

        '''if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuwe munitietype in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_new)
        popup.destroy()'''

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy)\
        .grid(row=3, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk")

    label_type_edit = ttk.Label(tab_edit, text="Munitie te bewerken:")\
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    ammunition_types = database.execute_sql('''SELECT type FROM ammunition;''')
    options = ammunition_types
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    label_price_edit = ttk.Label(tab_edit, text="Nieuwe prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_edit = tk.StringVar(tab_edit)
    entry_price_edit = ttk.Entry(tab_edit, textvariable=value_price_edit, width=20)\
        .grid(row=1, column=1, padx=5, pady=2)

    label_stock_edit = ttk.Label(tab_edit, text="Voorraad toevoegen:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_edit = tk.StringVar(tab_edit)
    entry_stock_edit = ttk.Entry(tab_edit, textvariable=value_stock_edit, width=20)\
        .grid(row=2, column=1, padx=5, pady=2)

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # if the submit button is clicked then we will need to check which value is filled,
    # based on this we need to either, get stock value, add it to the new value and submit it
    # or update the price of the ammunition and submit it
    def clicked_edit():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy)\
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete= ttk.Label(tab_delete, text="Munitie te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    options = ammunition_types
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


# popup for scorecard settings
def popup_scorecard_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Score Kaart Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    # creation of the new tab
    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuwe")

    label_type_new = ttk.Label(tab_new, text="Type kaart:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_new = tk.StringVar(tab_new)
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20).grid(row=0, column=1, padx=5, pady=2)

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.StringVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20).grid(row=1, column=1, padx=5, pady=2)

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.StringVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20).grid(row=2, column=1, padx=5, pady=2)

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        print('Clicked')

        '''if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuwe munitietype in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_new)
        popup.destroy()'''

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk")

    label_type_edit = ttk.Label(tab_edit, text="Score kaart te bewerken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    ammunition_types = database.execute_sql('''SELECT type FROM scorecard;''')
    options = ammunition_types
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    label_price_edit = ttk.Label(tab_edit, text="Nieuwe Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_edit = tk.StringVar(tab_edit)
    entry_price_edit = ttk.Entry(tab_edit, textvariable=value_price_edit, width=20) \
        .grid(row=1, column=1, padx=5, pady=2)

    label_stock_edit = ttk.Label(tab_edit, text="Voorraad toevoegen:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_edit = tk.StringVar(tab_edit)
    entry_stock_edit = ttk.Entry(tab_edit, textvariable=value_stock_edit, width=20) \
        .grid(row=2, column=1, padx=5, pady=2)

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # if the submit button is clicked then we will need to check which value is filled,
    # based on this we need to either, get stock value, add it to the new value and submit it
    # or update the price of the ammunition and submit it
    def clicked_edit():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Score kaart te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    options = ammunition_types
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, options[0], *options) \
        .grid(row=0, column=1, padx=5, pady=2)

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        print('Clicked')

        '''if result_edit == 'success':
            messagebox.showinfo(title="Information", message=
                                "Het systeem heeft met succes nieuwe voorraad in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data: " + result_edit)
        popup.destroy()'''

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

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

        file_menu.add_command(label="Lid Instellingen", command=lambda: popup_user_settings())

        file_menu.add_command(label="Vuurapen Instellingen", command=lambda: popup_firearm_settings())

        file_menu.add_command(label="Munitie Instellingen", command=lambda: popup_ammunition_settings())

        file_menu.add_command(label="Score Kaart Instellingen", command=lambda: popup_scorecard_settings())

        file_menu.add_separator()

        file_menu.add_command(label="Sluiten", command=quit, accelerator="Ctrl+Q")

        menu_bar.add_cascade(label="Instellingen", menu=file_menu)

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

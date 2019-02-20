import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database


LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


# popup for the settings of users
def popup_user_settings():
    popup = tk.Tk()
    popup.wm_title("Lid Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuw Lid")

    label_user_type_new = ttk.Label(tab_new, text="Gebruikerstype:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    user_types = ("Standaard", "Beheerder")
    value_user_type_new = tk.StringVar(tab_new)
    value_user_type_new.set("Select")
    option_menu_user_type_new = ttk.OptionMenu(tab_new, value_user_type_new, user_types[0], *user_types)\
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_first_name_new = ttk.Label(tab_new, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_first_name_new = tk.StringVar(tab_new)
    entry_first_name_new = ttk.Entry(tab_new, textvariable=value_first_name_new, width=20)\
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_last_name_new = ttk.Label(tab_new, text="Familienaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_last_name_new = tk.StringVar(tab_new)
    entry_last_name_new = ttk.Entry(tab_new, textvariable=value_last_name_new, width=20)\
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_date_of_birth_new = ttk.Label(tab_new, text="Geboorte Datum (YYYY-MM-DD):")\
        .grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth_new = tk.StringVar(tab_new)
    entry_date_of_birth_new = ttk.Entry(tab_new, textvariable=value_date_of_birth_new, width=20)\
        .grid(row=3, column=1, padx=5, pady=2, sticky="W")

    label_address_new = ttk.Label(tab_new, text="Adres:").grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_address_new = tk.StringVar(tab_new)
    entry_address_new = ttk.Entry(tab_new, textvariable=value_address_new, width=20)\
        .grid(row=4, column=1, padx=5, pady=2)

    label_city_new = ttk.Label(tab_new, text="Woonplaats:").grid(row=5, column=0, padx=5, pady=5, sticky="W")
    value_city_new = tk.StringVar(tab_new)
    entry_city_new = ttk.Entry(tab_new, textvariable=value_city_new, width=20)\
        .grid(row=5, column=1, padx=5, pady=2, sticky="W")

    label_post_code_new = ttk.Label(tab_new, text="Postcode:").grid(row=6, column=0, padx=5, pady=2, sticky="W")
    value_post_code_new = tk.StringVar(tab_new)
    entry_post_code_new = ttk.Entry(tab_new, textvariable=value_post_code_new, width=20)\
        .grid(row=6, column=1, padx=5, pady=2, sticky="W")

    label_telephone_number_new = ttk.Label(tab_new, text="Telefoonnummer:")\
        .grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number_new = tk.StringVar(tab_new)
    entry_telephone_number_new = ttk.Entry(tab_new, textvariable=value_telephone_number_new, width=20)\
        .grid(row=7, column=1, padx=5, pady=2, sticky="W")

    label_email_address_new = ttk.Label(tab_new, text="Email Adres:").grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_email_address_new = tk.StringVar(tab_new)
    entry_email_address_new = ttk.Entry(tab_new, textvariable=value_email_address_new, width=20)\
        .grid(row=8, column=1, padx=5, pady=2, sticky="W")

    label_password_new = ttk.Label(tab_new, text="Wachtwoord:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_password_new = tk.StringVar(tab_new)
    entry_password_new = ttk.Entry(tab_new, show="*", textvariable=value_password_new, width=20)\
        .grid(row=9, column=1, padx=5, pady=2, sticky="W")

    label_knsa_licence_number_new = ttk.Label(tab_new, text="KNSA Licentienummer:")\
        .grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number_new = tk.StringVar(tab_new)
    entry_knsa_licence_number_new = ttk.Entry(tab_new, textvariable=value_knsa_licence_number_new, width=20)\
        .grid(row=10, column=1, padx=5, pady=2, sticky="W")

    label_date_of_membership_new = ttk.Label(tab_new, text="Datum van Lidmaatschap Ingang (YYYY-MM-DD):")\
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership_new = tk.StringVar(tab_new)
    entry_date_of_membership_new = ttk.Entry(tab_new, textvariable=value_date_of_membership_new, width=20)\
        .grid(row=11, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new())\
        .grid(row=12, column=0, padx=120, pady=15)

    def clicked_new():
        print('Clicked')

        '''if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new user into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()'''

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy)\
        .grid(row=12, column=1, padx=10, pady=15)

    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk Lid")

    label_users_edit = ttk.Label(tab_edit, text="Lid te Berwerken:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    value_user_edit = tk.StringVar(tab_edit)
    value_user_edit.set("Select")
    option_menu_user_edit = ttk.OptionMenu(tab_edit, value_user_edit, users[0], *users) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_user_type_edit = ttk.Label(tab_edit, text="Gebruikerstype:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_user_type_edit = tk.StringVar(tab_edit)
    value_user_type_edit.set("Select")
    option_menu_user_type_edit = ttk.OptionMenu(tab_edit, value_user_type_new, user_types[0], *user_types) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_first_name_edit = ttk.Label(tab_edit, text="Voornaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_first_name_edit = tk.StringVar(tab_edit)
    entry_first_name_edit = ttk.Entry(tab_edit, textvariable=value_first_name_edit, width=20)\
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_last_name_edit = ttk.Label(tab_edit, text="Familienaam:").grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_last_name_edit = tk.StringVar(tab_edit)
    entry_last_name_edit = ttk.Entry(tab_edit, textvariable=value_last_name_edit, width=20)\
        .grid(row=3, column=1, padx=5, pady=2, sticky="W")

    label_address_edit = ttk.Label(tab_edit, text="Adres:").grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_address_edit = tk.StringVar(tab_edit)
    entry_address_edit = ttk.Entry(tab_edit, textvariable=value_address_edit, width=20) \
        .grid(row=4, column=1, padx=5, pady=2, sticky="W")

    label_city_edit = ttk.Label(tab_edit, text="Woonplaats:").grid(row=5, column=0, padx=5, pady=5, sticky="W")
    value_city_edit = tk.StringVar(tab_edit)
    entry_city_edit = ttk.Entry(tab_edit, textvariable=value_city_new, width=20)\
        .grid(row=5, column=1, padx=5, pady=2, sticky="W")

    label_post_code_edit = ttk.Label(tab_edit, text="Postcode:").grid(row=6, column=0, padx=5, pady=2, sticky="W")
    value_post_code_edit = tk.StringVar(tab_edit)
    entry_post_code_edit = ttk.Entry(tab_edit, textvariable=value_post_code_edit, width=20) \
        .grid(row=6, column=1, padx=5, pady=2, sticky="W")

    label_telephone_number_edit = ttk.Label(tab_edit, text="Telefoonnummer:")\
        .grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number_edit = tk.StringVar(tab_edit)
    entry_telephone_number_edit = ttk.Entry(tab_edit, textvariable=value_telephone_number_edit, width=20) \
        .grid(row=7, column=1, padx=5, pady=2, sticky="W")

    label_email_address_edit = ttk.Label(tab_edit, text="Email Adres:")\
        .grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_email_address_edit = tk.StringVar(tab_edit)
    entry_email_address_edit = ttk.Entry(tab_edit, textvariable=value_email_address_edit, width=20) \
        .grid(row=8, column=1, padx=5, pady=2, sticky="W")

    label_password_edit = ttk.Label(tab_edit, text="Wachtwoord:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_password_edit = tk.StringVar(tab_edit)
    entry_password_edit = ttk.Entry(tab_edit, show="*", textvariable=value_password_edit, width=20) \
        .grid(row=9, column=1, padx=5, pady=2, sticky="W")

    label_knsa_licence_number_edit = ttk.Label(tab_edit, text="KNSA Licentienummer:") \
        .grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number_edit = tk.StringVar(tab_edit)
    entry_knsa_licence_number_edit = ttk.Entry(tab_edit, textvariable=value_knsa_licence_number_edit, width=20) \
        .grid(row=10, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
        .grid(row=11, column=0, padx=120, pady=15)

    def clicked_edit():
        print('Clicked')

        '''if result == 'success':
            messagebox.showinfo(title="Information", message="Successfully entered a new user into the database.")
        else:
            messagebox.showerror(title="Error", message="An error occurred: " + result)
        popup.destroy()'''

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=11, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder Lid")

    label_user_delete = ttk.Label(tab_delete, text="Lid te Verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_user_delete = tk.StringVar(tab_delete)
    value_user_delete.set("Select")
    option_menu_user_delete = ttk.OptionMenu(tab_delete, value_user_delete, users[0], *users) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

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


# popup for the settings of firearm
def popup_firearm_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Vuurwapen Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    # creation of the new tab
    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuwe Vuurwapen")

    label_type_new = ttk.Label(tab_new, text="Type Vuurwapen:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_new = tk.StringVar(tab_new)
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20)\
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_users_new = ttk.Label(tab_new, text="Eigenaar:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    value_users_new = tk.StringVar(tab_new)
    value_users_new.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_new, value_users_new, users[0], *users) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

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
    notebook.add(tab_edit, text="Bewerk Vuurwapen")

    label_existing_edit = ttk.Label(tab_edit, text="Vuurwapen te Bewerken:")\
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    firearms = database.execute_sql('''SELECT owner, type FROM firearm;''')
    value_existing_edit = tk.StringVar(tab_edit)
    value_existing_edit.set("Select")
    option_menu_existing_edit = ttk.OptionMenu(tab_edit, value_existing_edit, firearms[0], *firearms) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_type_edit = ttk.Label(tab_edit, text="Nieuw Type:")\
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit = value_existing_edit
    entry_type_edit = ttk.Entry(tab_edit, textvariable=value_type_edit, width=20)\
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_users_edit = ttk.Label(tab_edit, text="Nieuwe Eigenaar:")\
        .grid(row=2, column=0, padx=5, pady=2, sticky="W")
    options = users
    value_users_edit = tk.StringVar(tab_edit)
    value_users_edit.set("Select")
    option_menu_users_edit = ttk.OptionMenu(tab_edit, value_users_edit, options[0], *options) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
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
    notebook.add(tab_delete, text="Verwijder Vuurwapen")

    label_type_delete = ttk.Label(tab_delete, text="Vuurwapen te Verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, firearms[0], *firearms) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15, sticky="W")

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
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20)\
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.StringVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20)\
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.StringVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20)\
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

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
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_edit = ttk.Label(tab_edit, text="Nieuwe prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_edit = tk.StringVar(tab_edit)
    entry_price_edit = ttk.Entry(tab_edit, textvariable=value_price_edit, width=20)\
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_edit = ttk.Label(tab_edit, text="Voorraad toevoegen:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_edit = tk.StringVar(tab_edit)
    entry_stock_edit = ttk.Entry(tab_edit, textvariable=value_stock_edit, width=20)\
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

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
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

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
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20)\
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.StringVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20)\
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.StringVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20)\
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

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
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_edit = ttk.Label(tab_edit, text="Nieuwe Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_edit = tk.StringVar(tab_edit)
    entry_price_edit = ttk.Entry(tab_edit, textvariable=value_price_edit, width=20) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_edit = ttk.Label(tab_edit, text="Voorraad toevoegen:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_edit = tk.StringVar(tab_edit)
    entry_stock_edit = ttk.Entry(tab_edit, textvariable=value_stock_edit, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

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
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

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

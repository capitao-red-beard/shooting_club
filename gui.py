import tkinter as tk
from datetime import date
from tkinter import messagebox
from tkinter import ttk

import database

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


# popup for the settings of users (1 ERROR / USER TYPE NOT ENTERING INTO DATABASE)
def popup_user_settings():
    popup = tk.Tk()
    popup.wm_title("Lid Instellingen")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuw Lid")

    fields = {
        'Standaard': 1,
        'Beheerder': 2
    }

    label_user_type_new = ttk.Label(tab_new, text="Gebruikerstype:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_user_type_new = tk.StringVar(tab_new)
    value_user_type_new.set("Select")
    option_menu_user_type_new = ttk.OptionMenu(tab_new, value_user_type_new, next(iter(fields)), *fields.keys()) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_first_name_new = ttk.Label(tab_new, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_first_name_new = tk.StringVar(tab_new)
    entry_first_name_new = ttk.Entry(tab_new, textvariable=value_first_name_new, width=20) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_last_name_new = ttk.Label(tab_new, text="Familienaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_last_name_new = tk.StringVar(tab_new)
    entry_last_name_new = ttk.Entry(tab_new, textvariable=value_last_name_new, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_date_of_birth_new = ttk.Label(tab_new, text="Geboorte Datum (YYYY-MM-DD):") \
        .grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth_new = tk.StringVar(tab_new)
    entry_date_of_birth_new = ttk.Entry(tab_new, textvariable=value_date_of_birth_new, width=20) \
        .grid(row=3, column=1, padx=5, pady=2, sticky="W")

    label_address_new = ttk.Label(tab_new, text="Adres:").grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_address_new = tk.StringVar(tab_new)
    entry_address_new = ttk.Entry(tab_new, textvariable=value_address_new, width=20) \
        .grid(row=4, column=1, padx=5, pady=2)

    label_city_new = ttk.Label(tab_new, text="Woonplaats:").grid(row=5, column=0, padx=5, pady=5, sticky="W")
    value_city_new = tk.StringVar(tab_new)
    entry_city_new = ttk.Entry(tab_new, textvariable=value_city_new, width=20) \
        .grid(row=5, column=1, padx=5, pady=2, sticky="W")

    label_post_code_new = ttk.Label(tab_new, text="Postcode:").grid(row=6, column=0, padx=5, pady=2, sticky="W")
    value_post_code_new = tk.StringVar(tab_new)
    entry_post_code_new = ttk.Entry(tab_new, textvariable=value_post_code_new, width=20) \
        .grid(row=6, column=1, padx=5, pady=2, sticky="W")

    label_telephone_number_new = ttk.Label(tab_new, text="Telefoonnummer:") \
        .grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number_new = tk.StringVar(tab_new)
    entry_telephone_number_new = ttk.Entry(tab_new, textvariable=value_telephone_number_new, width=20) \
        .grid(row=7, column=1, padx=5, pady=2, sticky="W")

    label_email_address_new = ttk.Label(tab_new, text="Email Adres:").grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_email_address_new = tk.StringVar(tab_new)
    entry_email_address_new = ttk.Entry(tab_new, textvariable=value_email_address_new, width=20) \
        .grid(row=8, column=1, padx=5, pady=2, sticky="W")

    label_password_new = ttk.Label(tab_new, text="Wachtwoord:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_password_new = tk.StringVar(tab_new)
    entry_password_new = ttk.Entry(tab_new, show="*", textvariable=value_password_new, width=20) \
        .grid(row=9, column=1, padx=5, pady=2, sticky="W")

    label_knsa_licence_number_new = ttk.Label(tab_new, text="KNSA Licentienummer:") \
        .grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number_new = tk.StringVar(tab_new)
    entry_knsa_licence_number_new = ttk.Entry(tab_new, textvariable=value_knsa_licence_number_new, width=20) \
        .grid(row=10, column=1, padx=5, pady=2, sticky="W")

    label_date_of_membership_new = ttk.Label(tab_new, text="Datum van Lidmaatschap Ingang (YYYY-MM-DD):") \
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership_new = tk.StringVar(tab_new)
    entry_date_of_membership_new = ttk.Entry(tab_new, textvariable=value_date_of_membership_new, width=20) \
        .grid(row=11, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=12, column=0, padx=10, pady=15)

    # TODO fix the issue that user type is not being entered into the database
    def clicked_new():
        result_new = database.execute_sql('''INSERT OR IGNORE INTO user (
                type, 
                first_name,
                last_name, 
                date_of_birth, 
                address, 
                city, 
                post_code, 
                telephone_number, 
                email_address, 
                password, 
                knsa_licence_number, 
                date_of_membership
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);''', (
            fields.get(value_user_type_new.get()),
            value_first_name_new.get().lower(),
            value_last_name_new.get().lower(),
            value_date_of_birth_new.get().lower(),
            value_address_new.get().lower(),
            value_city_new.get().lower(),
            value_post_code_new.get().lower(),
            value_telephone_number_new.get().lower(),
            value_email_address_new.get().lower(),
            value_password_new.get().lower(),
            value_knsa_licence_number_new.get().lower(),
            value_date_of_membership_new.get().lower()))

        if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuw lid "
                                        + value_first_name_new.get() + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=12, column=1, padx=10, pady=15)

    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk Lid")

    label_users_edit = ttk.Label(tab_edit, text="Lid te Berwerken:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    value_user_edit = tk.StringVar(tab_edit)
    value_user_edit.set("Select")
    option_menu_user_edit = ttk.OptionMenu(tab_edit, value_user_edit, users[0], *users) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    fields = {'Adres': 'address',
              'Woonplaats': 'city',
              'Postcode': 'post_code',
              'Telefoonnummer': 'telephone_number',
              'Email Adres': 'email_address',
              'KNSA Licentienummer': 'knsa_licence_number'}

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_user_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields)), *fields.keys()) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.StringVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        result_edit = database.execute_sql('UPDATE user SET ' + fields.get(value_field_edit.get())
                                           + ' = ? WHERE  knsa_licence_number = ?',
                                           (value_update_edit.get().lower(), value_user_edit.get()[2:8]))

        if result_edit == 'success':
            messagebox.showinfo(title="Information", message="Het systeem heeft met succes het lid "
                                                             + value_user_edit.get()[2:8] + " aangepast")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

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
        result_delete = database.execute_sql(
            '''DELETE FROM user WHERE knsa_licence_number = ?;''', (value_user_delete.get()[2:8],))

        if result_delete == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes het lid "
                                        + value_user_delete.get()[0] + " verwijderd")
        else:
            messagebox.showerror(title="Error",
                                 message="Er was een fout bij het verwijderen van deze lid")
        popup.destroy()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


# popup for the settings of firearm (FINISHED)
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
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_users_new = ttk.Label(tab_new, text="Eigenaar:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    value_users_new = tk.StringVar(tab_new)
    value_users_new.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_new, value_users_new, users[0], *users) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_new():
        result_new = database.execute_sql('''INSERT OR IGNORE INTO firearm (
        type, owner) VALUES (?, ?)''', (value_type_new.get().lower(), value_users_new.get()[2:8]))

        if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuw vuurwapen "
                                        + value_type_new.get().lower() + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=2, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk Vuurwapen")

    label_existing_edit = ttk.Label(tab_edit, text="Vuurwapen te Bewerken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    firearms = database.execute_sql('''SELECT owner, type FROM firearm;''')
    value_existing_edit = tk.StringVar(tab_edit)
    value_existing_edit.set("Select")
    option_menu_existing_edit = ttk.OptionMenu(tab_edit, value_existing_edit, firearms[0], *firearms) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_users_edit = ttk.Label(tab_edit, text="Nieuwe Eigenaar:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_users_edit = tk.StringVar(tab_edit)
    value_users_edit.set("Select")
    option_menu_users_edit = ttk.OptionMenu(tab_edit, value_users_edit, users[0], *users) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_edit():
        result_edit = database.execute_sql('''UPDATE firearm SET owner = ? WHERE owner = ?''',
                                           (value_users_edit.get()[2:8], value_existing_edit.get()[2:8]))

        if result_edit == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes het vuurwapen eigenaar aangepast van "
                                        + value_existing_edit.get()[2:8] + " tot "
                                        + value_users_edit.get()[2:8].lower())
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=2, column=1, padx=10, pady=15)

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
        result_delete = database.execute_sql(
            '''DELETE FROM firearm WHERE type = ? AND owner = ?''',
            (value_type_delete.get()[12:-2], value_type_delete.get()[2:8]))

        if result_delete == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes het vuurwapen "
                                        + value_type_delete.get()[0].lower() + " verwijderd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


# popup for the settings of ammunition (FINISHED)
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
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.DoubleVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.IntVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        result_new = database.execute_sql('''INSERT OR IGNORE INTO ammunition (
        type, price, stock) VALUES (?, ?, ?)''',
                                          (value_type_new.get().lower(), value_price_new.get(), value_stock_new.get()))

        if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuwe munitietype "
                                        + value_type_new.get().lower() + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk")

    fields = {
        'Prijs': 'price',
        'Voorraad': 'stock'
    }

    label_type_edit = ttk.Label(tab_edit, text="Munitie te bewerken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    ammunition_types = database.execute_sql('''SELECT type FROM ammunition;''')
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, ammunition_types[0], *ammunition_types) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_value_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields)), *fields.keys()) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        if fields.get(value_field_edit.get()) == 'stock':
            current_stock = database.execute_sql('''SELECT stock from ammunition WHERE type = ?''',
                                                 (value_type_edit.get()[2:5],))
            new_value = int(current_stock[0][0] + value_update_edit.get())
        else:
            new_value = value_update_edit.get()

        result_edit = database.execute_sql('UPDATE ammunition SET ' + fields.get(value_field_edit.get())
                                           + ' = ? WHERE type = ?',
                                           (new_value, value_type_edit.get()[2:5]))

        if result_edit == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes nieuwe " + value_field_edit.get().lower()
                                        + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Munitie te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, ammunition_types[0], *ammunition_types) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        result_delete = database.execute_sql('''DELETE FROM ammunition WHERE type = ?''',
                                             (value_type_delete.get()[2:-3]), )

        if result_delete == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes de ammunitie "
                                        + value_type_delete.get().lower() + " verwijderd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
        popup.destroy()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


# popup for scorecard settings (FINISHED)
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
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_new = ttk.Label(tab_new, text="Prijs (EUR):").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_new = tk.DoubleVar(tab_new)
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=20) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.IntVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        result_new = database.execute_sql('''INSERT OR IGNORE INTO scorecard (
                type, price, stock) VALUES (?, ?, ?)''',
                                          (value_type_new.get().lower(), value_price_new.get(), value_stock_new.get()))

        if result_new == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een nieuwe scorecard "
                                        + value_type_new.get().lower() + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    # creation of the edit tab
    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk")

    fields = {
        'Prijs': 'price',
        'Voorraad': 'stock'
    }

    fields2 = {
        'Standaard': 'regular',
        'Competitie': 'competition'
    }

    label_type_edit = ttk.Label(tab_edit, text="Score kaart te bewerken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")

    scorecard_types = database.execute_sql('''SELECT type FROM scorecard;''')
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, next(iter(fields2)), *fields2.keys()) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_value_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields)), *fields.keys()) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=20) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        if fields.get(value_field_edit.get()) == 'stock':
            print(fields2.get(value_type_edit.get()))
            current_stock = database.execute_sql('''SELECT stock from scorecard WHERE type = ?''',
                                                 (fields2.get(value_type_edit.get()),))
            new_value = int(current_stock[0][0] + value_update_edit.get())
        else:
            new_value = value_update_edit.get()

        result_edit = database.execute_sql('UPDATE scorecard SET ' + fields.get(value_field_edit.get())
                                           + ' = ? WHERE type = ?',
                                           (new_value, fields2.get(value_type_edit.get())))

        if result_edit == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes nieuwe " + value_field_edit.get().lower()
                                        + " in de database ingevoerd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
        popup.destroy()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Score kaart te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, scorecard_types[0], *scorecard_types) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        result_delete = database.execute_sql('''DELETE FROM scorecard WHERE type = ?''',
                                             (fields.get(value_type_delete.get()),))

        if result_delete == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes de scorecard " + value_type_delete.get().lower()
                                        + " verwijderd")
        else:
            messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
        popup.destroy()

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

        button1 = ttk.Button(self, text="Score Page", command=lambda: controller.show_frame(ScorePage))
        button1.pack()

        button2 = ttk.Button(self, text="Finance Page", command=lambda: controller.show_frame(FinancePage))
        button2.pack()


# TODO add email functionality to mail the scores to the user also add total scores for both cards
class ScorePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Frame.__init__(self, parent)
        frame_left = tk.Frame(self)
        frame_left.pack(side="left")

        button_main_menu = ttk.Button(frame_left, text="Main Menu",
                                      command=lambda: controller.show_frame(MainMenu))
        button_main_menu.pack()

        button_finance_page = ttk.Button(frame_left, text="Finance Page",
                                         command=lambda: controller.show_frame(FinancePage))
        button_finance_page.pack()

        frame_right = tk.Frame(self)
        frame_right.pack(side="right", fill='both', expand=True)

        label_frame_left = tk.LabelFrame(frame_right, text="Submit Score")
        label_frame_left.pack(side="left", fill="both", expand=True)

        label_details = tk.Frame(label_frame_left)
        label_details.pack(side="top", anchor="nw")

        label_user_left = ttk.Label(label_details, text="Lid:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_left = tk.StringVar(label_details)
        value_user_left.set("Select")
        option_menu_user_left = ttk.OptionMenu(label_details, value_user_left, users[0], *users) \
            .grid(row=0, column=1, padx=5, pady=5, sticky="W")

        label_firearm_left = ttk.Label(label_details, text="Vuurwapen:") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="W")

        firearms = database.execute_sql('''SELECT owner, type FROM firearm;''')
        value_firearm_left = tk.StringVar(label_details)
        value_firearm_left.set("Select")
        option_menu_scorecard_left = ttk.OptionMenu(
            label_details, value_firearm_left, firearms[0], *firearms) \
            .grid(row=1, column=1, padx=5, pady=5, sticky="W")

        frame_scores = tk.Frame(label_frame_left)
        frame_scores.pack(anchor="w")

        label_scorecard1 = ttk.Label(frame_scores, text="1e Scorecard:") \
            .grid(row=2, column=0, padx=5, pady=5, sticky="W")

        value_scorecard1_shot1 = tk.IntVar(frame_scores)
        entry_scorecard1_shot1 = ttk.Entry(frame_scores, textvariable=value_scorecard1_shot1, width=5) \
            .grid(row=2, column=2, padx=5, pady=5, sticky="W")

        value_scorecard1_shot2 = tk.IntVar(frame_scores)
        entry_scorecard1_shot2 = ttk.Entry(frame_scores, textvariable=value_scorecard1_shot2, width=5) \
            .grid(row=2, column=3, padx=5, pady=5, sticky="W")

        value_scorecard1_shot3 = tk.IntVar(frame_scores)
        entry_scorecard1_shot3 = ttk.Entry(frame_scores, textvariable=value_scorecard1_shot3, width=5) \
            .grid(row=2, column=4, padx=5, pady=5, sticky="W")

        value_scorecard1_shot4 = tk.IntVar(frame_scores)
        entry_scorecard1_shot4 = ttk.Entry(frame_scores, textvariable=value_scorecard1_shot4, width=5) \
            .grid(row=2, column=5, padx=5, pady=5, sticky="W")

        value_scorecard1_shot5 = tk.IntVar(frame_scores)
        entry_scorecard1_shot5 = ttk.Entry(frame_scores, textvariable=value_scorecard1_shot5, width=5) \
            .grid(row=2, column=6, padx=5, pady=5, sticky="W")

        label_scorecard_2 = ttk.Label(frame_scores, text="2e Scorecard:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="W")

        value_scorecard2_shot1 = tk.IntVar(frame_scores)
        entry_scorecard2_shot1 = ttk.Entry(frame_scores, textvariable=value_scorecard2_shot1, width=5) \
            .grid(row=3, column=2, padx=5, pady=5, sticky="W")

        value_scorecard2_shot2 = tk.IntVar(frame_scores)
        entry_scorecard2_shot2 = ttk.Entry(frame_scores, textvariable=value_scorecard2_shot2, width=5) \
            .grid(row=3, column=3, padx=5, pady=5, sticky="W")

        value_scorecard2_shot3 = tk.IntVar(frame_scores)
        entry_scorecard2_shot3 = ttk.Entry(frame_scores, textvariable=value_scorecard2_shot3, width=5) \
            .grid(row=3, column=4, padx=5, pady=5, sticky="W")

        value_scorecard2_shot4 = tk.IntVar(frame_scores)
        entry_scorecard2_shot4 = ttk.Entry(frame_scores, textvariable=value_scorecard2_shot4, width=5) \
            .grid(row=3, column=5, padx=5, pady=5, sticky="W")

        value_scorecard2_shot5 = tk.IntVar(frame_scores)
        entry_scorecard2_shot5 = ttk.Entry(frame_scores, textvariable=value_scorecard2_shot5, width=5) \
            .grid(row=3, column=6, padx=5, pady=5, sticky="W")

        frame_buttons_left = tk.Frame(label_frame_left)
        frame_buttons_left.pack(anchor="w")

        button_submit_left = ttk.Button(frame_buttons_left, text="Invoeren", command=lambda: clicked_submit_left()) \
            .grid(row=0, column=0, padx=10, pady=15, sticky="W")

        def clicked_submit_left():
            total_card1 = int(value_scorecard1_shot1.get()
                              + value_scorecard1_shot2.get()
                              + value_scorecard1_shot3.get()
                              + value_scorecard1_shot4.get()
                              + value_scorecard1_shot5.get())

            total_card2 = int(value_scorecard2_shot1.get()
                              + value_scorecard2_shot2.get()
                              + value_scorecard2_shot3.get()
                              + value_scorecard2_shot4.get()
                              + value_scorecard2_shot5.get())

            result_submit_left = database.execute_sql('''INSERT OR IGNORE INTO score (
            card_one_shot_one,
            card_one_shot_two,
            card_one_shot_three,
            card_one_shot_four,
            card_one_shot_five,
            card_one_total,
            card_two_shot_one,
            card_two_shot_two,
            card_two_shot_three,
            card_two_shot_four,
            card_two_shot_five,
            card_two_total,
            date_score,
            shooter,
            firearm_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (
                value_scorecard1_shot1.get(),
                value_scorecard1_shot2.get(),
                value_scorecard1_shot3.get(),
                value_scorecard1_shot4.get(),
                value_scorecard1_shot5.get(),
                total_card1,
                value_scorecard2_shot1.get(),
                value_scorecard2_shot2.get(),
                value_scorecard2_shot3.get(),
                value_scorecard2_shot4.get(),
                value_scorecard2_shot5.get(),
                total_card2,
                str(date.today()),
                value_user_left.get()[2:8],
                value_firearm_left.get()[12:-2]))

            if result_submit_left == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met success de score voor "
                                            + value_user_left.get()[2:8] + " ingevoerd")
            else:
                messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")

        def clicked_reset():
            value_scorecard1_shot1.set(0)
            value_scorecard1_shot2.set(0)
            value_scorecard1_shot3.set(0)
            value_scorecard1_shot4.set(0)
            value_scorecard1_shot5.set(0)
            value_scorecard2_shot1.set(0)
            value_scorecard2_shot2.set(0)
            value_scorecard2_shot3.set(0)
            value_scorecard2_shot4.set(0)
            value_scorecard2_shot5.set(0)

        button_reset_left = ttk.Button(frame_buttons_left, text="Reset", command=lambda: clicked_reset()) \
            .grid(row=0, column=1, padx=10, pady=15, sticky="W")

        label_frame_right = tk.LabelFrame(frame_right, text="View Scores")
        label_frame_right.pack(side="right", fill="both", expand=True)


# TODO add email functionality to mail a receipt to the user also add totals for transactions
class FinancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame_left = tk.Frame(self)
        frame_left.pack(side="left")

        button_main_menu = ttk.Button(frame_left, text="Main Menu",
                                      command=lambda: controller.show_frame(MainMenu))
        button_main_menu.pack()

        button_finance_page = ttk.Button(frame_left, text="Score Page",
                                         command=lambda: controller.show_frame(ScorePage))
        button_finance_page.pack()

        frame_right = tk.Frame(self)
        frame_right.pack(side="right", fill="both", expand=True)

        frame_top = tk.Frame(frame_right)
        frame_top.pack(side="top", fill="both", expand=True)

        label_frame_top_left = tk.LabelFrame(frame_top, text="Ammunition Transaction")
        label_frame_top_left.pack(side="left", fill="both", expand=True)

        frame_ammunition_top = tk.Frame(label_frame_top_left)
        frame_ammunition_top.pack(side="top", anchor="nw")

        label_user_top_left = ttk.Label(frame_ammunition_top, text="Lid:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_top_left = tk.StringVar(frame_ammunition_top)
        value_user_top_left.set("Select")
        option_menu_user_top_left = ttk.OptionMenu(frame_ammunition_top, value_user_top_left, users[0], *users) \
            .grid(row=0, column=1, padx=5, pady=5, sticky="W")

        frame_ammunition_middle = tk.Frame(label_frame_top_left)
        frame_ammunition_middle.pack(anchor="nw")

        label_ammunition_type = ttk.Label(frame_ammunition_middle, text="Munitie type:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        ammunition_types = database.execute_sql('''SELECT type FROM ammunition;''')
        value_ammunition_type = tk.StringVar(frame_ammunition_middle)
        value_ammunition_type.set("Select")
        option_menu_ammunition_type = ttk.OptionMenu(frame_ammunition_middle,
                                                     value_ammunition_type,
                                                     ammunition_types[0],
                                                     *ammunition_types).grid(row=0, column=1, padx=5, pady=2,
                                                                             sticky="W")

        label_ammunition_quantity = ttk.Label(frame_ammunition_middle, text="Aantal:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="W")
        value_ammunition_quantity = tk.IntVar(frame_ammunition_middle)
        entry_ammunition_quantity = ttk.Entry(frame_ammunition_middle,
                                              textvariable=value_ammunition_quantity,
                                              width=5).grid(row=0, column=3, padx=5, pady=5, sticky="W")

        label_ammunition_valuation = ttk.Label(frame_ammunition_middle, text="Totaal (EUR):") \
            .grid(row=1, column=0, padx=5, pady=2, sticky="W")
        total_price_left = tk.DoubleVar()
        total_price_left.set(0.0)
        label_ammunition_total = ttk.Label(frame_ammunition_middle, textvariable=total_price_left) \
            .grid(row=1, column=1, padx=5, pady=2, sticky="W")

        frame_ammunition_bottom = tk.Frame(label_frame_top_left)
        frame_ammunition_bottom.pack(anchor="w")

        button_submit_left = ttk.Button(frame_ammunition_bottom,
                                        text="Verkopen",
                                        command=lambda: clicked_submit_left()) \
            .grid(row=0, column=0, padx=10, pady=15, sticky="W")

        def clicked_submit_left():
            ammunition_stock = database.execute_sql('''SELECT stock FROM ammunition WHERE type = ?''',
                                                    (value_ammunition_type.get()[2:-3],))

            new_ammunition_stock = ammunition_stock[0][0] - value_ammunition_quantity.get()

            if new_ammunition_stock < 0:
                messagebox.showinfo(title="Error",
                                    message="Er is niet genoeg voorraad om zo veel te verkopen er is slechts " +
                                            str(ammunition_stock[0][0]) + " over en u probeert " +
                                            str(value_ammunition_quantity.get()) + " te verkopen")
            else:
                ammunition_price = database.execute_sql('''SELECT price FROM ammunition WHERE type = ?''',
                                                        (value_ammunition_type.get()[2:-3],))

                total_ammunition_price = round(value_ammunition_quantity.get() * ammunition_price[0][0], 2)

                result_submit_left = database.execute_sql('''INSERT OR IGNORE INTO sale_ammunition (
                                            date_sold,
                                            quantity,
                                            type,
                                            seller,
                                            buyer,
                                            price) VALUES (?, ?, ?, ?, ?, ?)''', (
                    str(date.today()),
                    value_ammunition_quantity.get(),
                    value_ammunition_type.get()[2:-3],
                    '123456',
                    value_user_top_left.get()[2:8],
                    total_ammunition_price
                ))

                value_ammunition_quantity.set(0)
                total_price_left.set(0.0)

                if result_submit_left == 'success':
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes munitie verkocht er is nu " +
                                                str(new_ammunition_stock) + " voorraad van " +
                                                value_ammunition_type.get()[2:-3] + " over")
                else:
                    messagebox.showerror(title="Error",
                                         message="Er was een fout bij het verkopen van de munitie")

        button_reset_left = ttk.Button(frame_ammunition_bottom, text="Reset", command=lambda: clicked_reset_left()) \
            .grid(row=0, column=1, padx=10, pady=15, sticky="W")

        def clicked_reset_left():
            value_ammunition_quantity.set(0)
            total_price_left.set(0.0)

        button_ammunition_total = ttk.Button(frame_ammunition_bottom,
                                             text="Reken Totaal",
                                             command=lambda: clicked_total_left()) \
            .grid(row=0, column=2, padx=10, pady=15, sticky="W")

        def clicked_total_left():
            ammunition_price = database.execute_sql('''SELECT price FROM ammunition WHERE type = ?''',
                                                    (value_ammunition_type.get()[2:-3],))

            total_ammunition_price = round(value_ammunition_quantity.get() * ammunition_price[0][0], 2)

            total_price_left.set(total_ammunition_price)

        # scorecard sales starts here

        fields = {
            'Standaard': 'regular',
            'Competitie': 'competition'
        }

        label_frame_top_right = tk.LabelFrame(frame_top, text="Scorecard Transaction")
        label_frame_top_right.pack(side="right", fill="both", expand=True)

        frame_scorecard_top = tk.Frame(label_frame_top_right)
        frame_scorecard_top.pack(side="top", anchor="nw")

        label_user_top_right = ttk.Label(frame_scorecard_top, text="Lid:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_top_right = tk.StringVar(frame_scorecard_top)
        value_user_top_right.set("Select")
        option_menu_user_top_right = ttk.OptionMenu(frame_scorecard_top, value_user_top_right, users[0], *users) \
            .grid(row=0, column=1, padx=5, pady=5, sticky="W")

        frame_scorecard_middle = tk.Frame(label_frame_top_right)
        frame_scorecard_middle.pack(anchor="nw")

        label_scorecard_type = ttk.Label(frame_scorecard_middle, text="Scorecard type:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        scorecard_types = database.execute_sql('''SELECT type FROM scorecard;''')
        value_scorecard_type = tk.StringVar(frame_scorecard_middle)
        value_scorecard_type.set("Select")
        option_menu_scorecard_type = ttk.OptionMenu(frame_scorecard_middle,
                                                    value_scorecard_type,
                                                    next(iter(fields)),
                                                    *fields.keys()).grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_scorecard_quantity = ttk.Label(frame_scorecard_middle, text="Aantal:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="W")
        value_scorecard_quantity = tk.IntVar(frame_scorecard_middle)
        entry_scorecard_quantity = ttk.Entry(frame_scorecard_middle,
                                             textvariable=value_scorecard_quantity,
                                             width=5).grid(row=0, column=3, padx=5, pady=5, sticky="W")

        label_scorecard_valuation = ttk.Label(frame_scorecard_middle, text="Totaal (EUR):") \
            .grid(row=1, column=0, padx=5, pady=2, sticky="W")
        total_price_right = tk.DoubleVar()
        total_price_right.set(0.0)
        label_scorecard_total = ttk.Label(frame_scorecard_middle, textvariable=total_price_right) \
            .grid(row=1, column=1, padx=5, pady=2, sticky="W")

        frame_scorecard_bottom = tk.Frame(label_frame_top_right)
        frame_scorecard_bottom.pack(anchor="w")

        button_submit_right = ttk.Button(frame_scorecard_bottom,
                                         text="Verkopen",
                                         command=lambda: clicked_submit_right()) \
            .grid(row=0, column=0, padx=10, pady=15, sticky="W")

        def clicked_submit_right():
            scorecard_stock = database.execute_sql('''SELECT stock FROM scorecard WHERE type = ?''',
                                                   (fields.get(value_scorecard_type.get()),))

            new_scorecard_stock = scorecard_stock[0][0] - value_scorecard_quantity.get()

            if new_scorecard_stock < 0:
                messagebox.showinfo(title="Error",
                                    message="Er is niet genoeg voorraad om zo veel te verkopen er is slechts " +
                                            str(scorecard_stock[0][0]) + " over en u probeert " +
                                            str(value_scorecard_quantity.get()) + " te verkopen")
            else:
                scorecard_price = database.execute_sql('''SELECT price FROM scorecard WHERE type = ?''',
                                                       (fields.get(value_scorecard_type.get()),))

                total_scorecard_price = round(value_scorecard_quantity.get() * scorecard_price[0][0], 2)

                database.execute_sql('''UPDATE scorecard SET stock = ? WHERE type = ?''',
                                     (new_scorecard_stock, fields.get(value_scorecard_type.get()),))

                result_submit_right = database.execute_sql('''INSERT OR IGNORE INTO sale_scorecard (
                                                    date_sold,
                                                    quantity,
                                                    type,
                                                    seller,
                                                    buyer,
                                                    price) VALUES (?, ?, ?, ?, ?, ?)''', (
                    str(date.today()),
                    value_scorecard_quantity.get(),
                    fields.get(value_scorecard_type.get()),
                    '123456',
                    value_user_top_right.get()[2:8],
                    total_scorecard_price
                ))

                value_scorecard_quantity.set(0)
                total_price_right.set(0.0)

                if result_submit_right == 'success':
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes scorecard verkocht u heeft nu " +
                                                str(new_scorecard_stock) + " voorraad van " +
                                                fields.get(value_scorecard_type.get()) + " over")
                else:
                    messagebox.showerror(title="Error",
                                         message="Er was een fout bij het verkopen van de scorecard")

        button_reset_right = ttk.Button(frame_scorecard_bottom, text="Reset", command=lambda: clicked_reset_right()) \
            .grid(row=0, column=1, padx=10, pady=15, sticky="W")

        def clicked_reset_right():
            value_scorecard_quantity.set(0)
            total_price_right.set(0.0)

        button_scorecard_total = ttk.Button(frame_scorecard_bottom,
                                            text="Reken Totaal",
                                            command=lambda: clicked_total_right()) \
            .grid(row=0, column=2, padx=10, pady=15, sticky="W")

        def clicked_total_right():
            scorecard_price = database.execute_sql('''SELECT price FROM scorecard WHERE type = ?''',
                                                   (fields.get(value_scorecard_type.get()),))

            total_scorecard_price = round(value_scorecard_quantity.get() * scorecard_price[0][0], 2)

            total_price_right.set(total_scorecard_price)

        frame_bottom = tk.Frame(frame_right)
        frame_bottom.pack(side="bottom", fill="both", expand=True)

        label_frame_bottom = tk.LabelFrame(frame_bottom, text="View Transactions")
        label_frame_bottom.pack(side="bottom", fill="both", expand=True)


app = ShootingClub()
app.geometry("900x500")
app.minsize(900, 500)
app.mainloop()

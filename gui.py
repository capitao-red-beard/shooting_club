import tkinter as tk
from datetime import date
from tkinter import messagebox
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import database
import mail

matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pull_data = open("sample_data.txt", "r").read()
    data_list = pull_data.split('\n')

    x_list = []
    y_list = []

    for line in data_list:
        if len(line) > 1:
            x, y = line.split(',')
            x_list.append(int(x))
            y_list.append(int(y))

    a.clear()
    a.plot(x_list, y_list)


def is_int(char):
    if char.isdigit():
        return True
    elif char is '':
        return True
    else:
        return False


def popup_user_settings():
    popup = tk.Tk()
    popup.wm_title("Lid Instellingen")

    reg_int = popup.register(is_int)

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
    option_menu_user_type_new = ttk.OptionMenu(tab_new, value_user_type_new, next(iter(fields)), *fields.keys())
    option_menu_user_type_new.config(width=max([len(i) for i in fields.keys()]) + 1)
    option_menu_user_type_new.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_first_name_new = ttk.Label(tab_new, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_first_name_new = tk.StringVar(tab_new)
    entry_first_name_new = ttk.Entry(tab_new, textvariable=value_first_name_new, width=25)
    entry_first_name_new.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_last_name_new = ttk.Label(tab_new, text="Familienaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_last_name_new = tk.StringVar(tab_new)
    entry_last_name_new = ttk.Entry(tab_new, textvariable=value_last_name_new, width=25) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_date_of_birth_new = ttk.Label(tab_new, text="Geboorte Datum (YYYY-MM-DD):") \
        .grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth_new = tk.StringVar(tab_new)
    entry_date_of_birth_new = ttk.Entry(tab_new, textvariable=value_date_of_birth_new, width=25) \
        .grid(row=3, column=1, padx=5, pady=2, sticky="W")

    label_address_new = ttk.Label(tab_new, text="Adres:").grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_address_new = tk.StringVar(tab_new)
    entry_address_new = ttk.Entry(tab_new, textvariable=value_address_new, width=25) \
        .grid(row=4, column=1, padx=5, pady=2, sticky="W")

    label_city_new = ttk.Label(tab_new, text="Woonplaats:").grid(row=5, column=0, padx=5, pady=5, sticky="W")
    value_city_new = tk.StringVar(tab_new)
    entry_city_new = ttk.Entry(tab_new, textvariable=value_city_new, width=25) \
        .grid(row=5, column=1, padx=5, pady=2, sticky="W")

    label_post_code_new = ttk.Label(tab_new, text="Postcode:").grid(row=6, column=0, padx=5, pady=2, sticky="W")
    value_post_code_new = tk.StringVar(tab_new)
    entry_post_code_new = ttk.Entry(tab_new, textvariable=value_post_code_new, width=25) \
        .grid(row=6, column=1, padx=5, pady=2, sticky="W")

    label_telephone_number_new = ttk.Label(tab_new, text="Telefoonnummer:") \
        .grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number_new = tk.StringVar(tab_new)
    entry_telephone_number_new = ttk.Entry(tab_new, textvariable=value_telephone_number_new, width=25)
    entry_telephone_number_new.config(validate="key", validatecommand=(reg_int, '%P'))
    entry_telephone_number_new.grid(row=7, column=1, padx=5, pady=2, sticky="W")

    label_email_address_new = ttk.Label(tab_new, text="Email Adres:").grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_email_address_new = tk.StringVar(tab_new)
    entry_email_address_new = ttk.Entry(tab_new, textvariable=value_email_address_new, width=25) \
        .grid(row=8, column=1, padx=5, pady=2, sticky="W")

    label_password_new = ttk.Label(tab_new, text="Wachtwoord:").grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_password_new = tk.StringVar(tab_new)
    entry_password_new = ttk.Entry(tab_new, show="*", textvariable=value_password_new, width=25) \
        .grid(row=9, column=1, padx=5, pady=2, sticky="W")

    label_knsa_licence_number_new = ttk.Label(tab_new, text="KNSA Licentienummer:") \
        .grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number_new = tk.StringVar(tab_new)
    entry_knsa_licence_number_new = ttk.Entry(tab_new, textvariable=value_knsa_licence_number_new, width=25)
    entry_knsa_licence_number_new.config(validate="key", validatecommand=(reg_int, '%P'))
    entry_knsa_licence_number_new.grid(row=10, column=1, padx=5, pady=2, sticky="W")

    label_date_of_membership_new = ttk.Label(tab_new, text="Datum van Lidmaatschap Ingang (YYYY-MM-DD):") \
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership_new = tk.StringVar(tab_new)
    entry_date_of_membership_new = ttk.Entry(tab_new, textvariable=value_date_of_membership_new, width=25) \
        .grid(row=11, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=12, column=0, padx=10, pady=15)

    def clicked_new():
        data_list_new = [value_first_name_new.get(),
                         value_last_name_new.get(),
                         value_date_of_birth_new.get(),
                         value_address_new.get(),
                         value_city_new.get(),
                         value_post_code_new.get(),
                         value_telephone_number_new.get(),
                         value_email_address_new.get(),
                         value_password_new.get(),
                         value_knsa_licence_number_new.get(),
                         value_date_of_membership_new.get()]

        if data_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
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
                email_body = 'Gefeliciteerd ' + value_first_name_new.get() + \
                             ', \n\n Uw gegevens zijn nu opgeslaan in het schietvereniging systeem. ' \
                             '\n\n U kunt nu scores opslaan, terug kijken, munitie en kaarten copen en veel meer!' \
                             '\n\n Reageer aub niet op deze email.' \
                             '\n\n Fijne dag!'

                email_result = mail.send_email(value_email_address_new.get(),
                                               'Welkom bij Schietvereniging Prinses Juliana',
                                               email_body)

                if email_result:
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes een niewe lid aangemaakt")
                    popup.destroy()
                else:
                    messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")
                    popup.lift()

            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=12, column=1, padx=10, pady=15)

    tab_edit = ttk.Frame(notebook)
    notebook.add(tab_edit, text="Bewerk Lid")

    label_users_edit = ttk.Label(tab_edit, text="Lid te Berwerken:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
    value_user_edit = tk.StringVar(tab_edit)
    value_user_edit.set("Select")
    option_menu_user_edit = ttk.OptionMenu(tab_edit, value_user_edit, users[0], *users)
    option_menu_user_edit.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
    option_menu_user_edit.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    fields2 = {'Adres': 'address',
               'Woonplaats': 'city',
               'Postcode': 'post_code',
               'Telefoonnummer': 'telephone_number',
               'Email Adres': 'email_address',
               'KNSA Licentienummer': 'knsa_licence_number'}

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_user_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields2)), *fields2.keys())
    option_menu_user_edit.config(width=max([len(i) for i in fields2.keys()]) + 1)
    option_menu_user_edit.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.StringVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=25) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        data_list_edit = [value_update_edit.get()]

        if data_list_edit.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
            result_edit = database.execute_sql('UPDATE user SET ' + str(fields2.get(value_field_edit.get()))
                                               + ' = ? WHERE  knsa_licence_number = ?',
                                               (value_update_edit.get().lower(), value_user_edit.get()[2:8]))

            if result_edit == 'success':
                user_data = database.execute_sql('''SELECT email_address, first_name 
                        FROM user WHERE knsa_licence_number = ?''', (value_user_edit.get()[2:8],))

                email_body = 'Hallo ' + user_data[0][1] + \
                             ', \n\n Uw ' + value_field_edit.get() + \
                             ' is met succes veranderd in het systeem.' \
                             ' \n\n Reageer aub niet op deze email. \n\n Fijne dag!'

                email_result = mail.send_email(user_data[0][0], 'Uw gegevens zijn veranderd', email_body)

                if email_result:
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes een lid aangepast")
                    popup.destroy()
                else:
                    messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")
                    popup.lift()

            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder Lid")

    label_user_delete = ttk.Label(tab_delete, text="Lid te Verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_user_delete = tk.StringVar(tab_delete)
    value_user_delete.set("Select")
    option_menu_user_delete = ttk.OptionMenu(tab_delete, value_user_delete, users[0], *users)
    option_menu_user_delete.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
    option_menu_user_delete.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning', 'Weet jij zeker dat jij deze lid wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database.execute_sql(
                '''DELETE FROM user WHERE knsa_licence_number = ?;''', (value_user_delete.get()[2:8],))

            if result_delete == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes de lid verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error",
                                     message="Er was een fout bij het verwijderen van deze lid")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


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
    option_menu_user_new = ttk.OptionMenu(tab_new, value_users_new, users[0], *users)
    option_menu_user_new.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
    option_menu_user_new.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_new():
        firearm_list_new = [value_type_new.get()]

        if firearm_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
            result_new = database.execute_sql('''INSERT OR IGNORE INTO firearm (
                    type, owner) VALUES (?, ?)''', (value_type_new.get().lower(), value_users_new.get()[2:8]))

            if result_new == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een niewe vuurwapen aangemaakt")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

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
    option_menu_existing_edit = ttk.OptionMenu(tab_edit, value_existing_edit, firearms[0], *firearms)
    option_menu_existing_edit.config(width=max([sum([len(q) for q in i]) for i in firearms]) + 3)
    option_menu_existing_edit.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_users_edit = ttk.Label(tab_edit, text="Nieuwe Eigenaar:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_users_edit = tk.StringVar(tab_edit)
    value_users_edit.set("Select")
    option_menu_users_edit = ttk.OptionMenu(tab_edit, value_users_edit, users[0], *users)
    option_menu_users_edit.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
    option_menu_users_edit.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Bewerken", command=lambda: clicked_edit()) \
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_edit():
        result_edit = database.execute_sql('''UPDATE firearm SET owner = ? WHERE owner = ?''',
                                           (value_users_edit.get()[2:8], value_existing_edit.get()[2:8]))

        if result_edit == 'success':
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een vuurwapen aangepast")
            popup.destroy()
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
            popup.lift()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=2, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder Vuurwapen")

    label_type_delete = ttk.Label(tab_delete, text="Vuurwapen te Verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, firearms[0], *firearms)
    option_menu_type_delete.config(width=max([sum([len(q) for q in i]) for i in firearms]) + 3)
    option_menu_type_delete.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15, sticky="W")

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze vuurwapen wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database.execute_sql(
                '''DELETE FROM firearm WHERE type = ? AND owner = ?''',
                (value_type_delete.get()[12:-2], value_type_delete.get()[2:8]))

            if result_delete == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een vuurwapen verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_ammunition_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Munitie Instellingen")

    reg_int = popup.register(is_int)

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
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=10) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.IntVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=10)
    entry_stock_new.config(validate="key", validatecommand=(reg_int, '%P'))
    entry_stock_new.grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        ammunition_list_new = [value_type_new.get()]

        if ammunition_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
        else:
            result_new = database.execute_sql('''INSERT OR IGNORE INTO ammunition (
                    type, price, stock) VALUES (?, ?, ?)''',
                                              (value_type_new.get().lower(), value_price_new.get(),
                                               value_stock_new.get()))

            if result_new == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een niewe munitie type aangemaakt")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

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
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, ammunition_types[0], *ammunition_types)
    option_menu_type_edit.config(width=max([sum([len(q) for q in i]) for i in ammunition_types]) + 1)
    option_menu_type_edit.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_value_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields)), *fields.keys())
    option_menu_value_edit.config(width=max([len(i) for i in fields.keys()]) + 1)
    option_menu_value_edit.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=10) \
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
                                message="Het systeem heeft met succes een munitie type aangepast")
            popup.destroy()
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
            popup.lift()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Munitie te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, ammunition_types[0], *ammunition_types)
    option_menu_type_delete.config(width=max([sum([len(q) for q in i]) for i in ammunition_types]) + 1)
    option_menu_type_delete.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze munitie wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database.execute_sql('''DELETE FROM ammunition WHERE type = ?''',
                                                 (value_type_delete.get()[2:-3]), )

            if result_delete == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een lid verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_scorecard_settings():
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Score Kaart Instellingen")

    reg_int = popup.register(is_int)

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
    entry_price_new = ttk.Entry(tab_new, textvariable=value_price_new, width=10) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_new = ttk.Label(tab_new, text="Voorraad:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_new = tk.IntVar(tab_new)
    entry_stock_new = ttk.Entry(tab_new, textvariable=value_stock_new, width=10)
    entry_stock_new.config(validate="key", validatecommand=(reg_int, '%P'))
    entry_stock_new.grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        scorecard_list_new = [value_type_new.get()]

        if scorecard_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
            result_new = database.execute_sql('''INSERT OR IGNORE INTO scorecard (
                            type, price, stock) VALUES (?, ?, ?)''',
                                              (value_type_new.get().lower(), value_price_new.get(),
                                               value_stock_new.get()))

            if result_new == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een niewe scorecard aangemaakt")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

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
    option_menu_type_edit = ttk.OptionMenu(tab_edit, value_type_edit, next(iter(fields2)), *fields2.keys())
    option_menu_type_edit.config(width=max([len(i) for i in fields2.keys()]) + 1)
    option_menu_type_edit.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    option_menu_value_edit = ttk.OptionMenu(tab_edit, value_field_edit, next(iter(fields)), *fields.keys())
    option_menu_value_edit.config(width=max([len(i) for i in fields.keys()]) + 1)
    option_menu_value_edit.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=10) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        if fields.get(value_field_edit.get()) == 'stock':
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
                                message="Het systeem heeft met succes een scorecard aangepast")
            popup.destroy()
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
            popup.lift()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Score kaart te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    option_menu_type_delete = ttk.OptionMenu(tab_delete, value_type_delete, next(iter(fields2)), *fields2.keys())
    option_menu_type_delete.config(width=max([len(i) for i in fields2.keys()]) + 1)
    option_menu_type_delete.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze scorecard wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database.execute_sql('''DELETE FROM scorecard WHERE type = ?''',
                                                 (fields.get(value_type_delete.get()),))

            if result_delete == 'success':
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes de scorecard verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
                popup.lift()
        else:
            popup.lift()

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
        file_menu.add_command(label="Sluiten", command=lambda: self.on_exit(), accelerator="Ctrl+Q")
        menu_bar.add_cascade(label="Instellingen", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (MainMenu, ScorePage, FinancePage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.resizable(0, 0)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def on_exit(self):
        if messagebox.askquestion('Warning',
                                  'Weet jij zeker dat jij de applicatie wilt sluiten?', icon="warning") == 'yes':
            self.quit()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Score Page", command=lambda: controller.show_frame(ScorePage))
        button1.pack()

        button2 = ttk.Button(self, text="Finance Page", command=lambda: controller.show_frame(FinancePage))
        button2.pack()


# TODO add matplotlib functionality
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

        label_frame_top = tk.LabelFrame(frame_right, text="Submit Score")
        label_frame_top.pack(side="top", fill="x", expand=True)

        frame_top = tk.Frame(label_frame_top)
        frame_top.pack(side="top", anchor="w")

        frame_details = tk.Frame(frame_top)
        frame_details.pack(side="left", anchor="nw")

        label_user_left = ttk.Label(frame_details, text="Lid:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_left = tk.StringVar(frame_details)
        value_user_left.set("Select")
        option_menu_user_left = ttk.OptionMenu(frame_details, value_user_left, users[0], *users)
        option_menu_user_left.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
        option_menu_user_left.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        label_firearm_left = ttk.Label(frame_details, text="Vuurwapen:") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="W")

        firearms = database.execute_sql('''SELECT owner, type FROM firearm;''')
        value_firearm_left = tk.StringVar(frame_details)
        value_firearm_left.set("Select")
        option_menu_firearm_left = ttk.OptionMenu(frame_details, value_firearm_left, firearms[0], *firearms)
        option_menu_firearm_left.config(width=max([sum([len(q) for q in i]) for i in firearms]) + 3)
        option_menu_firearm_left.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        frame_scores = tk.Frame(frame_top)
        frame_scores.pack(side="right", anchor="nw")

        list_score = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        label_scorecard1 = ttk.Label(frame_scores, text="1e Scorecard:") \
            .grid(row=2, column=0, padx=5, pady=5, sticky="W")

        value_scorecard1_shot1 = tk.IntVar(frame_scores)
        value_scorecard1_shot1.set(0)
        option_menu_scorecard1_shot1 = ttk.OptionMenu(frame_scores, value_scorecard1_shot1, list_score[0], *list_score)
        option_menu_scorecard1_shot1.config(width=2)
        option_menu_scorecard1_shot1.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        value_scorecard1_shot2 = tk.IntVar(frame_scores)
        value_scorecard1_shot2.set(0)
        option_menu_scorecard1_shot2 = ttk.OptionMenu(frame_scores, value_scorecard1_shot2, list_score[0], *list_score)
        option_menu_scorecard1_shot2.config(width=2)
        option_menu_scorecard1_shot2.grid(row=2, column=2, padx=5, pady=5, sticky="W")

        value_scorecard1_shot3 = tk.IntVar(frame_scores)
        value_scorecard1_shot3.set(0)
        option_menu_scorecard1_shot3 = ttk.OptionMenu(frame_scores, value_scorecard1_shot3, list_score[0], *list_score)
        option_menu_scorecard1_shot3.config(width=2)
        option_menu_scorecard1_shot3.grid(row=2, column=3, padx=5, pady=5, sticky="W")

        value_scorecard1_shot4 = tk.IntVar(frame_scores)
        value_scorecard1_shot4.set(0)
        option_menu_scorecard1_shot4 = ttk.OptionMenu(frame_scores, value_scorecard1_shot4, list_score[0], *list_score)
        option_menu_scorecard1_shot4.config(width=2)
        option_menu_scorecard1_shot4.grid(row=2, column=4, padx=5, pady=5, sticky="W")

        value_scorecard1_shot5 = tk.IntVar(frame_scores)
        value_scorecard1_shot5.set(0)
        option_menu_scorecard1_shot5 = ttk.OptionMenu(frame_scores, value_scorecard1_shot5, list_score[0], *list_score)
        option_menu_scorecard1_shot5.config(width=2)
        option_menu_scorecard1_shot5.grid(row=2, column=5, padx=5, pady=5, sticky="W")

        label_scorecard1_valuation = ttk.Label(frame_scores, text="Totaal Scorecard 1:") \
            .grid(row=2, column=6, padx=5, pady=5, sticky="W")
        total_scorecard1 = tk.IntVar()
        total_scorecard1.set(0)
        label_ammunition_total = ttk.Label(frame_scores, textvariable=total_scorecard1) \
            .grid(row=2, column=7, padx=5, pady=5, sticky="W")

        label_scorecard_2 = ttk.Label(frame_scores, text="2e Scorecard:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="W")

        value_scorecard2_shot1 = tk.IntVar(frame_scores)
        value_scorecard2_shot1.set(0)
        option_menu_scorecard2_shot1 = ttk.OptionMenu(frame_scores, value_scorecard2_shot1, list_score[0], *list_score)
        option_menu_scorecard2_shot1.config(width=2)
        option_menu_scorecard2_shot1.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        value_scorecard2_shot2 = tk.IntVar(frame_scores)
        value_scorecard2_shot2.set(0)
        option_menu_scorecard2_shot2 = ttk.OptionMenu(frame_scores, value_scorecard2_shot2, list_score[0], *list_score)
        option_menu_scorecard2_shot2.config(width=2)
        option_menu_scorecard2_shot2.grid(row=3, column=2, padx=5, pady=5, sticky="W")

        value_scorecard2_shot3 = tk.IntVar(frame_scores)
        value_scorecard2_shot3.set(0)
        option_menu_scorecard2_shot3 = ttk.OptionMenu(frame_scores, value_scorecard2_shot3, list_score[0], *list_score)
        option_menu_scorecard2_shot3.config(width=2)
        option_menu_scorecard2_shot3.grid(row=3, column=3, padx=5, pady=5, sticky="W")

        value_scorecard2_shot4 = tk.IntVar(frame_scores)
        value_scorecard2_shot4.set(0)
        option_menu_scorecard2_shot4 = ttk.OptionMenu(frame_scores, value_scorecard2_shot4, list_score[0], *list_score)
        option_menu_scorecard2_shot4.config(width=2)
        option_menu_scorecard2_shot4.grid(row=3, column=4, padx=5, pady=5, sticky="W")

        value_scorecard2_shot5 = tk.IntVar(frame_scores)
        value_scorecard2_shot5.set(0)
        option_menu_scorecard2_shot5 = ttk.OptionMenu(frame_scores, value_scorecard2_shot5, list_score[0], *list_score)
        option_menu_scorecard2_shot5.config(width=2)
        option_menu_scorecard2_shot5.grid(row=3, column=5, padx=5, pady=5, sticky="W")

        label_scorecard2_valuation = ttk.Label(frame_scores, text="Totaal Scorecard 2:") \
            .grid(row=3, column=6, padx=5, pady=5, sticky="W")
        total_scorecard2 = tk.IntVar()
        total_scorecard2.set(0)
        label_ammunition_total = ttk.Label(frame_scores, textvariable=total_scorecard2) \
            .grid(row=3, column=7, padx=5, pady=5, sticky="W")

        frame_bottom = tk.Frame(label_frame_top)
        frame_bottom.pack(anchor="nw")

        button_submit = ttk.Button(frame_bottom, text="Invoeren", command=lambda: clicked_submit_left()) \
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

                sc1 = [value_scorecard1_shot1.get(),
                       value_scorecard1_shot2.get(),
                       value_scorecard1_shot3.get(),
                       value_scorecard1_shot4.get(),
                       value_scorecard1_shot5.get(),
                       total_card1]

                sc2 = [value_scorecard2_shot1.get(),
                       value_scorecard2_shot2.get(),
                       value_scorecard2_shot3.get(),
                       value_scorecard2_shot4.get(),
                       value_scorecard2_shot5.get(),
                       total_card2]

                user_data = database.execute_sql('''SELECT email_address, first_name 
                                                 FROM user WHERE knsa_licence_number = ?''',
                                                 (value_user_left.get()[2:8],))

                email_body = 'Hallo ' + user_data[0][1] + \
                             ', \n\n u scores zijn voor ' + \
                             str(date.today()) + \
                             ' in de database ingevoerd. U heeft met ' + value_firearm_left.get()[12:-2] + \
                             ' geschoten. \n U heeft voor uw eerste kaart: \n schot 1: ' + str(sc1[0]) + \
                             '\n schot 2: ' + str(sc1[1]) + \
                             '\n schot 3: ' + str(sc1[2]) + \
                             '\n schot 4: ' + str(sc1[3]) + \
                             '\n schot 5: ' + str(sc1[4]) + \
                             '\n met een totaal score van: ' + str(sc1[5]) + \
                             '\n\n en voor uw tweede kaart: \n schot 1: ' + str(sc2[0]) + \
                             '\n schot 2: ' + str(sc2[1]) + \
                             '\n schot 3: ' + str(sc2[2]) + \
                             '\n schot 4: ' + str(sc2[3]) + \
                             '\n schot 5: ' + str(sc2[4]) + \
                             '\n met een totaal score van: ' + str(sc2[5]) + \
                             '\n\n reageer aub niet op deze email. \n\n Fijne dag!'

                email_result = mail.send_email(user_data[0][0], 'U heeft nieuwe scores ingediend', email_body)

                if email_result:
                    clicked_reset()
                else:
                    messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")

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
            total_scorecard1.set(0)
            total_scorecard2.set(0)

        button_reset = ttk.Button(frame_bottom, text="Reset", command=lambda: clicked_reset()) \
            .grid(row=0, column=1, padx=10, pady=15, sticky="W")

        def clicked_total():
            total_scorecard1.set(value_scorecard1_shot1.get() +
                                 value_scorecard1_shot2.get() +
                                 value_scorecard1_shot3.get() +
                                 value_scorecard1_shot4.get() +
                                 value_scorecard1_shot5.get())

            total_scorecard2.set(value_scorecard2_shot1.get() +
                                 value_scorecard2_shot2.get() +
                                 value_scorecard2_shot3.get() +
                                 value_scorecard2_shot4.get() +
                                 value_scorecard2_shot5.get())

        button_total = ttk.Button(frame_bottom, text="Reken Totaal", command=lambda: clicked_total()) \
            .grid(row=0, column=2, padx=10, pady=15, sticky="W")

        label_frame_bottom = tk.LabelFrame(frame_right, text="View Scores")
        label_frame_bottom.pack(side="right", fill="both", expand=True)

        frame_menu = tk.Frame(label_frame_bottom)
        frame_menu.pack(side="top", fill="x")

        label_user_matplot = ttk.Label(frame_menu, text="Lid:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_user_matplot = tk.StringVar(frame_menu)
        value_user_matplot.set("Select")
        option_menu_user_matplot = ttk.OptionMenu(frame_menu, value_user_matplot, users[0], *users)
        option_menu_user_matplot.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
        option_menu_user_matplot.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        # matplotlib graph starts here
        frame_matplot = tk.Frame(label_frame_bottom)
        frame_matplot.pack(side="bottom", fill="both")

        canvas = FigureCanvasTkAgg(f, frame_matplot)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, frame_matplot)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# TODO add matplotlib functionality
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
        label_frame_top_left.pack(side="left", fill="x", expand=True)

        frame_ammunition_top = tk.Frame(label_frame_top_left)
        frame_ammunition_top.pack(side="top", anchor="nw")

        label_user_top_left = ttk.Label(frame_ammunition_top, text="Lid:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_top_left = tk.StringVar(frame_ammunition_top)
        value_user_top_left.set("Select")
        option_menu_user_top_left = ttk.OptionMenu(frame_ammunition_top, value_user_top_left, users[0], *users)
        option_menu_user_top_left.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
        option_menu_user_top_left.grid(row=0, column=1, padx=5, pady=5, sticky="W")

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
                                                     *ammunition_types)
        option_menu_ammunition_type.config(width=max([sum([len(q) for q in i]) for i in ammunition_types]) + 1)
        option_menu_ammunition_type.grid(row=0, column=1, padx=5, pady=2, sticky="W")

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

                if result_submit_left == 'success':
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes munitie verkocht er is nu " +
                                                str(new_ammunition_stock) + " voorraad van " +
                                                value_ammunition_type.get()[2:-3] + " over")

                    user_data = database.execute_sql('''SELECT email_address, first_name 
                                                     FROM user WHERE knsa_licence_number = ?''',
                                                     (value_user_top_left.get()[2:8],))

                    email_body = 'Hallo ' + user_data[0][1] + \
                                 ', \n\n U heeft een transactie afgerond bij de scheitvereniging op ' \
                                 + str(date.today()) + \
                                 '. \n\n U heeft ' + str(value_ammunition_quantity.get()) + ' van ' + \
                                 value_ammunition_type.get()[2:-3] + \
                                 ' gekocht voor een prijs van totaal €' + str(total_price_left.get()) + \
                                 '\n\n reageer aub niet op deze email. \n\n Fijne dag!'

                    email_result = mail.send_email(user_data[0][0],
                                                   'U heeft iets gekocht op de schietvereniging',
                                                   email_body)

                    if email_result:
                        clicked_reset_left()
                    else:
                        messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")

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
        label_frame_top_right.pack(side="right", fill="x", expand=True)

        frame_scorecard_top = tk.Frame(label_frame_top_right)
        frame_scorecard_top.pack(side="top", anchor="nw")

        label_user_top_right = ttk.Label(frame_scorecard_top, text="Lid:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        users = database.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')
        value_user_top_right = tk.StringVar(frame_scorecard_top)
        value_user_top_right.set("Select")
        option_menu_user_top_right = ttk.OptionMenu(frame_scorecard_top, value_user_top_right, users[0], *users)
        option_menu_user_top_right.config(width=max([sum([len(q) for q in i]) for i in users]) + 1)
        option_menu_user_top_right.grid(row=0, column=1, padx=5, pady=5, sticky="W")

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
                                                    *fields.keys())
        option_menu_scorecard_type.config(width=max([len(i) for i in fields.keys()]) + 1)
        option_menu_scorecard_type.grid(row=0, column=1, padx=5, pady=2, sticky="W")

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

                if result_submit_right == 'success':
                    messagebox.showinfo(title="Information",
                                        message="Het systeem heeft met succes scorecard verkocht u heeft nu " +
                                                str(new_scorecard_stock) + " voorraad van " +
                                                value_scorecard_type.get() + " over")

                    user_data = database.execute_sql('''SELECT email_address, first_name 
                                                     FROM user WHERE knsa_licence_number = ?''',
                                                     (value_user_top_right.get()[2:8],))

                    email_body = 'Hallo ' + user_data[0][1] + \
                                 ', \n\n U heeft een transactie afgerond bij de scheitvereniging op ' \
                                 + str(date.today()) + \
                                 '. \n\n U heeft ' + str(value_scorecard_quantity.get()) + ' van ' + \
                                 value_scorecard_type.get() + \
                                 ' gekocht voor een prijs van totaal €' + str(total_price_right.get()) + \
                                 '\n\n reageer aub niet op deze email. \n\n Fijne dag!'

                    email_result = mail.send_email(user_data[0][0],
                                                   'U heeft iets gekocht op de schietvereniging',
                                                   email_body)

                    if email_result:
                        clicked_reset_right()
                    else:
                        messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")

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
        label_frame_bottom.pack(side="bottom", fill="x", expand=True)

        # matplotlib graph starts here
        canvas = FigureCanvasTkAgg(f, label_frame_bottom)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, label_frame_bottom)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


app = ShootingClub()
app.geometry("820x730")
app.minsize(860, 730)
app.maxsize(860, 730)
ani = animation.FuncAnimation(f, animate, interval=8000)
app.mainloop()

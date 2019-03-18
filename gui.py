import tkinter as tk
from datetime import date
from tkinter import messagebox
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import database_manager
import email_manager
import input_validation
import password_manager

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

matplotlib.use("TkAgg")
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


def get_user_data():
    return [str(u[2]) + ' ' + str(u[1]) + ' - ' + str(u[0]) for u in
            database_manager.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')]


def get_firearm_type():
    return [str(y[0]) for y in database_manager.execute_sql('''SELECT type FROM firearm;''')]


def get_ammunition_type():
    return [str(p[0]) for p in database_manager.execute_sql('''SELECT type FROM ammunition;''')]


def get_scorecard_type():
    return [str(s[0]) for s in database_manager.execute_sql('''SELECT type FROM scorecard;''')]


def get_discipline_type():
    return [str(d[0]) for d in database_manager.execute_sql('''SELECT type FROM discipline;''')]


def refresh(v, l):
    v.set_completion_list(l)


def popup_user_settings(user_session):
    popup = tk.Tk()
    popup.wm_title("Lid Instellingen: " + "(" + user_session + ") ")

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
    a_c_new_user = AutocompleteCombobox(tab_new, textvariable=value_user_type_new)
    a_c_new_user.set_completion_list(fields.keys())
    a_c_new_user.config(width=max([len(i) for i in fields.keys()]) + 1)
    a_c_new_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_first_name_new = ttk.Label(tab_new, text="Voornaam:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_first_name_new = tk.StringVar(tab_new)
    entry_first_name_new = ttk.Entry(tab_new, textvariable=value_first_name_new, width=25)
    entry_first_name_new.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_last_name_new = ttk.Label(tab_new, text="Familienaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_last_name_new = tk.StringVar(tab_new)
    entry_last_name_new = ttk.Entry(tab_new, textvariable=value_last_name_new, width=25) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_date_of_birth_new = ttk.Label(tab_new, text="Geboorte Datum (DD-MM-YYYY):") \
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
    entry_knsa_licence_number_new.grid(row=10, column=1, padx=5, pady=2, sticky="W")

    label_date_of_membership_new = ttk.Label(tab_new, text="Datum van Lidmaatschap Ingang (DD-MM-YYYY):") \
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership_new = tk.StringVar(tab_new)
    entry_date_of_membership_new = ttk.Entry(tab_new, textvariable=value_date_of_membership_new, width=25) \
        .grid(row=11, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=12, column=0, padx=10, pady=15)

    def clicked_new():
        data = [fields.get(value_user_type_new.get()),
                value_first_name_new.get().lower().strip(),
                value_last_name_new.get().lower().strip(),
                value_date_of_birth_new.get().strip(),
                value_address_new.get().lower().strip(),
                value_city_new.get().lower().strip(),
                value_post_code_new.get().replace(' ', '').lower(),
                value_telephone_number_new.get(),
                value_email_address_new.get().lower().strip(),
                value_password_new.get().strip(),
                value_knsa_licence_number_new.get().lower().strip(),
                value_date_of_membership_new.get().strip()]

        error_message = []

        if data[1] == '':
            error_message.append('Vul aub een voornaam in voordat je verder gaat\n')
        elif data[2] == '':
            error_message.append('Vul aub een familienaam in voordat je verder gaat\n')
        elif input_validation.is_date(str(input_validation.convert_input_date(data[3]))) is False:
            error_message.append('Vul aub een valide gebortedatum in voordat je verder gaat\n')
        elif input_validation.is_address(data[4], data[5], data[6]) is None:
            error_message.append('Vul aub een valide adres in in voordat je verder gaat\n')
        elif input_validation.is_phone_number(data[7]) is False:
            error_message.append('Vul aub een valide telefoonnummer in voor dat je verder gaat\n')
        elif input_validation.is_knsa(data[10]) is False:
            error_message.append('Vul aub een valide KNSA licentienummer in voordat je verder gaat\n')
        elif input_validation.is_date(str(input_validation.convert_input_date(data[11]))) is False:
            error_message.append('Vul aub een valide datum van litmaatschap ingang in voordat je verder gaat\n')

        if data[0] == 2:
            if input_validation.is_email(data[8]) is False:
                error_message.append('Vul aub een valide email adres in voor dat je verder gaat\n')
            elif input_validation.is_password(data[9]) is False:
                error_message.append('Vul aub een valide wachtwoord in voor dat je verder gaat\n')
            else:
                hashed_password = password_manager.hash_password(data[9])
        elif data[0] == 1:
            if len(data[8]) > 0:
                if input_validation.is_email(data[8]) is False:
                    error_message.append('Vul aub een valide email adres in voor dat je verder gaat\n')
            else:
                data[8] = None

            hashed_password = None

        if error_message:
            for m in error_message:
                messagebox.showerror(title="Error", message=m)
            popup.lift()
        else:
            result_new = database_manager.execute_sql(
                '''INSERT INTO user (type, first_name,last_name, date_of_birth, address, city, post_code, 
                telephone_number, email_address, password, knsa_licence_number, date_of_membership) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (
                    data[0],
                    data[1],
                    data[2],
                    input_validation.convert_input_date(data[3]),
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    hashed_password,
                    data[10],
                    input_validation.convert_input_date(data[11])))

            if result_new:
                email_result_user = True

                if data[8] is not None:
                    email_body_user = 'Gefeliciteerd ' + value_first_name_new.get() + \
                                      ', \n\n Uw gegevens zijn nu opgeslaan in het schietvereniging systeem. ' \
                                      '\n\n U kunt nu scores opslaan, terug kijken, ' \
                                      'munitie en kaarten copen en veel meer! ' \
                                      '\n\n Reageer aub niet op deze email. \n\n Fijne dag!'

                    email_result_user = email_manager.send_email(value_email_address_new.get(),
                                                                 'Welkom bij Schietvereniging Prinses Juliana',
                                                                 email_body_user)

                email_body_admin = 'Beheerder, \n\n Er is een nieuwe lid in het schietvereniging systeem, ' \
                                   'het lid was ingevoerd door ' + user_session + \
                                   '\n\n Reageer aub niet op deze email. \n\n Fijne dag!'

                admins = database_manager.execute_sql('''SELECT email_address FROM user WHERE type = ?''', (2,))

                recipients = []
                for x in admins:
                    recipients.append(x[0])

                email_result_admin = email_manager.send_email(recipients,
                                                              'Nieuwe Lid bij Schietvereniging Prinses Juliana',
                                                              email_body_admin)

                if email_result_user and email_result_admin:
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

    value_user_edit = tk.StringVar(tab_edit)
    value_user_edit.set("Select")
    a_c_edit_user = AutocompleteCombobox(tab_edit, textvariable=value_user_edit)
    a_c_edit_user.set_completion_list(get_user_data())
    a_c_edit_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
    a_c_edit_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

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
    a_c_edit_user_field = AutocompleteCombobox(tab_edit, textvariable=value_field_edit)
    a_c_edit_user_field.set_completion_list(fields2.keys())
    a_c_edit_user_field.config(width=max([len(i) for i in fields2.keys()]) + 2)
    a_c_edit_user_field.grid(row=1, column=1, padx=5, pady=2, sticky="W")

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
        elif fields2.get(value_field_edit.get()) == fields2.get('telefoonnummer'):
            if input_validation.is_int(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide telefoonnummer in")
                popup.lift()
        elif fields2.get(value_field_edit.get()) == fields2.get('email_address'):
            if input_validation.is_email(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide email adres in")
                popup.lift()
        elif fields2.get(value_field_edit.get()) == fields2.get('knsa_licence_number'):
            if input_validation.is_email(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide KNSA licentie nummer in")
                popup.lift()
        else:
            result_edit = database_manager.execute_sql(
                'UPDATE user SET ' + str(fields2.get(value_field_edit.get())) + ' = ? WHERE  knsa_licence_number = ?',
                (value_update_edit.get().lower(), int(value_user_edit.get()[-6:])))

            if result_edit:
                user_data = database_manager.execute_sql(
                    '''SELECT email_address, first_name FROM user WHERE knsa_licence_number = ?''',
                    (int(value_user_edit.get()[-6:]),))

                email_body = 'Hallo ' + user_data[0][1] + \
                             ', \n\n Uw ' + value_field_edit.get() + \
                             ' bent met succes veranderd in het systeem.' \
                             ' \n\n Reageer aub niet op deze email. \n\n Fijne dag!'

                email_result = email_manager.send_email(user_data[0][0], 'Uw gegevens zijn veranderd', email_body)

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
    a_c_delete_user = AutocompleteCombobox(tab_delete, textvariable=value_user_delete)
    a_c_delete_user.set_completion_list(get_user_data())
    a_c_delete_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
    a_c_delete_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning', 'Weet jij zeker dat jij deze lid wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database_manager.execute_sql(
                '''DELETE FROM user WHERE knsa_licence_number = ?;''', (int(value_user_delete.get()[-6:]),))

            if result_delete:
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

    tab_view = ttk.Frame(notebook)
    notebook.add(tab_view, text="Bekijk Lid")

    label_user_view = ttk.Label(tab_view, text="Lid te Bekijken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_user_view = tk.StringVar(tab_view)
    value_user_view.set('Select')
    a_c_view_user = AutocompleteCombobox(tab_view, textvariable=value_user_view)
    a_c_view_user.set_completion_list(get_user_data())
    a_c_view_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
    a_c_view_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_user_type_view = ttk.Label(tab_view, text="Gebruikerstype:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_user_type_view = tk.StringVar(tab_view)
    label_user_type = ttk.Label(tab_view, textvariable=value_user_type_view) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_first_name_view = ttk.Label(tab_view, text="Voornaam:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_first_name_view = tk.StringVar(tab_view)
    label_user_first_name = ttk.Label(tab_view, textvariable=value_first_name_view) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    label_last_name_view = ttk.Label(tab_view, text="Familienaam:").grid(row=3, column=0, padx=5, pady=2, sticky="W")
    value_last_name_view = tk.StringVar(tab_view)
    label_user_last_name = ttk.Label(tab_view, textvariable=value_last_name_view) \
        .grid(row=3, column=1, padx=5, pady=2, sticky="W")

    label_date_of_birth_view = ttk.Label(tab_view, text="Geboorte Datum (DD-MM-YYYY):") \
        .grid(row=4, column=0, padx=5, pady=2, sticky="W")
    value_date_of_birth_view = tk.StringVar(tab_view)
    label_date_of_birth = ttk.Label(tab_view, textvariable=value_date_of_birth_view) \
        .grid(row=4, column=1, padx=5, pady=2, sticky="W")

    label_address_view = ttk.Label(tab_view, text="Adres:").grid(row=5, column=0, padx=5, pady=2, sticky="W")
    value_address_view = tk.StringVar(tab_view)
    label_address = ttk.Label(tab_view, textvariable=value_address_view) \
        .grid(row=5, column=1, padx=5, pady=2, sticky="W")

    label_city_view = ttk.Label(tab_view, text="Woonplaats:").grid(row=6, column=0, padx=5, pady=5, sticky="W")
    value_city_view = tk.StringVar(tab_view)
    label_city = ttk.Label(tab_view, textvariable=value_city_view) \
        .grid(row=6, column=1, padx=5, pady=2, sticky="W")

    label_post_code_view = ttk.Label(tab_view, text="Postcode:").grid(row=7, column=0, padx=5, pady=2, sticky="W")
    value_post_code_view = tk.StringVar(tab_view)
    label_post_code = ttk.Label(tab_view, textvariable=value_post_code_view) \
        .grid(row=7, column=1, padx=5, pady=2, sticky="W")

    label_telephone_number_view = ttk.Label(tab_view, text="Telefoonnummer:") \
        .grid(row=8, column=0, padx=5, pady=2, sticky="W")
    value_telephone_number_view = tk.StringVar(tab_view)
    label_telephone_number = ttk.Label(tab_view, textvariable=value_telephone_number_view) \
        .grid(row=8, column=1, padx=5, pady=2, sticky="W")

    label_email_address_view = ttk.Label(tab_view, text="Email Adres:") \
        .grid(row=9, column=0, padx=5, pady=2, sticky="W")
    value_email_address_view = tk.StringVar(tab_view)
    label_email_address = ttk.Label(tab_view, textvariable=value_email_address_view) \
        .grid(row=9, column=1, padx=5, pady=2, sticky="W")

    label_knsa_licence_number_view = ttk.Label(tab_view, text="KNSA Licentienummer:") \
        .grid(row=10, column=0, padx=5, pady=2, sticky="W")
    value_knsa_licence_number_view = tk.StringVar(tab_view)
    label_knsa_licence_number = ttk.Label(tab_view, textvariable=value_knsa_licence_number_view) \
        .grid(row=10, column=1, padx=5, pady=2, sticky="W")

    label_date_of_membership_view = ttk.Label(tab_view, text="Datum van Lidmaatschap Ingang (DD-MM-YYYY):") \
        .grid(row=11, column=0, padx=5, pady=2, sticky="W")
    value_date_of_membership_view = tk.StringVar(tab_view)
    label_date_of_membership = ttk.Label(tab_view, textvariable=value_date_of_membership_view) \
        .grid(row=11, column=1, padx=5, pady=2, sticky="W")

    button_submit_view = ttk.Button(tab_view, text="Bekijk", command=lambda: clicked_view()) \
        .grid(row=12, column=0, padx=10, pady=15)

    def clicked_view():
        fields3 = {
            1: 'Standaard',
            2: 'Beheerder'
        }

        result_view = database_manager.execute_sql(
            '''SELECT type, first_name, last_name, date_of_birth, address, city, post_code, telephone_number,
             email_address, knsa_licence_number, date_of_membership FROM user WHERE knsa_licence_number = ?''',
            (int(value_user_view.get()[-6:]),))

        # May need to convert date formats here if this fails
        value_user_type_view.set(fields3.get(result_view[0][0]))
        value_first_name_view.set(result_view[0][1])
        value_last_name_view.set(result_view[0][2])
        value_date_of_birth_view.set(input_validation.convert_output_date(result_view[0][3]))
        value_address_view.set(result_view[0][4])
        value_city_view.set(result_view[0][5])
        value_post_code_view.set(result_view[0][6])
        value_telephone_number_view.set(result_view[0][7])
        value_email_address_view.set(result_view[0][8])
        value_knsa_licence_number_view.set(result_view[0][9])
        value_date_of_membership_view.set(input_validation.convert_output_date(result_view[0][10]))

    button_cancel_view = ttk.Button(tab_view, text="Annuleren", command=popup.destroy) \
        .grid(row=12, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_firearm_settings(user_session):
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Vuurwapen Instellingen: " + "(" + user_session + ") ")

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

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=2, column=0, padx=10, pady=15)

    def clicked_new():
        firearm_list_new = [value_type_new.get()]

        if firearm_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
            result_new = database_manager.execute_sql(
                '''INSERT INTO firearm (type) VALUES (?)''', (value_type_new.get().lower(),))

            if result_new:
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een niewe vuurwapen aangemaakt")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=2, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder Vuurwapen")

    label_type_delete = ttk.Label(tab_delete, text="Vuurwapen te Verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    a_c_delete_firearm = AutocompleteCombobox(tab_delete, textvariable=value_type_delete)
    a_c_delete_firearm.set_completion_list(get_firearm_type())
    a_c_delete_firearm.config(width=max([sum([len(str(q)) for q in i]) for i in get_firearm_type()]) + 1)
    a_c_delete_firearm.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=2, column=0, padx=10, pady=15, sticky="W")

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze vuurwapen wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database_manager.execute_sql(
                '''DELETE FROM firearm WHERE type = ?''', (value_type_delete.get(),))

            if result_delete:
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een vuurwapen verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=2, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_ammunition_settings(user_session):
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Munitie Instellingen: " + "(" + user_session + ") ")

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
    entry_stock_new.grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_new():
        ammunition_list_new = [value_type_new.get()]

        if ammunition_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        elif input_validation.is_float(value_price_new.get()) is False:
            messagebox.showerror(title="Error", message="Vul aub een valide prijs in")
            popup.lift()
        elif input_validation.is_int(value_stock_new.get()) is False:
            messagebox.showerror(title="Error", message="Vul aub een valide voorraad in")
            popup.lift()
        else:
            result_new = database_manager.execute_sql(
                '''INSERT INTO ammunition (type, price, stock) VALUES (?, ?, ?)''',
                (value_type_new.get().lower(), value_price_new.get(), value_stock_new.get()))

            if result_new:
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
    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    a_c_edit_ammunition_type = AutocompleteCombobox(tab_edit, textvariable=value_type_edit)
    a_c_edit_ammunition_type.set_completion_list(get_ammunition_type())
    a_c_edit_ammunition_type.config(width=max([sum([len(str(q)) for q in i]) for i in get_ammunition_type()]) + 2)
    a_c_edit_ammunition_type.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    a_c_edit_ammunition_field = AutocompleteCombobox(tab_edit, textvariable=value_field_edit)
    a_c_edit_ammunition_field.set_completion_list(fields.keys())
    a_c_edit_ammunition_field.config(width=max([sum([len(str(q)) for q in i]) for i in fields.keys()]) + 1)
    a_c_edit_ammunition_field.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=10) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        if fields.get(value_field_edit.get()) == 'stock':
            if input_validation.is_int(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide voorraad in")
                popup.lift()
            else:
                current_stock = database_manager.execute_sql(
                    '''SELECT stock from ammunition WHERE type = ?''', (value_type_edit.get(),))
                new_value = int(current_stock[0][0] + value_update_edit.get())
        else:
            if input_validation.is_float(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide prijs in")
                popup.lift()
            else:
                new_value = value_update_edit.get()

        if fields.get(value_field_edit.get()) == 'price':
            result_edit = database_manager.execute_sql(
                '''UPDATE ammunition SET price = ? WHERE type = ?''', (new_value, value_type_edit.get()))
        else:
            result_edit = database_manager.execute_sql(
                '''UPDATE ammunition SET stock = ? WHERE type = ?''', (new_value, value_type_edit.get()))

        if result_edit:
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
    a_c_delete_ammunition = AutocompleteCombobox(tab_delete, textvariable=value_type_delete)
    a_c_delete_ammunition.set_completion_list(get_ammunition_type())
    a_c_delete_ammunition.config(width=max([sum([len(str(q)) for q in i]) for i in get_ammunition_type()]) + 1)
    a_c_delete_ammunition.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=1, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze munitie wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database_manager.execute_sql(
                '''DELETE FROM ammunition WHERE type = ?''', ((value_type_delete.get()),))

            if result_delete:
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een lid verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=1, column=1, padx=10, pady=15)

    tab_view = ttk.Frame(notebook)
    notebook.add(tab_view, text="Bekijk")

    label_type_view = ttk.Label(tab_view, text="Munitie te bekijken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_view = tk.StringVar(tab_view)
    value_type_view.set("Select")
    a_c_view_ammunition = AutocompleteCombobox(tab_view, textvariable=value_type_view)
    a_c_view_ammunition.set_completion_list(get_ammunition_type())
    a_c_view_ammunition.config(width=max([sum([len(str(q)) for q in i]) for i in get_ammunition_type()]) + 2)
    a_c_view_ammunition.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_view = ttk.Label(tab_view, text="Prijs (EUR):") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_view = tk.StringVar(tab_view)
    label_price = ttk.Label(tab_view, textvariable=value_price_view) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_view = ttk.Label(tab_view, text="Voorraad:") \
        .grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_view = tk.StringVar(tab_view)
    label_stock = ttk.Label(tab_view, textvariable=value_stock_view) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_view = ttk.Button(tab_view, text="Bekijk", command=lambda: clicked_view()) \
        .grid(row=3, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_view():
        result_view = database_manager.execute_sql(
            '''SELECT price, stock FROM ammunition WHERE type = ?''', (value_type_view.get(),))

        value_price_view.set(result_view[0][0])
        value_stock_view.set(result_view[0][1])

    button_cancel_view = ttk.Button(tab_view, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_scorecard_settings(user_session):
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Score Kaart Instellingen: " + "(" + user_session + ") ")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

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

    value_type_edit = tk.StringVar(tab_edit)
    value_type_edit.set("Select")
    a_c_edit_scorecard_type = AutocompleteCombobox(tab_edit, textvariable=value_type_edit)
    a_c_edit_scorecard_type.set_completion_list(fields2.keys())
    a_c_edit_scorecard_type.config(width=max([len(i) for i in fields2.keys()]) + 1)
    a_c_edit_scorecard_type.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_field_edit = ttk.Label(tab_edit, text="Gegeven te Bewerken:") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_field_edit = tk.StringVar(tab_edit)
    value_field_edit.set("Select")
    a_c_edit_scorecard_field = AutocompleteCombobox(tab_edit, textvariable=value_field_edit)
    a_c_edit_scorecard_field.set_completion_list(fields.keys())
    a_c_edit_scorecard_field.config(width=max([len(i) for i in fields.keys()]) + 1)
    a_c_edit_scorecard_field.grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_update_edit = ttk.Label(tab_edit, text="Nieuwe Waarde:").grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_update_edit = tk.DoubleVar(tab_edit)
    entry_update_edit = ttk.Entry(tab_edit, textvariable=value_update_edit, width=10) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_edit = ttk.Button(tab_edit, text="Invoeren", command=lambda: clicked_edit()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_edit():
        if fields.get(value_field_edit.get()) == 'stock':
            if input_validation.is_int(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide voorraad in")
                popup.lift()
            else:
                current_stock = database_manager.execute_sql(
                    '''SELECT stock from scorecard WHERE type = ?''', (fields2.get(value_type_edit.get()),))
                new_value = int(current_stock[0][0] + value_update_edit.get())
        else:
            if input_validation.is_float(value_update_edit.get()) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide prijs in")
                popup.lift()
            else:
                new_value = value_update_edit.get()

        if fields.get(value_field_edit.get()) == 'price':
            result_edit = database_manager.execute_sql(
                '''UPDATE scorecard SET price = ? WHERE type = ?''', (new_value, fields2.get(value_type_edit.get())))
        else:
            result_edit = database_manager.execute_sql(
                '''UPDATE scorecard SET stock = ? WHERE type = ?''', (new_value, fields2.get(value_type_edit.get())))

        if result_edit:
            messagebox.showinfo(title="Information",
                                message="Het systeem heeft met succes een scorecard aangepast")
            popup.destroy()
        else:
            messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
            popup.lift()

    button_cancel_edit = ttk.Button(tab_edit, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    tab_view = ttk.Frame(notebook)
    notebook.add(tab_view, text="Bekijk")

    label_type_view = ttk.Label(tab_view, text="Scorecard te bekijken:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_view = tk.StringVar(tab_view)
    a_c_view_scorecard = AutocompleteCombobox(tab_view, textvariable=value_type_view)
    a_c_view_scorecard.set_completion_list(fields2.keys())
    a_c_view_scorecard.config(width=max([len(i) for i in fields2.keys()]) + 1)
    a_c_view_scorecard.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    label_price_view = ttk.Label(tab_view, text="Prijs (EUR):") \
        .grid(row=1, column=0, padx=5, pady=2, sticky="W")
    value_price_view = tk.StringVar(tab_view)
    label_price = ttk.Label(tab_view, textvariable=value_price_view) \
        .grid(row=1, column=1, padx=5, pady=2, sticky="W")

    label_stock_view = ttk.Label(tab_view, text="Voorraad:") \
        .grid(row=2, column=0, padx=5, pady=2, sticky="W")
    value_stock_view = tk.StringVar(tab_view)
    label_stock = ttk.Label(tab_view, textvariable=value_stock_view) \
        .grid(row=2, column=1, padx=5, pady=2, sticky="W")

    button_submit_view = ttk.Button(tab_view, text="Bekijk", command=lambda: clicked_view()) \
        .grid(row=3, column=0, padx=10, pady=15)

    def clicked_view():
        result_view = database_manager.execute_sql(
            '''SELECT price, stock FROM scorecard WHERE type = ?''', (fields2.get(value_type_view.get()),))

        value_price_view.set(result_view[0][0])
        value_stock_view.set(result_view[0][1])

    button_cancel_view = ttk.Button(tab_view, text="Annuleren", command=popup.destroy) \
        .grid(row=3, column=1, padx=10, pady=15)

    popup.mainloop()


def popup_discipline_settings(user_session):
    # main window holding all elements
    popup = tk.Tk()
    popup.wm_title("Discipline Instellingen: " + "(" + user_session + ") ")

    # notebook holding the tabs
    notebook = ttk.Notebook(popup)
    notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky="nsew")

    # creation of the new tab
    tab_new = ttk.Frame(notebook)
    notebook.add(tab_new, text="Nieuwe")

    label_type_new = ttk.Label(tab_new, text="Type Discipline:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_new = tk.StringVar(tab_new)
    entry_type_new = ttk.Entry(tab_new, textvariable=value_type_new, width=20) \
        .grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_new = ttk.Button(tab_new, text="Invoeren", command=lambda: clicked_new()) \
        .grid(row=1, column=0, padx=10, pady=15)

    def clicked_new():
        discipline_list_new = [value_type_new.get()]

        if discipline_list_new.count('') > 0:
            messagebox.showerror(title="Error", message="Vul aub alle velden in voordat je verdergaat")
            popup.lift()
        else:
            result_new = database_manager.execute_sql(
                '''INSERT INTO discipline (type) VALUES (?)''', (value_type_new.get(),))

            if result_new:
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes een niewe discipline aangemaakt")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met invoeren van de data")
                popup.lift()

    button_cancel_new = ttk.Button(tab_new, text="Annuleren", command=popup.destroy) \
        .grid(row=1, column=1, padx=10, pady=15)

    tab_delete = ttk.Frame(notebook)
    notebook.add(tab_delete, text="Verwijder")

    label_type_delete = ttk.Label(tab_delete, text="Discipline te verwijderen:") \
        .grid(row=0, column=0, padx=5, pady=2, sticky="W")
    value_type_delete = tk.StringVar(tab_delete)
    value_type_delete.set("Select")
    a_c_delete_discipline = AutocompleteCombobox(tab_delete, textvariable=value_type_delete)
    a_c_delete_discipline.set_completion_list(get_discipline_type())
    a_c_delete_discipline.config(width=max([sum([len(str(q)) for q in i]) for i in get_discipline_type()]) + 1)
    a_c_delete_discipline.grid(row=0, column=1, padx=5, pady=2, sticky="W")

    button_submit_delete = ttk.Button(tab_delete, text="Verwijder", command=lambda: clicked_delete()) \
        .grid(row=1, column=0, padx=10, pady=15)

    # this should delete the record in the dropdown menu
    def clicked_delete():
        ays = messagebox.askquestion('Warning',
                                     'Weet jij zeker dat jij deze discipline wil verwijderen?', icon="warning")

        if ays == 'yes':
            result_delete = database_manager.execute_sql(
                '''DELETE FROM discipline WHERE type = ?''', (value_type_delete.get(),))

            if result_delete:
                messagebox.showinfo(title="Information",
                                    message="Het systeem heeft met succes het discipline verwijderd")
                popup.destroy()
            else:
                messagebox.showerror(title="Error", message="Er was een fout met verwijderen van de data")
                popup.lift()
        else:
            popup.lift()

    button_cancel_delete = ttk.Button(tab_delete, text="Annuleren", command=popup.destroy) \
        .grid(row=1, column=1, padx=10, pady=15)

    popup.mainloop()


# TODO add feature to ensure a user submits a score at least once every 10 weeks
class ShootingClub(tk.Tk):

    def __init__(self, user_session, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.user_session = user_session

        result = database_manager.execute_sql(
            '''SELECT first_name FROM user WHERE knsa_licence_number = ?''', (user_session,))

        # tk.Tk.iconbitmap(self, default="logo_16_16.ico")
        tk.Tk.wm_title(self, "Schietvereniging - Prinses Juliana: " + "(" + user_session + ") " + result[0][0])

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu_bar = tk.Menu(container)
        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label="Lid Instellingen", command=lambda: popup_user_settings(user_session))
        file_menu.add_command(label="Vuurapen Instellingen", command=lambda: popup_firearm_settings(user_session))
        file_menu.add_command(label="Discipline Instellingen", command=lambda: popup_discipline_settings(user_session))
        file_menu.add_command(label="Munitie Instellingen", command=lambda: popup_ammunition_settings(user_session))
        file_menu.add_command(label="Score Kaart Instellingen", command=lambda: popup_scorecard_settings(user_session))
        file_menu.add_separator()
        file_menu.add_command(label="Sluiten", command=lambda: self.on_exit(), accelerator="Ctrl+Q")
        menu_bar.add_cascade(label="Instellingen", menu=file_menu)

        tk.Tk.config(self, menu=menu_bar)

        self.frames = {}

        for F in (MainMenu, ScorePage, FinancePage):
            frame = F(container, self, user_session)
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
                                  'Weet je zeker dat je de applicatie wilt sluiten?', icon="warning") == 'yes':
            self.destroy()
            self.quit()


class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)

        '''self.style = ttk.Style()
        print(self.style.theme_names())
        self.style.theme_use('xpnative')'''

        # tk.Tk.iconbitmap(self, default="logo_16_16.ico")
        tk.Tk.wm_title(self, "Schietvereniging - Prinses Juliana")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        label_username = ttk.Label(container, text="KNSA Licentie Nummer:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_username = tk.StringVar(container)
        entry_username = ttk.Entry(container, textvariable=value_username) \
            .grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_password = ttk.Label(container, text="Wachtwoord:").grid(row=1, column=0, padx=5, pady=2, sticky="W")
        value_password = tk.StringVar(container)
        entry_password = ttk.Entry(container, textvariable=value_password, show='*') \
            .grid(row=1, column=1, padx=5, pady=2, sticky="W")

        button_login = ttk.Button(container, text="Login", command=lambda: login_clicked()) \
            .grid(row=2, column=0, padx=10, pady=15)
        button_reset = ttk.Button(container, text="Reset", command=lambda: reset_clicked()) \
            .grid(row=2, column=1, padx=10, pady=15)

        def login_clicked():
            user_details = database_manager.execute_sql(
                '''SELECT password, type FROM user WHERE knsa_licence_number = ?''', (value_username.get(),))

            valid = password_manager.verify_password(value_password.get(), user_details[0][0])

            if valid and user_details[0][1] == 2:
                app2.quit()
                app2.destroy()

                app = ShootingClub(value_username.get())
                app.geometry("860x730")
                app.minsize(860, 730)
                app.maxsize(860, 730)

                ani = animation.FuncAnimation(f, animate, interval=8000)

                app.mainloop()

            else:
                messagebox.showerror(title="Error", message="Verkeerde KNSA en wachtwoord combinatie")
                reset_clicked()
                self.lift()

        def reset_clicked():
            value_username.set('')
            value_password.set('')


# TODO add feature to track users, classes and stock
# TODO add feature to allow sending of data to EXCEL
class MainMenu(tk.Frame):

    def __init__(self, parent, controller, user_session):
        self.user_session = user_session

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Score", command=lambda: controller.show_frame(ScorePage))
        button1.pack()

        button2 = ttk.Button(self, text="Finance", command=lambda: controller.show_frame(FinancePage))
        button2.pack()

        results = database_manager.execute_sql('''SELECT knsa_licence_number, first_name, last_name FROM user;''')

        tree = ttk.Treeview(self)
        tree["columns"] = 'KNSA', 'First Name', 'Last Name'
        tree.column('KNSA', stretch="yes")
        tree.column('First Name', stretch="yes")
        tree.column('Last Name', stretch="yes")
        tree.heading('KNSA', text='KNSA')
        tree.heading('First Name', text='Voornaam')
        tree.heading('Last Name', text='Familienaam')
        tree.insert("", 'end', values=(results[0][0], results[0][1], results[0][2]))
        tree.pack()


# TODO add matplotlib functionality
class ScorePage(tk.Frame):

    def __init__(self, parent, controller, user_session):
        self.user_session = user_session

        tk.Frame.__init__(self, parent)

        frame_left = tk.Frame(self)
        frame_left.pack(side="left")

        button_main_menu = ttk.Button(frame_left, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button_main_menu.pack()

        button_finance_page = ttk.Button(frame_left,
                                         text="Finance",
                                         command=lambda: controller.show_frame(FinancePage))
        button_finance_page.pack()

        frame_right = tk.Frame(self)
        frame_right.pack(side="right", fill='both', expand=True)

        label_frame_top = tk.LabelFrame(frame_right, text="Submit Score")
        label_frame_top.pack(side="top", fill="x", expand=True)

        frame_top_left = tk.Frame(label_frame_top)
        frame_top_left.pack(side="left", anchor="nw")

        label_user_left = ttk.Label(frame_top_left, text="Lid:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        value_user_left = tk.StringVar(frame_top_left)
        value_user_left.set("Select")
        a_c_score_user = AutocompleteCombobox(frame_top_left, textvariable=value_user_left)
        a_c_score_user.set_completion_list(get_user_data())
        a_c_score_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
        a_c_score_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_firearm_left = ttk.Label(frame_top_left, text="Vuurwapen:") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="W")

        value_firearm_left = tk.StringVar(frame_top_left)
        value_firearm_left.set("Select")
        a_c_score_firearm = AutocompleteCombobox(frame_top_left, textvariable=value_firearm_left)
        a_c_score_firearm.set_completion_list(get_firearm_type())
        a_c_score_firearm.config(width=max([sum([len(str(q)) for q in i]) for i in get_firearm_type()]) + 1)
        a_c_score_firearm.grid(row=1, column=1, padx=5, pady=2, sticky="W")

        label_discipline = ttk.Label(frame_top_left, text="Discipline:") \
            .grid(row=2, column=0, padx=5, pady=5, sticky="W")
        value_discipline = tk.StringVar(frame_top_left)
        value_discipline.set('Select')
        a_c_score_discipline = AutocompleteCombobox(frame_top_left, textvariable=value_discipline)
        a_c_score_discipline.set_completion_list(get_discipline_type())
        a_c_score_discipline.config(width=max([sum([len(str(q)) for q in i]) for i in get_discipline_type()]) + 1)
        a_c_score_discipline.grid(row=2, column=1, padx=5, pady=2, sticky="W")

        label_own_firearm = ttk.Label(frame_top_left, text="Eigen Wapen:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="W")
        value_own_firearm = tk.IntVar(frame_top_left)
        value_own_firearm.set(0)
        checkbutton_own_firearm = ttk.Checkbutton(frame_top_left, variable=value_own_firearm) \
            .grid(row=3, column=1, padx=5, pady=5, sticky="W")

        frame_top_right = tk.Frame(label_frame_top)
        frame_top_right.pack(side="top", anchor="nw")

        frame_inner_top_right = tk.Frame(frame_top_right)
        frame_inner_top_right.pack(side="top", anchor="nw")

        label_scorecard1 = ttk.Label(frame_inner_top_right, text="1e Scorecard:") \
            .grid(row=2, column=0, padx=5, pady=5, sticky="W")

        value_scorecard1_shot1 = tk.IntVar(frame_inner_top_right)
        value_scorecard1_shot1.set(0)
        entry_scorecard1_shot1 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard1_shot1, width=3)
        entry_scorecard1_shot1.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        value_scorecard1_shot2 = tk.IntVar(frame_inner_top_right)
        value_scorecard1_shot2.set(0)
        entry_scorecard1_shot2 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard1_shot2, width=3)
        entry_scorecard1_shot2.grid(row=2, column=2, padx=5, pady=5, sticky="W")

        value_scorecard1_shot3 = tk.IntVar(frame_inner_top_right)
        value_scorecard1_shot3.set(0)
        entry_scorecard1_shot3 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard1_shot3, width=3)
        entry_scorecard1_shot3.grid(row=2, column=3, padx=5, pady=5, sticky="W")

        value_scorecard1_shot4 = tk.IntVar(frame_inner_top_right)
        value_scorecard1_shot4.set(0)
        entry_scorecard1_shot4 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard1_shot4, width=3)
        entry_scorecard1_shot4.grid(row=2, column=4, padx=5, pady=5, sticky="W")

        value_scorecard1_shot5 = tk.IntVar(frame_inner_top_right)
        value_scorecard1_shot5.set(0)
        entry_scorecard1_shot5 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard1_shot5, width=3)
        entry_scorecard1_shot5.grid(row=2, column=5, padx=5, pady=5, sticky="W")

        label_scorecard1_valuation = ttk.Label(frame_inner_top_right, text="Totaal Scorecard 1:") \
            .grid(row=2, column=6, padx=5, pady=5, sticky="W")
        total_scorecard1 = tk.IntVar()
        total_scorecard1.set(0)
        label_scorecard1_total = ttk.Label(frame_inner_top_right, textvariable=total_scorecard1) \
            .grid(row=2, column=7, padx=5, pady=5, sticky="W")

        label_scorecard_2 = ttk.Label(frame_inner_top_right, text="2e Scorecard:") \
            .grid(row=3, column=0, padx=5, pady=5, sticky="W")

        value_scorecard2_shot1 = tk.IntVar(frame_inner_top_right)
        value_scorecard2_shot1.set(0)
        entry_scorecard2_shot1 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard2_shot1, width=3)
        entry_scorecard2_shot1.grid(row=3, column=1, padx=5, pady=5, sticky="W")

        value_scorecard2_shot2 = tk.IntVar(frame_inner_top_right)
        value_scorecard2_shot2.set(0)
        entry_scorecard2_shot2 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard2_shot2, width=3)
        entry_scorecard2_shot2.grid(row=3, column=2, padx=5, pady=5, sticky="W")

        value_scorecard2_shot3 = tk.IntVar(frame_inner_top_right)
        value_scorecard2_shot3.set(0)
        entry_scorecard2_shot3 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard2_shot3, width=3)
        entry_scorecard2_shot3.grid(row=3, column=3, padx=5, pady=5, sticky="W")

        value_scorecard2_shot4 = tk.IntVar(frame_inner_top_right)
        value_scorecard2_shot4.set(0)
        entry_scorecard2_shot4 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard2_shot4, width=3)
        entry_scorecard2_shot4.grid(row=3, column=4, padx=5, pady=5, sticky="W")

        value_scorecard2_shot5 = tk.IntVar(frame_inner_top_right)
        value_scorecard2_shot5.set(0)
        entry_scorecard2_shot5 = ttk.Entry(frame_inner_top_right, textvariable=value_scorecard2_shot5, width=3)
        entry_scorecard2_shot5.grid(row=3, column=5, padx=5, pady=5, sticky="W")

        label_scorecard2_valuation = ttk.Label(frame_inner_top_right, text="Totaal Scorecard 2:") \
            .grid(row=3, column=6, padx=5, pady=5, sticky="W")
        total_scorecard2 = tk.IntVar()
        total_scorecard2.set(0)
        label_scorecard2_total = ttk.Label(frame_inner_top_right, textvariable=total_scorecard2) \
            .grid(row=3, column=7, padx=5, pady=5, sticky="W")

        frame_inner_bottom_right = tk.Frame(frame_top_right)
        frame_inner_bottom_right.pack(side="bottom")

        button_submit_top = ttk.Button(frame_inner_bottom_right,
                                       text="Invoeren",
                                       command=lambda: clicked_submit_top()) \
            .grid(row=0, column=4, padx=10, pady=15, sticky="W")

        def clicked_submit_top():
            if value_user_left.get in get_user_data() \
                    or value_firearm_left.get() in get_firearm_type() or \
                    value_discipline.get() in get_discipline_type():
                dates = input_validation.date_range(1)

                last_entries = database_manager.execute_sql(
                    '''SELECT date FROM score WHERE shooter = ? AND discipline = ? AND date BETWEEN ? AND ?''',
                    (value_user_left.get()[-6:], value_discipline.get(), dates[0], dates[1]))

                if last_entries:
                    messagebox.showerror(title="Error", message="De gebruiker " + value_user_left.get()[-6:] +
                                                                " heeft al scores ingediend deze week,"
                                                                " voor deze discipline naamelijks op " +
                                                                str(last_entries[0]))
                else:
                    if clicked_total_top() is not False:
                        totals = clicked_total_top()

                        result_submit_left = database_manager.execute_sql(
                            '''INSERT INTO score (card_one_shot_one, card_one_shot_two, card_one_shot_three, card_one_shot_four,
                            card_one_shot_five,card_one_total, card_two_shot_one, card_two_shot_two, card_two_shot_three,
                            card_two_shot_four, card_two_shot_five, card_two_total, date, shooter, submitter, discipline,
                            firearm, own_firearm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', (
                                value_scorecard1_shot1.get(),
                                value_scorecard1_shot2.get(),
                                value_scorecard1_shot3.get(),
                                value_scorecard1_shot4.get(),
                                value_scorecard1_shot5.get(),
                                totals[0],
                                value_scorecard2_shot1.get(),
                                value_scorecard2_shot2.get(),
                                value_scorecard2_shot3.get(),
                                value_scorecard2_shot4.get(),
                                value_scorecard2_shot5.get(),
                                totals[1],
                                date.today(),
                                value_user_left.get()[-6:],
                                user_session,
                                value_discipline.get(),
                                value_firearm_left.get(),
                                value_own_firearm.get()))

                        if result_submit_left:
                            messagebox.showinfo(title="Information",
                                                message="Het systeem heeft met success de score voor "
                                                        + value_user_left.get()[-6:] + " ingevoerd")

                            sc1 = [value_scorecard1_shot1.get(),
                                   value_scorecard1_shot2.get(),
                                   value_scorecard1_shot3.get(),
                                   value_scorecard1_shot4.get(),
                                   value_scorecard1_shot5.get(),
                                   totals[0]]

                            sc2 = [value_scorecard2_shot1.get(),
                                   value_scorecard2_shot2.get(),
                                   value_scorecard2_shot3.get(),
                                   value_scorecard2_shot4.get(),
                                   value_scorecard2_shot5.get(),
                                   totals[1]]

                            user_data = database_manager.execute_sql(
                                '''SELECT email_address, first_name FROM user WHERE knsa_licence_number = ?''',
                                (value_user_left.get()[-6:],))

                            email_body = 'Hallo ' + user_data[0][1] + ', \n\n U scores zijn voor ' + str(
                                input_validation.convert_output_date(str(date.today()))) + \
                                         ' in de database ingevoerd. U heeft met ' + value_firearm_left.get() + \
                                         ' geschoten. En discipline ' + value_discipline.get() + \
                                         '\n\n U heeft voor uw eerste kaart: \n schot 1: ' + str(
                                value_scorecard1_shot1.get()) + '\n schot 2: ' + str(
                                value_scorecard1_shot2.get()) + '\n schot 3: ' + str(
                                value_scorecard1_shot3.get()) + '\n schot 4: ' + str(
                                value_scorecard1_shot4.get()) + '\n schot 5: ' + str(
                                value_scorecard1_shot5.get()) + '\n met een totaal score van: ' + str(
                                totals[0]) + '\n\n en voor uw tweede kaart: \n schot 1: ' + str(
                                value_scorecard2_shot1.get()) + '\n schot 2: ' + str(
                                value_scorecard2_shot2.get()) + '\n schot 3: ' + str(
                                value_scorecard2_shot3.get()) + '\n schot 4: ' + str(
                                value_scorecard2_shot4.get()) + '\n schot 5: ' + str(
                                value_scorecard2_shot5.get()) + '\n met een totaal score van: ' + str(
                                totals[1]) + '\n\n reageer aub niet op deze email. \n\n Fijne dag!'

                            email_result = email_manager.send_email(user_data[0][0], 'U heeft nieuwe scores ingediend',
                                                                    email_body)

                            if email_result:
                                clicked_reset_top()
                            else:
                                messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")
                        else:
                            messagebox.showerror(title="Error",
                                                 message="Er was een fout met de stuuren van scores naar de database")
            else:
                messagebox.showerror(title="Error",
                                     message="Vul aub een valide waarde in voor gebruiker, wapen of discipline")

        def clicked_reset_top():
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
            value_own_firearm.set(0)
            value_discipline.set('Select')
            value_firearm_left.set('Select')
            value_user_left.set('Select')

        button_reset = ttk.Button(frame_inner_bottom_right, text="Reset", command=lambda: clicked_reset_top()) \
            .grid(row=0, column=5, padx=10, pady=15, sticky="W")

        def clicked_total_top():
            scores = [value_scorecard1_shot1.get(),
                      value_scorecard1_shot2.get(),
                      value_scorecard1_shot3.get(),
                      value_scorecard1_shot4.get(),
                      value_scorecard1_shot5.get(),
                      value_scorecard2_shot1.get(),
                      value_scorecard2_shot2.get(),
                      value_scorecard2_shot3.get(),
                      value_scorecard2_shot4.get(),
                      value_scorecard2_shot5.get()]

            if all(i <= 10 for i in scores):
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

                return [total_scorecard1.get(), total_scorecard2.get()]
            else:
                messagebox.showerror(title="Error", message="U heeft een score ingevuld die meer dan 10 is")
                return False

        button_total = ttk.Button(frame_inner_bottom_right, text="Reken Totaal", command=lambda: clicked_total_top()) \
            .grid(row=0, column=6, padx=10, pady=15, sticky="W")

        label_frame_bottom = tk.LabelFrame(frame_right, text="View Scores")
        label_frame_bottom.pack(side="right", fill="both", expand=True)

        frame_menu = tk.Frame(label_frame_bottom)
        frame_menu.pack(side="bottom", fill="x")

        label_user_matplot = ttk.Label(frame_menu, text="Lid:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_user_matplot = tk.StringVar(frame_menu)
        value_user_matplot.set("Select")
        a_c_matplot_score_user = AutocompleteCombobox(frame_menu, textvariable=value_user_matplot)
        a_c_matplot_score_user.set_completion_list(get_user_data())
        a_c_matplot_score_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
        a_c_matplot_score_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_firearm_matplot = ttk.Label(frame_menu, text="Vuurwapen:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="W")
        value_firearm_matplot = tk.StringVar(frame_menu)
        value_firearm_matplot.set("Select")
        a_c_matplot_score_firearm = AutocompleteCombobox(frame_menu, textvariable=value_firearm_matplot)
        a_c_matplot_score_firearm.set_completion_list(get_firearm_type())
        a_c_matplot_score_firearm.config(width=max([sum([len(str(q)) for q in i]) for i in get_firearm_type()]) + 1)
        a_c_matplot_score_firearm.grid(row=0, column=3, padx=5, pady=2, sticky="W")

        label_discipline_matplot = ttk.Label(frame_menu, text="Discipline:") \
            .grid(row=1, column=2, padx=5, pady=2, sticky="W")
        value_discipline_matplot = tk.StringVar(frame_menu)
        value_discipline_matplot.set("Select")
        a_c_matplot_score_discipline = AutocompleteCombobox(frame_menu, textvariable=value_discipline_matplot)
        a_c_matplot_score_discipline.set_completion_list(get_firearm_type())
        a_c_matplot_score_discipline.config(
            width=max([sum([len(str(q)) for q in i]) for i in get_discipline_type()]) + 1)
        a_c_matplot_score_discipline.grid(row=1, column=3, padx=5, pady=2, sticky="W")

        label_date_from_matplot = ttk.Label(frame_menu, text="Datum van (DD-MM-YYYY):") \
            .grid(row=0, column=4, padx=5, pady=2, sticky="W")
        value_date_from_matplot = tk.StringVar(frame_menu)
        entry_date_from_matplot = ttk.Entry(frame_menu, textvariable=value_date_from_matplot, width=10) \
            .grid(row=0, column=5, padx=5, pady=2, sticky="W")

        label_date_to_matplot = ttk.Label(frame_menu, text="Datum tot (DD-MM-YYYY):") \
            .grid(row=1, column=4, padx=5, pady=2, sticky="W")
        value_date_to_matplot = tk.StringVar(frame_menu)
        entry_date_to_matplot = ttk.Entry(frame_menu, textvariable=value_date_to_matplot, width=10) \
            .grid(row=1, column=5, padx=5, pady=2, sticky="W")

        def clicked_show():
            if input_validation.is_date(str(input_validation.convert_input_date(
                    value_date_from_matplot.get()))) is False and input_validation.is_date(
                str(input_validation.convert_input_date(value_date_to_matplot.get()))) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide datum in")
                value_date_from_matplot.set('')
                value_date_to_matplot.set('')
            elif value_user_matplot.get() not in get_user_data():
                messagebox.showerror(title="Error", message="Vul aub een valide lid in")
            else:
                if value_date_from_matplot.get() == 'Select' and value_date_to_matplot.get() == 'Select':
                    result = database_manager.execute_sql(
                        '''SELECT date, card_one_total, card_two_total FROM score WHERE shooter = ? AND firearm= ?
                         ORDER BY date''', (value_user_matplot.get()[-6:], value_firearm_matplot.get()))
                else:
                    result = database_manager.execute_sql(
                        '''SELECT date, card_one_total, card_two_total FROM score WHERE shooter = ? AND firearm = ? 
                        AND date BETWEEN ? AND ? ORDER BY date''',
                        (value_user_matplot.get()[-6:], value_firearm_matplot.get(),
                         input_validation.convert_input_date(value_date_from_matplot.get()),
                         input_validation.convert_input_date(value_date_to_matplot.get())))

            print(result)

        button_show = ttk.Button(frame_menu, text="Laden", command=lambda: clicked_show()) \
            .grid(row=0, column=6, padx=5, pady=2, sticky="W")

        def clicked_reset_matplot():
            value_date_from_matplot.set('')
            value_date_to_matplot.set('')
            value_user_matplot.set('Select')
            value_firearm_matplot.set('Select')
            value_discipline_matplot.set('Select')

        button_reser_matplot = ttk.Button(frame_menu, text="Reset", command=lambda: clicked_reset_matplot()) \
            .grid(row=1, column=6, padx=5, pady=2, sticky="W")

        # matplotlib graph starts here
        frame_matplot = tk.Frame(label_frame_bottom)
        frame_matplot.pack(side="top", fill="both")

        canvas = FigureCanvasTkAgg(f, frame_matplot)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# TODO add matplotlib functionality
class FinancePage(tk.Frame):

    def __init__(self, parent, controller, user_session):
        self.user_session = user_session

        tk.Frame.__init__(self, parent)

        frame_left = tk.Frame(self)
        frame_left.pack(side="left")

        button_main_menu = ttk.Button(frame_left, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        button_main_menu.pack()

        button_finance_page = ttk.Button(frame_left,
                                         text="Score",
                                         command=lambda: controller.show_frame(ScorePage))
        button_finance_page.pack()

        frame_right = tk.Frame(self)
        frame_right.pack(side="right", fill="both", expand=True)

        frame_top = tk.Frame(frame_right)
        frame_top.pack(side="top", fill="both", expand=True)

        label_frame_top = tk.LabelFrame(frame_top, text="Verkoop")
        label_frame_top.pack(side="top", fill="both", expand=True)

        frame_inner_top = tk.Frame(label_frame_top)
        frame_inner_top.pack(side="top", fill="x")

        frame_inner_bottom = tk.Frame(label_frame_top)
        frame_inner_bottom.pack(side="bottom", fill="x")

        label_frame_top_left = tk.Frame(frame_inner_top)
        label_frame_top_left.pack(side="left", fill="both", expand=True)

        frame_ammunition_top = tk.Frame(label_frame_top_left)
        frame_ammunition_top.pack(side="top", anchor="nw")

        frame_ammunition_middle = tk.Frame(label_frame_top_left)
        frame_ammunition_middle.pack(anchor="nw")

        label_ammunition_type = ttk.Label(frame_ammunition_middle, text="Munitie type:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_ammunition_type = tk.StringVar(frame_ammunition_middle)
        value_ammunition_type.set("Select")
        a_c_transaction_ammunition = AutocompleteCombobox(frame_ammunition_middle, textvariable=value_ammunition_type)
        a_c_transaction_ammunition.set_completion_list(get_ammunition_type())
        a_c_transaction_ammunition.config(width=max([sum([len(str(q)) for q in i]) for i in get_ammunition_type()]) + 2)
        a_c_transaction_ammunition.grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_ammunition_quantity = ttk.Label(frame_ammunition_middle, text="Aantal:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="E")
        value_ammunition_quantity = tk.IntVar(frame_ammunition_middle)
        entry_ammunition_quantity = ttk.Entry(frame_ammunition_middle,
                                              textvariable=value_ammunition_quantity,
                                              width=3).grid(row=0, column=3, padx=5, pady=5, sticky="W")

        label_ammunition_valuation = ttk.Label(frame_ammunition_middle, text="Totaal (EUR):") \
            .grid(row=1, column=2, padx=5, pady=2, sticky="W")
        total_price_left = tk.DoubleVar()
        total_price_left.set(0.0)
        label_ammunition_total = ttk.Label(frame_ammunition_middle, textvariable=total_price_left) \
            .grid(row=1, column=3, padx=5, pady=2, sticky="W")

        def clicked_submit_left():
            if input_validation.is_int(int(value_ammunition_quantity.get())) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide munitie waarde in")
            else:
                ammunition_stock = database_manager.execute_sql(
                    '''SELECT stock FROM ammunition WHERE type = ?''', (value_ammunition_type.get(),))
                new_ammunition_stock = ammunition_stock[0][0] - value_ammunition_quantity.get()

                if new_ammunition_stock < 0:
                    messagebox.showinfo(title="Error",
                                        message="Er is niet genoeg voorraad om zo veel te verkopen er is slechts " +
                                                str(ammunition_stock[0][0]) + " over en u probeert " +
                                                str(value_ammunition_quantity.get()) + " te verkopen")

                else:
                    database_manager.execute_sql(
                        '''UPDATE ammunition SET stock = ? WHERE type = ?''',
                        (new_ammunition_stock, value_ammunition_type.get(),))

                    ammunition_price = database_manager.execute_sql(
                        '''SELECT price FROM ammunition WHERE type = ?''', (value_ammunition_type.get(),))

                    result_submit_left = database_manager.execute_sql(
                        '''INSERT INTO sale_ammunition (date, quantity, type, seller, buyer, price)
                         VALUES (?, ?, ?, ?, ?, ?)''', (
                            date.today(),
                            value_ammunition_quantity.get(),
                            value_ammunition_type.get(),
                            user_session,
                            value_user_middle.get()[-6:],
                            round(value_ammunition_quantity.get() * ammunition_price[0][0], 2)
                        ))

                    if result_submit_left:
                        messagebox.showinfo(title="Information",
                                            message="Het systeem heeft met succes munitie verkocht er is nu " +
                                                    str(new_ammunition_stock) + " voorraad van " +
                                                    value_ammunition_type.get() + " over")

                        user_data = database_manager.execute_sql(
                            '''SELECT email_address, first_name FROM user WHERE knsa_licence_number = ?''',
                            (value_user_middle.get()[-6:],))

                        email_body = 'Hallo ' + user_data[0][1] + \
                                     ', \n\n U heeft een transactie afgerond bij de scheitvereniging op ' \
                                     + str(date.today()) + \
                                     '. \n\n U heeft ' + str(value_ammunition_quantity.get()) + ' van ' + \
                                     value_ammunition_type.get() + \
                                     ' gekocht voor een prijs van totaal €' + \
                                     str(round(value_ammunition_quantity.get() * ammunition_price[0][0], 2)) + \
                                     '\n\n reageer aub niet op deze email. \n\n Fijne dag!'

                        email_result = email_manager.send_email(user_data[0][0],
                                                                'U heeft munitie gekocht op de schietvereniging',
                                                                email_body)

                        if email_result:
                            clicked_reset()
                        else:
                            messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")

                    else:
                        messagebox.showerror(title="Error",
                                             message="Er was een fout bij het verkopen van de munitie")

        def clicked_reset_left():
            value_ammunition_quantity.set(0)
            total_price_left.set(0.0)
            value_ammunition_type.set('Select')

        def clicked_total_left():
            if input_validation.is_int(value_ammunition_quantity.get()) is False or \
                    value_ammunition_type.get() not in get_ammunition_type():
                return 0
            else:
                ammunition_quantity = value_ammunition_quantity.get()

                ammunition_price = database_manager.execute_sql(
                    '''SELECT price FROM ammunition WHERE type = ?''', (value_ammunition_type.get(),))

                total_ammunition_price = round(ammunition_quantity * ammunition_price[0][0], 2)

                total_price_left.set(total_ammunition_price)

                return total_ammunition_price

        # scorecard sales starts here
        fields = {
            'Standaard': 'regular',
            'Competitie': 'competition'
        }

        label_frame_top_right = tk.Frame(frame_inner_top)
        label_frame_top_right.pack(side="right", fill="both", expand=True)

        frame_scorecard_top = tk.Frame(label_frame_top_right)
        frame_scorecard_top.pack(side="top", anchor="nw")

        frame_scorecard_middle = tk.Frame(label_frame_top_right)
        frame_scorecard_middle.pack(anchor="nw")

        label_scorecard_regular = ttk.Label(frame_scorecard_middle, text="Aantal Standaard Kaarten:") \
            .grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_scorecard_regular_quantity = tk.IntVar(frame_scorecard_middle)
        entry_scorecard_regular_quantity = ttk.Entry(frame_scorecard_middle,
                                                     textvariable=value_scorecard_regular_quantity,
                                                     width=3).grid(row=0, column=1, padx=5, pady=5, sticky="W")

        label_scorecard_competition = ttk.Label(frame_scorecard_middle, text="Competitie Kaarten:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="W")
        value_scorecard_competition = tk.IntVar(frame_scorecard_middle)
        value_scorecard_competition.set(0)
        checkbutton_scorecard_competition = ttk.Checkbutton(frame_scorecard_middle,
                                                            variable=value_scorecard_competition) \
            .grid(row=0, column=3, padx=5, pady=2, sticky="W")

        label_scorecard_valuation = ttk.Label(frame_scorecard_middle, text="Totaal (EUR):") \
            .grid(row=2, column=2, padx=5, pady=2, sticky="E")
        total_price_right = tk.DoubleVar()
        total_price_right.set(0.0)
        label_scorecard_total = ttk.Label(frame_scorecard_middle, textvariable=total_price_right) \
            .grid(row=2, column=3, padx=5, pady=2, sticky="W")

        def clicked_submit_right():
            if input_validation.is_int(int(value_scorecard_regular_quantity.get())) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide scorecard waarde in")
            else:
                if value_scorecard_competition.get() == 1:
                    value_scorecard_competition_quantity = 2
                    scorecard_stock_competition = database_manager.execute_sql(
                        '''SELECT stock FROM scorecard WHERE type = ?''', ('competition',))

                    if scorecard_stock_competition[0][0] - value_scorecard_competition_quantity < 0:
                        messagebox.showinfo(title="Error",
                                            message="Er is niet genoeg voorraad om zo veel te verkopen er is slechts " +
                                                    str(scorecard_stock_competition[0][0] -
                                                        value_scorecard_competition_quantity) +
                                                    " over en u probeert 2 te verkopen")
                else:
                    value_scorecard_competition_quantity = 0

                scorecard_stock_regular = database_manager.execute_sql(
                    '''SELECT stock FROM scorecard WHERE type = ?''', ('regular',))

                if scorecard_stock_regular[0][0] - value_scorecard_regular_quantity.get() < 0:
                    messagebox.showinfo(title="Error",
                                        message="Er is niet genoeg voorraad om zo veel te verkopen er is slechts " +
                                                str(scorecard_stock_regular[0][0]) + " over en u probeert " +
                                                str(value_scorecard_regular_quantity.get()) + " te verkopen")
                else:
                    scorecard_price = database_manager.execute_sql('''SELECT price FROM scorecard;''')

                    if value_scorecard_competition.get() == 1:
                        database_manager.execute_sql(
                            '''UPDATE scorecard SET stock = ? WHERE type = ?''',
                            (scorecard_stock_competition[0][0] - value_scorecard_competition_quantity, 'competition',))

                    database_manager.execute_sql(
                        '''UPDATE scorecard SET stock = ? WHERE type = ?''', (scorecard_stock_regular[0][0] -
                                                                              value_scorecard_regular_quantity.get(),
                                                                              'regular',))

                    result_submit_competition = 'success'
                    result_submit_regular = 'success'

                    if value_scorecard_competition.get() == 1:
                        result_submit_competition = database_manager.execute_sql(
                            '''INSERT INTO sale_scorecard (date, quantity, type, seller, buyer, price) 
                            VALUES (?, ?, ?, ?, ?, ?)''',
                            (date.today(),
                             value_scorecard_competition_quantity,
                             'competition',
                             user_session,
                             value_user_middle.get()[-6:],
                             round(value_scorecard_competition_quantity * scorecard_price[1][0], 2)))

                    if value_scorecard_regular_quantity.get() > 0:
                        result_submit_regular = database_manager.execute_sql(
                            '''INSERT INTO sale_scorecard (date, quantity, type, seller, buyer, price) 
                            VALUES (?, ?, ?, ?, ?, ?)''',
                            (date.today(),
                             value_scorecard_regular_quantity.get(),
                             'regular',
                             user_session,
                             value_user_middle.get()[-6:],
                             round(value_scorecard_regular_quantity.get() * scorecard_price[0][0], 2)))

                    if result_submit_competition and result_submit_regular:
                        messagebox.showinfo(title="Information",
                                            message="Het systeem heeft met succes scorecard verkocht u heeft nu " +
                                                    str(scorecard_stock_regular[0][0] -
                                                        value_scorecard_regular_quantity.get()) +
                                                    " voorraad van standaard over en "
                                                    + str(scorecard_stock_competition[0][0] -
                                                          value_scorecard_competition_quantity) +
                                                    " van competitie over.")

                        user_data = database_manager.execute_sql(
                            '''SELECT email_address, first_name FROM user WHERE knsa_licence_number = ?''',
                            (value_user_middle.get()[-6:],))

                        email_body = 'Hallo ' + user_data[0][1] + \
                                     ', \n\n U heeft een transactie voor score kaarten ' \
                                     'afgerond bij de scheitvereniging op ' \
                                     + str(date.today()) + ' u totaal bedrag was €' + \
                                     str(round(value_scorecard_regular_quantity.get() * scorecard_price[0][0], 2)
                                         + round(value_scorecard_competition_quantity * scorecard_price[1][0], 2))

                        email_result = email_manager.send_email(user_data[0][0],
                                                                'U heeft score kaarten gekocht op de schietvereniging',
                                                                email_body)

                        if email_result:
                            clicked_reset()
                        else:
                            messagebox.showerror(title="Error", message="Er was een fout met stuuren van de email")

                    else:
                        messagebox.showerror(title="Error",
                                             message="Er was een fout bij het verkopen van de scorecard")

        def clicked_reset_right():
            value_scorecard_regular_quantity.set(0)
            total_price_right.set(0.0)
            value_scorecard_competition.set(0)

        def clicked_total_right():
            if input_validation.is_int(value_scorecard_regular_quantity.get()) is False:
                regular_scorecard_quantity = 0
            else:
                regular_scorecard_quantity = value_scorecard_regular_quantity.get()

            if value_scorecard_competition.get() == 1:
                value_scorecard_competition_quantity = 2

                scorecard_price_competition = database_manager.execute_sql(
                    '''SELECT price FROM scorecard WHERE type = ?''', ('competition',))

                total_scorecard_price_competition = round(value_scorecard_competition_quantity *
                                                          scorecard_price_competition[0][0], 2)
            else:
                value_scorecard_competition_quantity = 0
                total_scorecard_price_competition = 0

            scorecard_price_regular = database_manager.execute_sql(
                '''SELECT price FROM scorecard WHERE type = ?''', ('regular',))

            total_price_right.set(round(round(regular_scorecard_quantity * scorecard_price_regular[0][0],
                                              2) + total_scorecard_price_competition, 2))

            return round(round(regular_scorecard_quantity * scorecard_price_regular[0][0],
                               2) + total_scorecard_price_competition, 2)

        frame_bottom_left = tk.Frame(frame_inner_bottom)
        frame_bottom_left.pack(side="left")

        label_user_middle = ttk.Label(frame_bottom_left, text="Lid:") \
            .grid(row=0, column=0, padx=5, pady=5, sticky="W")
        value_user_middle = tk.StringVar(frame_bottom_left)
        value_user_middle.set("Select")
        a_c_transaction_user = AutocompleteCombobox(frame_bottom_left, textvariable=value_user_middle)
        a_c_transaction_user.set_completion_list(get_user_data())
        a_c_transaction_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
        a_c_transaction_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

        label_middle_price = ttk.Label(frame_bottom_left, text="Totaal (EUR):") \
            .grid(row=1, column=0, padx=5, pady=5, sticky="W")
        total_price = tk.DoubleVar(frame_inner_bottom)
        total_price.set(0.0)
        label_total_price = ttk.Label(frame_bottom_left, textvariable=total_price) \
            .grid(row=1, column=1, padx=5, pady=5, sticky="W")

        frame_bottom_right = tk.Frame(frame_inner_bottom)
        frame_bottom_right.pack(side="bottom")

        def clicked_submit():
            if value_user_middle.get() not in get_user_data():
                messagebox.showerror(title="Error",
                                     message="Vul aub een lid in voor dat je verder gaat met verkopen")
            else:
                if value_ammunition_quantity.get() > 0:
                    clicked_submit_left()
                if value_scorecard_competition.get() == 1 or value_scorecard_regular_quantity.get() > 0:
                    clicked_submit_right()

        button_middle_submit = ttk.Button(frame_bottom_right, text="Verkopen", command=lambda: clicked_submit()) \
            .grid(row=0, column=0, padx=10, pady=15)

        def clicked_reset():
            clicked_reset_left()
            clicked_reset_right()
            total_price.set(0.0)
            value_user_middle.set('Select')

        button_middle_reset = ttk.Button(frame_bottom_right, text="Reset", command=lambda: clicked_reset()) \
            .grid(row=0, column=1, padx=10, pady=15)

        def clicked_total():
            total_price.set(round(clicked_total_left() + clicked_total_right(), 2))

        button_middle_total = ttk.Button(frame_bottom_right, text="Reken Totaal", command=lambda: clicked_total()) \
            .grid(row=0, column=2, padx=10, pady=15)

        label_frame_bottom = tk.LabelFrame(frame_right, text="View Transactions")
        label_frame_bottom.pack(side="right", fill="x", expand=True)

        frame_menu = tk.Frame(label_frame_bottom)
        frame_menu.pack(side="bottom", fill="x")

        label_user_matplot = ttk.Label(frame_menu, text="Lid:").grid(row=0, column=0, padx=5, pady=2, sticky="W")
        value_user_matplot = tk.StringVar(frame_menu)
        value_user_matplot.set("Select")
        a_c_matplot_transaction_user = AutocompleteCombobox(frame_menu, textvariable=value_user_matplot)
        a_c_matplot_transaction_user.set_completion_list(get_user_data())
        a_c_matplot_transaction_user.config(width=max([sum([len(str(q)) for q in i]) for i in get_user_data()]) - 3)
        a_c_matplot_transaction_user.grid(row=0, column=1, padx=5, pady=2, sticky="W")

        fields2 = {
            'Standaard': 'regular',
            'Competitie': 'competition',
        }

        label_scorecard_matplot = ttk.Label(frame_menu, text="Scorekaart:") \
            .grid(row=0, column=2, padx=5, pady=2, sticky="W")
        value_scorecard_matplot = tk.StringVar(frame_menu)
        value_scorecard_matplot.set("Select")
        a_c_matplot_transaction_scorecard = AutocompleteCombobox(frame_menu, textvariable=value_scorecard_matplot)
        a_c_matplot_transaction_scorecard.set_completion_list(fields2.keys())
        a_c_matplot_transaction_scorecard.config(width=max([sum([len(str(q)) for q in i]) for i in fields2.keys()]))
        a_c_matplot_transaction_scorecard.grid(row=0, column=3, padx=5, pady=2, sticky="W")

        label_ammunition_matplot = ttk.Label(frame_menu, text="Munitie:") \
            .grid(row=1, column=2, padx=5, pady=2, sticky="W")
        value_ammunition_matplot = tk.StringVar(frame_menu)
        value_ammunition_matplot.set("Select")
        a_c_matplot_transaction_ammunition = AutocompleteCombobox(frame_menu, textvariable=value_ammunition_matplot)
        a_c_matplot_transaction_ammunition.set_completion_list(get_ammunition_type())
        a_c_matplot_transaction_ammunition.config(
            width=max([sum([len(str(q)) for q in i]) for i in get_ammunition_type()]) + 2)
        a_c_matplot_transaction_ammunition.grid(row=1, column=3, padx=5, pady=2, sticky="W")

        label_date_from_matplot = ttk.Label(frame_menu, text="Datum van (DD-MM-YYYY):") \
            .grid(row=0, column=4, padx=5, pady=2, sticky="W")
        value_date_from_matplot = tk.StringVar(frame_menu)
        entry_date_from_matplot = ttk.Entry(frame_menu, textvariable=value_date_from_matplot, width=10) \
            .grid(row=0, column=5, padx=5, pady=2, sticky="W")

        label_date_to_matplot = ttk.Label(frame_menu, text="Datum tot (DD-MM-YYYY):") \
            .grid(row=1, column=4, padx=5, pady=2, sticky="W")
        value_date_to_matplot = tk.StringVar(frame_menu)
        entry_date_to_matplot = ttk.Entry(frame_menu, textvariable=value_date_to_matplot, width=10) \
            .grid(row=1, column=5, padx=5, pady=2, sticky="W")

        def clicked_show():
            if input_validation.is_date(input_validation.convert_input_date(
                    value_date_from_matplot.get())) is False and \
                    input_validation.is_date(input_validation.convert_input_date(value_date_to_matplot.get())) is False:
                messagebox.showerror(title="Error", message="Vul aub een valide datum in")
                value_date_from_matplot.set('')
                value_date_to_matplot.set('')
            else:
                print('Clicked')

        button_show = ttk.Button(frame_menu, text="Laden", command=lambda: clicked_show()) \
            .grid(row=0, column=6, padx=5, pady=2, sticky="W")

        def clicked_reset_matplot():
            value_user_matplot.set('Select')
            value_scorecard_matplot.set('Select')
            value_ammunition_matplot.set('Select')
            value_date_from_matplot.set('')
            value_date_to_matplot.set('')

        button_reser_matplot = ttk.Button(frame_menu, text="Reset", command=lambda: clicked_reset_matplot()) \
            .grid(row=1, column=6, padx=5, pady=2, sticky="W")

        # matplotlib graph starts here
        frame_matplot = tk.Frame(label_frame_bottom)
        frame_matplot.pack(side="top", fill="both")

        canvas = FigureCanvasTkAgg(f, frame_matplot)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


class AutocompleteCombobox(ttk.Combobox):

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list  # Setup our popup menu

    def autocomplete(self, delta=0):
        if delta:  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):  # Match case insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
        if event.keysym == "Left":
            if self.position < self.index(tk.END):  # delete the selection
                self.delete(self.position, tk.END)
            else:
                self.position = self.position - 1  # delete one character
                self.delete(self.position, tk.END)
        if event.keysym == "Right":
            self.position = self.index(tk.END)  # go to end (no selection)
        if len(event.keysym) == 1:
            self.autocomplete()
        # list at the position of the autocompletion


app2 = LoginPage()
app2.geometry("285x120")
app2.minsize(285, 120)
app2.maxsize(285, 120)
app2.mainloop()

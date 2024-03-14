import main
from variables import *
import customer_menu
import empoyee_menu
import manager_menu
import validations
import save


def create_account(role):
    name = input("Unesite ime i prezime: ")
    while True:
        username = input("Unesite korisničko ime: ")
        if validations.validation_username(username):
            break
        continue_search()
    while True:
        password = input("Unesite šifru: ")
        if validations.validation_password(password):
            break
        continue_search()
    all_users.append([username, password, name.title(), role])
    print("NALOG USPEŠNO NAPRAVLJEN!!!")


def login():
    username = input("Unesite korisničko ime: ")
    logged_user.append(username)
    password = input("Unesite šifru: ")
    logged_user.append(password)
    for user in all_users:
        if username == user[0] and password == user[1]:
            role = validations.check_role(username)
            if role == "Kupac":
                logged_user.append("Kupac")
                print("Prijavljeni ste kao KUPAC!")
                customer_menu.login_customer()
            elif role == "Prodavac":
                logged_user.append("Prodavac")
                print("Prijavljeni ste kao PRODAVAC!")
                empoyee_menu.login_employee()
            elif role == "Menadzer":
                logged_user.append("Menadzer")
                print("Prijavljeni ste kao MENADŽER!")
                manager_menu.login_manager()
    else:
        print("NEUSPEŠNA PRIJAVA! Proverite podatke ili napravite nalog!")
        logged_user.clear()
        main.start_point()


def logout():
    save.save_data()
    logged_user.clear()
    print("ODJAVILI STE SE!!!")
    main.start_point()


def data_change():
    while True:
        print("OPCIJE ZA PROMENU PODATAKA")
        print("Korisničko ime NE MOŽE da se menja!!!\n[1] Ime i prezime\n[2] Lozinka\n[x] Povratak")
        change = input("Odaberite stavku: ")
        if change == "1":
            change_name()
        elif change == "2":
            change_password()
        elif change.lower() == "x":
            break
        else:
            print("Unos nije odgovarajuć!!!")


def change_name():
    while True:
        username = logged_user[0]
        new_name = input("Unesite novo ime i prezime: ")
        for user in all_users:
            if user[0] == username:
                user[2] = new_name.title()
                print("IME I PREZIME USPEŠNO PROMENJENO!!!")
        break


def change_password():
    while True:
        username = logged_user[0]
        new_password = input("Unesite novu lozinku: ")
        if validations.validation_password(new_password):
            for user in all_users:
                if user[0] == username:
                    user[1] = new_password
                    print("LOZINKA USPEŠNO PROMENJENA!!!")
            break
        continue_search()


def loyalty_card(client_name, ticket_price):
    total_spending = 0
    for ticket in sold_tickets.values():
        if ticket["client"] == client_name:
            total_spending += float(ticket["ticket price"])
    if total_spending >= 5000:
        ticket_price = ticket_price - 0.1 * ticket_price
        print("KORISNIK OSTVARUJE POPUST 10% NA KARTICU LOJALNOSTI!")
    return ticket_price


def continue_search():
    print("[0] Ponovni unos\n[x] Povratak")
    while True:
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            break
        elif choice.lower() == "x":
            back_to_profile()
        else:
            print("Unesite odgovarajuću opciju!!!")


def back_to_profile():
    if len(logged_user) == 0:
        main.start_point()
    else:
        role = logged_user[2]
        if role == "Kupac":
            customer_menu.login_customer()
        elif role == "Prodavac":
            empoyee_menu.login_employee()
        elif role == "Menadzer":
            manager_menu.login_manager()

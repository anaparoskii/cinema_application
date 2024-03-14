from tabulate import tabulate
import datetime
from variables import *
import save
import validations
import user_functions
import screenings_functions


def report_a():
    while True:
        value = input("Unesite datum za koji želite da vidite prodate karte: ")
        if validations.validation_date(value):
            break
        user_functions.continue_search()
    for ticket in sold_tickets.values():
        if ticket["date sold"] == value:
            report.append([ticket["screening code"],
                           ticket["seat"],
                           ticket["client"],
                           ticket["date sold"],
                           ticket["sold by"],
                           ticket["ticket price"]])
    header = ["ŠIFRA PROJEKCIJE", "SEDIŠTE", "KUPAC", "DATUM PRODAJE", "PRODAVAC", "CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nijedna karta nije prodata taj dan!!!")
    reports_function("a")


def report_b():
    screenings_functions.show_repertoire()
    while True:
        value = input("Unesite šifru termina: ")
        if validations.validation_screening_code(value):
            break
        user_functions.continue_search()
    for ticket in sold_tickets.values():
        if ticket["screening code"] == value:
            report.append([ticket["screening code"],
                           ticket["seat"],
                           ticket["client"],
                           ticket["date sold"],
                           ticket["sold by"],
                           ticket["ticket price"]])
    header = ["ŠIFRA PROJEKCIJE", "SEDIŠTE", "KUPAC", "DATUM PRODAJE", "PRODAVAC", "CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nije prodata nijedna karta za ovaj termin!!!")
    reports_function("b")


def report_c():
    while True:
        date = input("Unesite datum za koji želite da vidite prodate karte: ")
        if validations.validation_date(date):
            break
        user_functions.continue_search()
    while True:
        name = input("Unesite ime prodavca: ")
        if validations.validation_employee(name):
            break
        user_functions.continue_search()
    for ticket in sold_tickets.values():
        if ticket["date sold"] == date and ticket["sold by"] == name:
            report.append([ticket["screening code"],
                           ticket["seat"],
                           ticket["client"],
                           ticket["date sold"],
                           ticket["sold by"],
                           ticket["ticket price"]])
    header = ["ŠIFRA PROJEKCIJE", "SEDIŠTE", "KUPAC", "DATUM PRODAJE", "PRODAVAC", "CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Odabrani radnik nije prodao nijednu kartu taj dan!!!")
    reports_function("c")


def report_d():
    summary = 0
    while True:
        day = input("Unesite željeni dan: ")
        if validations.validation_days(day):
            break
        user_functions.continue_search()
    for ticket in sold_tickets.values():
        if datetime.datetime.strptime(ticket["date sold"], '%d.%m.%Y.').weekday() == constants[day.lower()]:
            help_list.append([ticket["ticket price"]])
            summary += float(ticket["ticket price"])
    report.append([day, len(help_list), summary])
    header = ["DAN", "BROJ PRODATIH KARATA", "UKUPNA CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nijedna karta nije prodata na ovaj dan!!!")
    reports_function("d")


def report_e():
    summary = 0
    while True:
        for projection_key in projections.keys():
            print(projection_key)
        code = input("Unesite željenu projekciju: ")
        if validations.validation_screening_code(code):
            break
        user_functions.continue_search()
    print("Dani kada se prikazuje odabrana projekcija: ")
    for projection in projections.values():
        if projection["code"] == code:
            print(projection["days"])
    while True:
        day = input("Unesite željeni dan: ")
        if validations.validation_days(day):
            break
        user_functions.continue_search()
    for screening in screenings.values():
        if screening["code"][0:4] == code:
            if datetime.datetime.strptime(screening["date"], '%d.%m.%Y.').weekday() == constants[day.lower()]:
                screening_code = screening["code"]
                for ticket in sold_tickets.values():
                    if ticket["screening code"] == screening_code:
                        help_list.append([ticket["ticket price"]])
                        summary += float(ticket["ticket price"])
    report.append([code, projections[code]["movie"], day, len(help_list), summary])
    header = ["PROJEKCIJA", "FILM", "DAN ODRŽAVANJA", "BROJ PRODATIH KARATA", "UKUPNA CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nije prodata nijedna karta za taj termin!!!")
    reports_function("e")


def report_f():
    summary = 0
    while True:
        movie_name = input("Unesite ime željenog filma: ")
        if validations.check_movie(movie_name):
            break
        user_functions.continue_search()
    for projection in projections.values():
        if movie_name.lower() in projection["movie"].lower():
            code = projection["code"]
            for ticket in sold_tickets.values():
                if code in ticket["screening code"]:
                    help_list.append([ticket["ticket price"]])
                    summary += float(ticket["ticket price"])
    report.append([movie_name.title(), len(help_list), summary])
    header = ["FILM", "BROJ PRODATIH KARATA", "UKUPNA CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nije prodata nijedna karta za ovaj film!!!")
    reports_function("f")


def report_g():
    summary = 0
    while True:
        day = input("Unesite željeni dan: ")
        if validations.validation_days(day):
            break
        user_functions.continue_search()
    while True:
        seller = input("Unesite ime prodavca: ")
        if validations.validation_employee(seller):
            break
        user_functions.continue_search()
    for ticket in sold_tickets.values():
        if datetime.datetime.strptime(ticket["date sold"], '%d.%m.%Y.').weekday() == constants[day.lower()]\
                and seller.lower() in ticket["sold by"].lower():
            help_list.append([ticket["ticket price"]])
            summary += float(ticket["ticket price"])
    report.append([day, seller, len(help_list), summary])
    header = ["DAN", "PRODAVAC", "BROJ PRODATIH KARATA", "UKUPNA CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Ovaj prodavac nije prodao nijednu kartu na izabran dan!!!")
    reports_function("g")


def report_h():
    for user in all_users:
        if user[3] != "Kupac":
            seller = user[0]
            summary = 0
            for ticket in sold_tickets.values():
                date = validations.split_date(ticket["date sold"])
                today = datetime.datetime.today()
                if ticket["sold by"] == seller and today - date < datetime.timedelta(days=30):
                    help_list.append([ticket["ticket price"]])
                    summary += float(ticket["ticket price"])
            report.append([seller, len(help_list), summary])
            help_list.clear()
    header = ["PRODAVAC", "BROJ PRODATIH KARATA", "UKUPNA CENA"]
    print(tabulate(report, header, tablefmt="pretty"))
    if len(report) == 0:
        print("Nije bilo prodatih karata u poslednjih 30 dana!!!")
    reports_function("h")


def reports_function(letter):
    help_list.clear()
    while True:
        print("[0] Sačuvaj izveštaj\n[x] Nazad")
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            save.save_reports(letter)
            print("IZVEŠTAJ SAČUVAN!")
            break
        elif choice.lower() == "x":
            break
        else:
            print("Unesite odgovarajuću opciju!!!")

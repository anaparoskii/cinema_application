from tabulate import tabulate
import datetime
from variables import *
import seating
import user_functions
import validations
import screenings_functions
import save


def sell_reservation():
    print("PRODAJA KARTE")
    show_all_tickets("rezervisana")
    while True:
        choice = input("Unesite broj rezervacije: ")
        for ticket_key, ticket in tickets.items():
            if choice.isnumeric() and int(choice) == int(ticket["ticket key"]):
                seat = ticket["seat"]
                client = ticket["client"]
                screening = ticket["screening code"]
                ticket["date sold"] = datetime.datetime.today().strftime('%d.%m.%Y.')
                ticket["status"] = "prodata"
                print("USPEŠNA PRODAJA!!!")
                save_sell(seat, client, screening)
                tickets_function()
        else:
            print("Neispravan unos!!!")


def save_sell(seat, client, screening):
    all_keys = []
    if len(sold_tickets) == 0:
        key = 1000
    else:
        for keys in sold_tickets.keys():
            all_keys.append(int(keys))
        key = max(all_keys) + 1
    date_sold = datetime.datetime.today().strftime('%d.%m.%Y.')
    price = user_functions.loyalty_card(client, repertoire[screening]["ticket price"])
    seller = logged_user[0]
    sold_tickets[key] = {"ticket key": key,
                         "seat": seat,
                         "client": client,
                         "screening code": screening,
                         "date sold": date_sold,
                         "ticket price": price,
                         "sold by": seller}
    save.save_data()


def reserve_or_direct_sell(status):
    screenings_functions.show_repertoire()
    all_keys = []
    if status == "rezervisana":
        print("REZERVACIJA KARTE")
    else:
        print("PRODAJA KARTE")
    if len(tickets) == 0:
        key = 1000
    else:
        for keys in tickets.keys():
            all_keys.append(int(keys))
        key = max(all_keys) + 1
    while True:
        code = input("Unesite šifru termina za koji rezervišete: ")
        if code in screenings.keys():
            break
        print("Netačan unos!")
        user_functions.continue_search()
    print(tabulate([seats for seats in hall_seats[code]], tablefmt="grid"))
    while True:
        seat = input("Unesite sedište: ")
        if seat == "XX":
            print("ZAUZETO SEDIŠTE!")
            user_functions.continue_search()
        elif validations.validation_seat(code, seat):
            break
    if logged_user[2] != "Kupac":
        ticket_buyer = input("Unesite ime i prezime kupca: ")
    else:
        ticket_buyer = logged_user[0]
    seating.new_taken_seat(code, seat)
    date = datetime.datetime.today().strftime("%d.%m.%Y.")
    tickets[key] = {"ticket key": key,
                    "seat": seat,
                    "client": ticket_buyer,
                    "screening code": code,
                    "date sold": date,
                    "status": status}
    if status == "rezervisana":
        print("USPEŠNA REZERVACIJA!!!")
    else:
        print("USPEŠNA PRODAJA!!!")
        save_sell(seat, ticket_buyer, code)
    tickets_function()


def tickets_function():
    print("[0] Nastavi proces\n[x] Nazad")
    while True:
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            if logged_user[2] == "Kupac":
                reserve_or_direct_sell("rezervisana")
            else:
                while True:
                    print("[1] Prodaj REZERVISANU kartu\n[2] DIREKTNA prodaja\n[x] Nazad")
                    choice2 = input("Unesite željenu stavku: ")
                    if choice2 == "1":
                        sell_reservation()
                    elif choice2 == "2":
                        reserve_or_direct_sell("prodata")
                    elif choice2 == "x":
                        break
                    else:
                        print("Unesite odgovarajuću opciju")
        elif choice.lower() == "x":
            save.save_data()
            user_functions.back_to_profile()
        else:
            print("Unesite odgovarajuću stavku")


def show_my_reservations(name):
    print("MOJE REZERVACIJE")
    for value in tickets.values():
        if value["client"] == name and value["status"] == "rezervisana":
            code = value["screening code"]
            date = screenings[code]["date"]
            start_time = projections[code[0:4]]["start time"]
            end_time = projections[code[0:4]]["end time"]
            hall = projections[code[0:4]]["hall"]
            display_tickets.append([value["ticket key"],
                                    value["seat"],
                                    value["client"],
                                    value["screening code"],
                                    hall,
                                    start_time,
                                    end_time,
                                    date])
    header = ["BR.", "SEDIŠTE", "IME", "ŠIFRA", "SALA", "POČETAK", "KRAJ", "DATUM PRIKAZIVANJA"]
    print(tabulate(display_tickets, header, tablefmt="pretty"))
    if len(display_tickets) == 0:
        print("Ne postoje aktivne rezervacije!!!")
    display_tickets.clear()


def show_all_tickets(status):
    for value in tickets.values():
        if value["status"] == status:
            code = value["screening code"]
            date = screenings[code]["date"]
            start_time = projections[code[0:4]]["start time"]
            end_time = projections[code[0:4]]["end time"]
            hall = projections[code[0:4]]["hall"]
            display_tickets.append([value["ticket key"],
                                    value["seat"],
                                    value["client"],
                                    value["screening code"],
                                    hall,
                                    start_time,
                                    end_time,
                                    date,
                                    value["status"]])
        elif status == "all":
            code = value["screening code"]
            date = screenings[code]["date"]
            start_time = projections[code[0:4]]["start time"]
            end_time = projections[code[0:4]]["end time"]
            hall = projections[code[0:4]]["hall"]
            display_tickets.append([value["ticket key"],
                                    value["seat"],
                                    value["client"],
                                    value["screening code"],
                                    hall,
                                    start_time,
                                    end_time,
                                    date,
                                    value["status"]])
    header = ["BR.", "SEDIŠTE", "IME", "ŠIFRA", "SALA", "POČETAK", "KRAJ", "DATUM PRIKAZIVANJA", "STATUS"]
    print(tabulate(display_tickets, header, tablefmt="pretty"))
    display_tickets.clear()


def delete_reservations():
    print("PONIŠTAVANJE REZERVACIJE")
    while True:
        current_key = input("Unesite broj rezervacije koju poništavate: ")
        if validations.validation_ticket_key(current_key):
            break
        user_functions.continue_search()
    screening_seat = tickets[str(current_key)]["seat"]
    for row in hall_seats[tickets[str(current_key)]["screening code"]]:
        for i in range(len(row)):
            if str(row[0])[1:2] == screening_seat[1:2]:
                row[ord(screening_seat[0:1]) - 65] = screening_seat
                break
    del tickets[str(current_key)]
    print("REZERVACIJA USPEŠNO PONIŠTENA!")
    save.save_data()
    set_ticket_cancellation()


def delete_ticket():
    print("PONIŠTAVANJE KARTE")
    while True:
        current_key = input("Unesite broj karte koju poništavate: ")
        if validations.validation_ticket_key(current_key):
            break
        user_functions.continue_search()
    screening_seat = tickets[current_key]["seat"]
    screening_code = tickets[current_key]["screening code"]
    for row in hall_seats[tickets[current_key]["screening code"]]:
        for i in range(len(row)):
            if str(row[0])[1:2] == screening_seat[1:2]:
                row[ord(screening_seat[0:1]) - 65] = screening_seat
                break
    for ticket_key, sold_ticket in list(sold_tickets.items()):
        if sold_ticket["seat"] == screening_seat and sold_ticket["screening code"] == screening_code:
            del sold_tickets[ticket_key]
            break
    del tickets[current_key]
    print("KARTA USPEŠNO PONIŠTENA!")
    save.save_data()
    set_ticket_cancellation()


def set_ticket_cancellation():
    print("[0] Nastavi poništavanje\n[x] Nazad")
    while True:
        choice = input("Unesite odgovarajuću stavku: ")
        if choice == "0":
            while True:
                print("[1] Poništi rezervaciju\n[2] Poništi kartu\n[x] Nazad")
                choice0 = input("Unesite željenu stavku: ")
                if choice0 == "1":
                    delete_reservations()
                elif choice0 == "2":
                    delete_ticket()
                elif choice0.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!!!")
        elif choice.lower() == "x":
            break
        else:
            print("Unesite odgovarajuću stavku!!!")


def cancel_reservations():
    show_all_tickets("rezervisana")
    while True:
        screening_code = input("Unesite šifru projekcije: ")
        if validations.validation_screening_code(screening_code):
            if validations.validation_reserved_screening(screening_code):
                if validations.validation_start_time(screening_code):
                    break
        user_functions.continue_search()
    for ticket_key, ticket in list(tickets.items()):
        if ticket["screening code"] == screening_code and ticket["status"] == "rezervisana":
            del tickets[ticket_key]
    print("PONIŠTENE REZERVACIJE!")


def edit_ticket():
    print("IZMENA KARTE")
    show_all_tickets("all")
    while True:
        old_client = input("Unesite ime kupca: ")
        if validations.validation_client(old_client):
            break
        user_functions.continue_search()
    while True:
        old_screening = input("Unesite termin projekcije: ")
        if validations.validation_screening_code(old_screening):
            if validations.validation_client_screening(old_client, old_screening):
                break
        user_functions.continue_search()
    while True:
        old_seat = input("Unesite sedište: ")
        if validations.validation_client_screening_seat(old_client, old_screening, old_seat):
            break
        user_functions.continue_search()
    print("[1] Termin projekcije\n[2] Sedište\n[3] Ime kupca\n[x] Nazad")
    while True:
        change = input("Šta želite da izmenite? >> ")
        if change == "1":
            edit_ticket_screening(old_screening, old_seat)
            print("KARTA USPEŠNO IZMENJENA!")
            break
        elif change == "2":
            edit_ticket_seat(old_screening, old_seat)
            print("KARTA USPEŠNO IZMENJENA!")
            save.save_data()
            break
        elif change == "3":
            edit_ticket_client(old_screening, old_seat, old_client)
            print("KARTA USPEŠNO IZMENJENA!")
            save.save_data()
            break
        elif change.lower() == "x":
            break
        else:
            print("Unesite odgovarajuću opciju!!!")


def edit_ticket_screening(screening, seat):
    screenings_functions.show_repertoire()
    while True:
        new_screening = input("Unesite novi termin: ")
        if validations.validation_screening_code(new_screening):
            if screening[0:4] == new_screening[0:4]:
                break
            print("Nije termin odabrane bioskopske projekcije!!!")
            user_functions.continue_search()
        user_functions.continue_search()
    for ticket in tickets.values():
        if ticket["screening code"] == screening and ticket["seat"] == seat:
            ticket["screening code"] = new_screening
            if ticket["status"] == "prodata":
                for sold_ticket in sold_tickets.values():
                    if sold_ticket["screening code"] == screening and sold_ticket["seat"] == seat:
                        sold_ticket["screening code"] = new_screening
    edit_ticket_seat(new_screening, seat)


def edit_ticket_seat(screening, seat):
    print(tabulate([seats for seats in hall_seats[screening]], tablefmt="grid"))
    while True:
        new_seat = input("Unesite novo sedište: ")
        if new_seat == "XX":
            print("ZAUZETO SEDIŠTE!")
            user_functions.continue_search()
        elif validations.validation_seat(screening, new_seat):
            break
    for ticket in tickets.values():
        if ticket["screening code"] == screening and ticket["seat"] == seat:
            ticket["seat"] = new_seat
            if ticket["status"] == "prodata":
                for sold_ticket in sold_tickets.values():
                    if sold_ticket["screening code"] == screening and sold_ticket["seat"] == seat:
                        sold_ticket["seat"] = new_seat
    seating.new_taken_seat(screening, new_seat)
    seating.available_seat(screening, seat)


def edit_ticket_client(screening, seat, client):
    new_client = input("Unesite novo ime klijenta: ")
    for ticket in tickets.values():
        if ticket["screening code"] == screening and ticket["seat"] == seat and ticket["client"] == client:
            ticket["client"] = new_client
            if ticket["status"] == "prodata":
                for sold_ticket in sold_tickets.values():
                    if (sold_ticket["screening code"] == screening and sold_ticket["seat"] == seat
                            and sold_ticket["client"] == client):
                        sold_ticket["client"] = new_client

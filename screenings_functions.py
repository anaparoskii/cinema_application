from tabulate import tabulate
import datetime
from variables import *
import validations
import tickets_functions


def repertoire_function():
    print("[0] Rezervacija karte\n[x] Povratak")
    while True:
        choice = input("Unesite željenu stavku: ")
        if choice.lower() == "x":
            break
        elif choice == "0":
            if len(logged_user) == 0:
                print("Potrebna je registracija!!!")
            else:
                tickets_functions.reserve_or_direct_sell("rezervisana")
        else:
            print("Unesite odgovarajuću opciju!!!")


def show_repertoire():
    print("REPERTOAR")
    header = ["ŠIFRA", "DATUM", "FILM", "POČETAK", "KRAJ", "SALA", "CENA KARTE"]
    print(tabulate(repertoire_value, header, tablefmt="pretty"))


def delete_old_screenings():
    today_string = datetime.datetime.today().strftime('%d.%m.%Y.')
    today = validations.split_date(today_string)
    for screening_code, screening in screenings.items():
        date = validations.split_date(screening["date"])
        if date - today < datetime.timedelta(0):
            screenings[screening_code]["status"] = "invalid"


def generate_screenings():
    today = datetime.datetime.today().strftime('%d.%m.%Y.')
    start = validations.split_date(today)
    limit = start + datetime.timedelta(days=14)
    while start <= limit:
        day = start.strftime('%d.%m.%Y.')
        day_code = datetime.datetime.strptime(day, '%d.%m.%Y.').weekday()
        for projection in projections.values():
            weekdays = projection["days"].split(", ")
            for weekday in weekdays:
                if day_code == constants[weekday]:
                    screening_code = get_screening_letters(projection["code"])
                    if validation_existing_screening(screening_code, day):
                        screenings[screening_code] = {"code": screening_code,
                                                      "date": day,
                                                      "status": "valid"}
        start += datetime.timedelta(days=1)


def validation_existing_screening(screening_code, day):
    number = screening_code[0:4]
    for screening in list(screenings.values()):
        if (screening["date"] == day) and (number in screening["code"]) and (screening_code != screening["code"]):
            return False
    return True


def get_screening_letters(code):
    first_letter = ord("A")
    second_letter = ord("A")
    chosen_screening = []
    for screening in screenings.keys():
        if code in screening:
            chosen_screening.append(screening)
    first_letter += len(chosen_screening)//26
    if first_letter == ord("Z") + 1:
        first_letter = ord("A")
    second_letter += len(chosen_screening)
    if second_letter == ord("Z") + 1:
        second_letter = ord("A")
    screening_code = code + chr(first_letter) + chr(second_letter)
    return screening_code

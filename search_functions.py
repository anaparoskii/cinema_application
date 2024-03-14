from tabulate import tabulate
from variables import *
import user_functions
import validations
import tickets_functions


def search_tickets():
    print("PRETRAGA KARATA")
    while True:
        print("[1] Šifra projekcije\n[2] Ime kupca\n[3] Datum rezervacije/prodaje\n"
              "[4] Početak projekcije\n[5] Kraj projekcije\n[6] Status")
        choice = input("Po čemu želite da pretražite karte? >> ")
        if choice.isnumeric() and 1 <= int(choice) <= 6:
            break
        print("Unesite odgovarajuću opciju!!!")
    while True:
        criteria = input("Unesite kriterijum pretrage: ")
        if choice == "1":
            if validations.validation_screening_code(criteria):
                value = "screening code"
                break
            user_functions.continue_search()
        elif choice == "2":
            value = "client"
            break
        elif choice == "3":
            if validations.validation_date(criteria):
                value = "date sold"
                break
            user_functions.continue_search()
        elif choice == "4":
            if validations.validation_time(criteria):
                value = "start time"
                break
            user_functions.continue_search()
        elif choice == "5":
            if validations.validation_time(criteria):
                value = "end time"
                break
            user_functions.continue_search()
        elif choice == "6":
            tickets_functions.show_all_tickets(criteria)
    for ticket in tickets.values():
        if criteria.lower() in ticket[value].lower():
            code = ticket["screening code"]
            date = screenings[code]["date"]
            start_time = projections[code[0:4]]["start time"]
            end_time = projections[code[0:4]]["end time"]
            hall = projections[code[0:4]]["hall"]
            display_tickets.append([ticket["ticket key"],
                                    ticket["seat"],
                                    ticket["client"],
                                    ticket["screening code"],
                                    hall,
                                    start_time,
                                    end_time,
                                    date,
                                    ticket["status"]])
    header = ["BR.", "SEDIŠTE", "IME", "ŠIFRA", "SALA", "POČETAK", "KRAJ", "DATUM PRIKAZIVANJA", "STATUS"]
    print(tabulate(display_tickets, header, tablefmt="pretty"))
    set_ticket_search()


def set_ticket_search():
    if len(display_tickets) == 0:
        print("Ne postoje karte sa tim kriterijumima!")
    display_tickets.clear()
    while True:
        print("[0] Ponovna pretraga\n[x] Nazad")
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            search_tickets()
            break
        elif choice.lower() == "x":
            break
        else:
            print("Unesite odgovarajuću stavku!!!")


def search_projections():
    print("PRETRAGA PROJEKCIJA")
    while True:
        print("[1] Datum\n[2] Naziv\n[3] Vreme početka\n[4] Vreme kraja\n[5] Sala")
        criteria = input("Po čemu želite da pretražite projekciju? >> ")
        if criteria.isnumeric() and 1 <= int(criteria) <= 5:
            if int(criteria) == 1:
                print("Određeni su termini za naredne dve nedelje!\nUnesite datum u formatu [DD.MM.YYYY.]!")
                break
            elif int(criteria) == 3 or int(criteria) == 4:
                print("Prve projekcije počinju u 19h\nUnesite vreme u formatu [HH:MM]!")
                break
            elif int(criteria) == 5:
                for hall in movie_halls.keys():
                    print(hall)
                break
            break
        print("Unesite odgovarajuću stavku!")
    index = int(criteria)
    while True:
        searched_value = input("Unesite kriterijum pretrage >> ")
        if validations.validation_projection_search(searched_value, index):
            break
        user_functions.continue_search()
    for row in repertoire_value:
        if searched_value.lower() in row[index].lower():
            filtered_projections.append(row)
    header = ["ŠIFRA", "DATUM", "FILM", "POČETAK", "KRAJ", "SALA", "CENA KARTE"]
    print(tabulate(filtered_projections, header, tablefmt="pretty"))
    set_projections_search()


def set_projections_search():
    if len(filtered_projections) == 0:
        print("Ne postoje projekcije sa ovim kriterijumima!")
    while True:
        print("[0] Ponovna pretraga\n[1] Rezervacija\n[x] Povratak")
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            filtered_projections.clear()
            search_projections()
            break
        elif choice == "1":
            if len(logged_user) == 0:
                print("Potrebna je registracija!!!")
            else:
                tickets_functions.reserve_or_direct_sell("rezervisana")
        elif choice.lower() == "x":
            filtered_projections.clear()
            break
        else:
            print("Unesite odgovarajuću stavku!")


def search_movies(*unfiltered_movies):
    print("PRETRAGA FILMOVA")
    while True:
        print("[1] Naziv\n[2] Žanr\n[3] Trajanje\n[4] Režiser\n[5] Glavne uloge\n"
              "[6] Zemlja porekla\n[7] Godina proizvodnje")
        criteria = input("Po čemu želite da pretražite film? >> ")
        if criteria.isnumeric() and 1 <= int(criteria) <= 7:
            if int(criteria) == 2:
                print(*genres, sep=', ', end='\n')
                break
            elif int(criteria) == 3:
                print("[1] Po dužini\n[2] Po intervalu dužine")
                choice0 = input("Unesite odgovarajuću stavku: ")
                if choice0 == "1":
                    while True:
                        length = input("Unesite dužinu trajanja: ")
                        if validations.validation_length(length):
                            break
                        user_functions.continue_search()
                    movie_length(length, length, *unfiltered_movies)
                elif choice0 == "2":
                    while True:
                        length_min = input("Unesite MINIMALNU dužinu trajanja: ")
                        if validations.validation_length(length_min):
                            break
                        user_functions.continue_search()
                    while True:
                        length_max = input("Unesite MAKSIMALNU dužinu trajanja: ")
                        if validations.validation_length(length_max):
                            break
                        user_functions.continue_search()
                    movie_length(length_min, length_max, *unfiltered_movies)
            break
        print("Unesite odgovarajuću stavku!")
    index = int(criteria) - 1
    while True:
        searched_value = input("Unesite kriterijum pretrage >> ")
        if validations.validation_movie_search(searched_value, index):
            break
        user_functions.continue_search()
    filtered_movies.clear()
    for movie in unfiltered_movies:
        if searched_value.lower() in movie[index].lower():
            filtered_movies.append(movie)
    header = ["FILM", "ŽANR", "DUŽINA", "REŽISER", "GLAVNE ULOGE", "ZEMLJA POREKLA", "GODINA PROIZVODNJE"]
    print(tabulate(filtered_movies, header, tablefmt="pretty"))
    if len(filtered_movies) == 0:
        print("Ne postoje filmovi sa ovim kriterijumima!")
    set_movie_search()


def movie_length(minimal_length, maximal_length, *unfiltered_movies):
    filtered_movies.clear()
    for movie in unfiltered_movies:
        if int(minimal_length) <= int(movie[2]) <= int(maximal_length):
            filtered_movies.append(movie)
    header = ["FILM", "ŽANR", "DUŽINA", "REŽISER", "GLAVNE ULOGE", "ZEMLJA POREKLA", "GODINA PROIZVODNJE"]
    print(tabulate(filtered_movies, header, tablefmt="pretty"))
    if len(filtered_movies) == 0:
        print("Ne postoje filmovi sa ovim kriterijumima!")
    set_movie_search()


def set_movie_search():
    while True:
        print("[0] Dodatni kriterijum\n[1] Ponovna pretraga\n[x] Povratak")
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            search_movies(*filtered_movies)
            break
        elif choice == "1":
            filtered_movies.clear()
            search_movies(*all_movies)
            break
        elif choice.lower() == "x":
            filtered_movies.clear()
            break
        else:
            print("Unesite odgovarajuću stavku!")

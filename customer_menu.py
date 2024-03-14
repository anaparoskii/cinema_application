from variables import *
import user_functions
import search_functions
import tickets_functions
import screenings_functions
import movies_functions


def login_customer():
    while True:
        print("[1] Dostupni filmovi\n[2] Repertoar\n[3] Rezervacije\n[4] Pretraga\n"
              "[5] Promena ličnih podataka\n[x] Odjava")
        choice = input("Odaberite stavku: ")
        if choice == "1":
            movies_functions.available_movies()
            screenings_functions.repertoire_function()
        elif choice == "2":
            screenings_functions.show_repertoire()
            screenings_functions.repertoire_function()
        elif choice == "3":
            while True:
                print("[1] REZERVIŠI kartu\n[2] PREGLEDAJ rezervacije\n[3] PONIŠTI rezervacije\n[x] Nazad")
                choice1 = input("Unisite željenu stavku: ")
                if choice1 == "1":
                    tickets_functions.reserve_or_direct_sell("rezervisana")
                elif choice1 == "2":
                    tickets_functions.show_my_reservations(logged_user[0])
                elif choice1 == "3":
                    tickets_functions.show_my_reservations(logged_user[0])
                    tickets_functions.delete_reservations()
                elif choice1.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!")
        elif choice == "4":
            while True:
                print("[1] Pretraga FILMOVA\n[2] Pretraga PROJEKCIJA\n[x] Nazad")
                choice0 = input("Šta želite da pretražite? >> ")
                if choice0 == "1":
                    search_functions.search_movies(all_movies)
                elif choice0 == "2":
                    search_functions.search_projections()
                elif choice0.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!")
        elif choice == "5":
            user_functions.data_change()
        elif choice.lower() == "x":
            user_functions.logout()
        else:
            print("Unesite odgovarajuću opciju!!!")

from variables import *
import user_functions
import search_functions
import tickets_functions
import screenings_functions
import movies_functions


def login_employee():
    while True:
        print("[1] Dostupni filmovi\n[2] Repetoar\n[3] Pretraga\n[4] Karte\n"
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
                print("[1] Pretraga FILMOVA\n[2] Pretraga PROJEKCIJA\n[3] Pretraga KARATA\n[x] Nazad")
                choice0 = input("Šta želite da pretražite? >> ")
                if choice0 == "1":
                    search_functions.search_movies(all_movies)
                elif choice0 == "2":
                    search_functions.search_projections()
                elif choice0 == "3":
                    search_functions.search_tickets()
                elif choice0.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!")
        elif choice == "4":
            while True:
                print("[1] REZERVIŠI kartu\n[2] PRODAJ kartu\n[3] PREGLEDAJ karte\n"
                      "[4] PONIŠTI rezervacije\n[5] PONIŠTI kartu\n[6] IZMENI kartu\n"
                      "[7] Poništi ISTEKLE rezervacije\n[x] Nazad")
                choice1 = input("Unisite željenu stavku: ")
                if choice1 == "1":
                    tickets_functions.reserve_or_direct_sell("rezervisana")
                elif choice1 == "2":
                    while True:
                        print("[1] Prodaj REZERVISANU kartu\n[2] DIREKTNA prodaja\n[x] Nazad")
                        choice2 = input("Unesite željenu stavku: ")
                        if choice2 == "1":
                            tickets_functions.sell_reservation()
                        elif choice2 == "2":
                            tickets_functions.reserve_or_direct_sell("prodata")
                        elif choice2.lower() == "x":
                            break
                        else:
                            print("Unesite odgovarajuću opciju")
                elif choice1 == "3":
                    while True:
                        print("[1] Rezervacije\n[2] Prodaje\n[3] SVE karte\n[x] Nazad")
                        choice3 = input("Unesite željenu opciju: ")
                        if choice3 == "1":
                            tickets_functions.show_all_tickets("rezervisana")
                        elif choice3 == "2":
                            tickets_functions.show_all_tickets("prodata")
                        elif choice3 == "3":
                            tickets_functions.show_all_tickets("all")
                        elif choice3.lower() == "x":
                            break
                        else:
                            print("Unesite odgovarajuću opciju!!!")
                elif choice1 == "4":
                    tickets_functions.show_all_tickets("rezervisana")
                    tickets_functions.delete_reservations()
                elif choice1 == "5":
                    tickets_functions.show_all_tickets("prodata")
                    tickets_functions.delete_ticket()
                elif choice1 == "6":
                    tickets_functions.edit_ticket()
                elif choice1 == "7":
                    tickets_functions.cancel_reservations()
                elif choice1.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću opciju!!!")
        elif choice == "5":
            user_functions.data_change()
        elif choice.lower() == "x":
            user_functions.logout()
        else:
            print("Unesite odgovarajuću opciju!!!")

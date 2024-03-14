from variables import *
import user_functions
import search_functions
import tickets_functions
import screenings_functions
import movies_functions
import projections_functions
import reports
import save
import validations


def login_manager():
    while True:
        print("[1] Filmovi\n[2] Repertoar\n[3] Pretraga\n[4] Karte\n[5] Registracija zaposlenih\n"
              "[6] Izveštaji\n[7] Promena ličnih podataka\n[x] Odjava")
        choice = input("Odaberite stavku: ")
        if choice == "1":
            while True:
                print("[1] DOSTUPNI filmovi\n[2] DODAJ film\n[3] IZMENI film\n[4] OBRIŠI film\n[x] Nazad")
                choice0 = input("Odaberite stavku: ")
                if choice0 == "1":
                    movies_functions.available_movies()
                    screenings_functions.repertoire_function()
                elif choice0 == "2":
                    movies_functions.add_movie()
                elif choice0 == "3":
                    print("OPCIJE ZA IZMENU FILMA")
                    for movie in all_movies:
                        print(movie[0], sep=", ")
                    while True:
                        movie_name = input("\nKoji film želite da izmenite? >> ")
                        if validations.check_movie(movie_name):
                            movies_functions.edit_movie(movie_name)
                            break
                        user_functions.continue_search()
                elif choice0 == "4":
                    movies_functions.delete()
                elif choice0.lower() == "x":
                    break
                else:
                    print("Neodgovarajuća opcija!")
        elif choice == "2":
            while True:
                print("[1] PRIKAŽI repertoar\n[2] DODAJ projekciju\n[3] IZMENI projekciju\n"
                      "[4] GENERIŠI termine\n[x] Nazad")
                choice3 = input("Odaberite stavku: ")
                if choice3 == "1":
                    screenings_functions.show_repertoire()
                    screenings_functions.repertoire_function()
                elif choice3 == "2":
                    while True:
                        movie_name = input("Za koji film dodajete projekciju? >> ")
                        if validations.check_movie(movie_name):
                            break
                        user_functions.continue_search()
                    projections_functions.add_projection(movie_name)
                elif choice3 == "3":
                    projections_functions.edit_projections()
                elif choice3 == "4":
                    screenings_functions.generate_screenings()
                    save.save_data()
                elif choice3.lower() == "x":
                    break
                else:
                    print("Neodgovarajuća opcija!")
        elif choice == "3":
            while True:
                print("[1] Pretraga FILMOVA\n[2] Pretraga PROJEKCIJA\n[3] Pretraga KARATA\n[x] Nazad")
                choice1 = input("Šta želite da pretražite? >> ")
                if choice1 == "1":
                    search_functions.search_movies(all_movies)
                elif choice1 == "2":
                    search_functions.search_projections()
                elif choice1 == "3":
                    search_functions.search_tickets()
                elif choice1.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!")
        elif choice == "4":
            while True:
                print("[1] REZERVIŠI kartu\n[2] PRODAJ kartu\n[3] PREGLEDAJ karte\n"
                      "[4] PONIŠTI rezervacije\n[5] PONIŠTI kartu\n[6] IZMENI kartu\n"
                      "[7] Poništi ISTEKLE rezervacije\n[x] Nazad")
                choice4 = input("Unisite željenu stavku: ")
                if choice4 == "1":
                    tickets_functions.reserve_or_direct_sell("rezervisana")
                elif choice4 == "2":
                    while True:
                        print("[1] Prodaj REZERVISANU kartu\n[2] DIREKTNA prodaja\n[x] Nazad")
                        choice5 = input("Unesite željenu stavku: ")
                        if choice5 == "1":
                            tickets_functions.sell_reservation()
                        elif choice5 == "2":
                            tickets_functions.reserve_or_direct_sell("prodata")
                        elif choice5.lower() == "x":
                            break
                        else:
                            print("Unesite odgovarajuću opciju")
                elif choice4 == "3":
                    while True:
                        print("[1] Rezervacije\n[2] Prodaje\n[3] SVE karte\n[x] Nazad")
                        choice6 = input("Unesite željenu opciju: ")
                        if choice6 == "1":
                            tickets_functions.show_all_tickets("rezervisana")
                        elif choice6 == "2":
                            tickets_functions.show_all_tickets("prodata")
                        elif choice6 == "3":
                            tickets_functions.show_all_tickets("all")
                        elif choice6.lower() == "x":
                            break
                        else:
                            print("Unesite odgovarajuću opciju!!!")
                elif choice4 == "4":
                    tickets_functions.show_all_tickets("rezervisana")
                    tickets_functions.delete_reservations()
                elif choice4 == "5":
                    tickets_functions.show_all_tickets("prodata")
                    tickets_functions.delete_ticket()
                elif choice4 == "6":
                    tickets_functions.edit_ticket()
                elif choice4 == "7":
                    tickets_functions.cancel_reservations()
                elif choice4.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću opciju!!!")
        elif choice == "5":
            while True:
                print("[1] Registracija PRODAVCA\n[2] Registracija MENADŽERA\n[x] Nazad")
                choice2 = input("Odaberite stavku: ")
                if choice2 == "1":
                    user_functions.create_account("Prodavac")
                elif choice2 == "2":
                    user_functions.create_account("Menadzer")
                elif choice2.lower() == "x":
                    break
                else:
                    print("Neodgovarajuća opcija!")
        elif choice == "6":
            while True:
                print("[a] Lista prodatih karata za odabran datum prodaje\n"
                      "[b] Lista prodatih karata za odabran datum termina bioskopske projekcije\n"
                      "[c] Lista prodatih karata za odabran datum prodaje i odabranog prodavca\n"
                      "[d] Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) prodaje\n"
                      "[e] Ukupan broj i ukupna cena prodatih karata za izabran dan (u nedelji) održavanja projekcije\n"
                      "[f] Ukupna cena prodatih karata za zadati film u svim projekcijama\n"
                      "[g] Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca\n"
                      "[h] Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakog prodavca) "
                      "u poslednjih 30 dana\n"
                      "[x] Nazad")
                choice7 = input("Unesite slovo izmeštaja koji želite da vidite: ")
                if choice7.lower() == "a":
                    reports.report_a()
                    report.clear()
                elif choice7.lower() == "b":
                    reports.report_b()
                    report.clear()
                elif choice7.lower() == "c":
                    reports.report_c()
                    report.clear()
                elif choice7.lower() == "d":
                    reports.report_d()
                    report.clear()
                elif choice7.lower() == "e":
                    reports.report_e()
                    report.clear()
                elif choice7.lower() == "f":
                    reports.report_f()
                    report.clear()
                elif choice7.lower() == "g":
                    reports.report_g()
                    report.clear()
                elif choice7.lower() == "h":
                    reports.report_h()
                    report.clear()
                elif choice7.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću opciju!!!")
        elif choice == "7":
            user_functions.data_change()
        elif choice.lower() == "x":
            user_functions.logout()
        else:
            print("Unesite odgovarajuću opciju!!!")

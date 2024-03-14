import load
import save
import search_functions
import movies_functions
import screenings_functions
import user_functions
from variables import *


def start_point():
    while True:
        print("[1] Napravite nalog\n[2] Prijavite se\n[3] Dostupni filmova\n[4] Repertoar\n"
              "[5] Pretraga\n[x] Izađite iz aplikacije")
        choice = input("Odaberite stavku: ")
        if choice == "1":
            user_functions.create_account("Kupac")
        elif choice == "2":
            user_functions.login()
        elif choice == "3":
            movies_functions.available_movies()
            screenings_functions.repertoire_function()
        elif choice == "4":
            screenings_functions.show_repertoire()
            screenings_functions.repertoire_function()
        elif choice == "5":
            while True:
                print("[1] Pretraga filmova\n[2] Pretraga projekcija\n[x] Nazad")
                choice0 = input("Šta želite da pretražite? >> ")
                if choice0 == "1":
                    search_functions.search_movies(*all_movies)
                elif choice0 == "2":
                    search_functions.search_projections()
                elif choice0.lower() == "x":
                    break
                else:
                    print("Unesite odgovarajuću stavku!")
        elif choice.lower() == "x":
            save.save_data()
            print(">>>IZLAZAK IZ APLIKACIJE<<<")
            exit()
        else:
            print("Unesite odgovarajuću opciju!!!")


if __name__ == "__main__":
    print(">>>BIOSKOP<<<")
    load.load_data()
    start_point()

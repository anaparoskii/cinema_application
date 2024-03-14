from tabulate import tabulate
from variables import *
import user_functions
import screenings_functions
import projections_functions
import save
import validations


def available_movies():
    print("DOSTUPNI FILMOVI")
    header = ["FILM", "ŽANR", "DUŽINA", "REŽISER", "GLAVNE ULOGE", "ZEMLJA POREKLA", "GODINA PROIZVODNJE"]
    print(tabulate(all_movies, header, tablefmt="pretty"))


def add_movie():
    print("DODAJTE NOVI FILM")
    while True:
        movie_name = input("Unesite naziv: ")
        if validations.validation_name(movie_name):
            break
        user_functions.continue_search()
    while True:
        print(*genres, sep=", ")
        genre = input("Unesite žanr: ")
        if validations.validation_genre(genre):
            break
        user_functions.continue_search()
    while True:
        length = input("Unesite dužinu trajanja (u minutima): ")
        if validations.validation_length(length):
            break
        user_functions.continue_search()
    while True:
        director = input("Unesite žerisera: ")
        if validations.validation_is_word(director):
            break
        user_functions.continue_search()
    while True:
        lead_roles = input("Unesite glavne glumce: ")
        if validations.validation_is_word(lead_roles):
            break
        user_functions.continue_search()
    while True:
        country = input("Unesite zemlju porekla: ")
        if validations.validation_is_word(country):
            break
        user_functions.continue_search()
    while True:
        year = input("Unesite godinu proizvodnje: ")
        if validations.validation_year(year):
            break
        user_functions.continue_search()
    all_movies.append([movie_name.title(),
                       genre,
                       length,
                       director.title(),
                       lead_roles.title(),
                       country.title(),
                       year])
    print("FILM USPEŠNO DODAT!\n[0] Dodajte projekciju\n[x] Povratak")
    save.save_data()
    while True:
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            projections_functions.add_projection(movie_name)
            break
        elif choice.lower() == "x":
            save.save_data()
            break
        else:
            print("Unesite odgovarajuću opciju!")


def edit_movie(input_movie_name):
    print("IZMENI FILM")
    while True:
        print("[1] Naziv\n[2] Žanr\n[3] Dužina trajanja\n[4] Žeriser\n[5] Glavne uloge\n"
              "[6] Zemlja porekla\n[7] Godina proizvodnje")
        choice = input("Šta želite da izmenite? >> ")
        if choice.isnumeric() and 1 <= int(choice) <= 7:
            index = int(choice) - 1
            edit_function(input_movie_name, index)
            print("FILM USPEŠNO IZMENJEN!")
            save.save_data()
            break
        else:
            print("Unos nije odgovarajuć!!!")


def edit_function(input_movie_name, index):
    new_value = input("Unesite novu vrednost: ")
    if validations.validation_editing(new_value, index):
        if index == 0:
            for projection in projections:
                projection[2] = new_value
        for movie in all_movies:
            if input_movie_name.lower() in movie[0].lower():
                if index != 1 and index != 2 and index != 6:
                    movie[index] = new_value.title()
                movie[index] = new_value


def delete():
    print("BRISANJE FILMA I PROJEKCIJA")
    while True:
        movie_name = input("Koji film brišete? >> ")
        for movie in all_movies:
            if movie_name.lower() in movie[0].lower():
                delete_dates(movie_name)
                delete_projections(movie_name)
                delete_movie(movie_name)
                print("FILM I PROJEKCIJE USPEŠNO OBRISANE!")
                screenings_functions.generate_screenings()
                save.save_data()
                user_functions.back_to_profile()
        else:
            print("Ne postoji takav film u sistemu!")
            user_functions.continue_search()


def delete_dates(input_movie_name):
    for projection_code, projection in projections.items():
        if input_movie_name.lower() in projection["movie"].lower():
            projection_code = projection["code"]
            for screening_code, screening in list(screenings.items()):
                if str(projection_code) in str(screening["code"]):
                    screenings[screening_code]["status"] = "invalid"


def delete_projections(input_movie_name):
    for projection_code, projection in list(projections.items()):
        if input_movie_name.lower() in projection["movie"].lower():
            del projections[projection_code]


def delete_movie(input_movie_name):
    for movie in all_movies:
        if input_movie_name.lower() in movie[0].lower():
            all_movies.remove(movie)

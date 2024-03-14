from variables import *
import user_functions
import screenings_functions
import save
import validations


def add_projection(movie_name):
    print("DODAVAJTE NOVU PROJEKCIJU")
    start_code = 1000
    projection_code = start_code + len(projections)
    original_price = "400.00"
    while True:
        days = input("Unesite dane prikazivanja: ")
        if validations.validation_days(days):
            break
        user_functions.continue_search()
    while True:
        while True:
            for hall in movie_halls.keys():
                print(hall)
            hall = input("Unesite salu održavanja projekcije: ")
            if validations.validation_hall(hall):
                break
            user_functions.continue_search()
        while True:
            start_time = input("Unesite vreme početka projekcije: ")
            if validations.validation_time(start_time):
                break
            user_functions.continue_search()
        while True:
            end_time = input("Unesite vreme kraja projekcije: ")
            if validations.validation_time(end_time):
                break
            user_functions.continue_search()
        if validations.validation_projection(hall, start_time, end_time, days):
            break
        user_functions.continue_search()
    projections[projection_code] = {"code": str(projection_code),
                                    "hall": hall,
                                    "start time": start_time,
                                    "end time": end_time,
                                    "days": days,
                                    "movie": movie_name.title(),
                                    "ticket price": original_price}
    print("PROJEKCIJA USPEŠNO DODATA!")
    save.save_data()


def edit_projections():
    print("IZMENI PROJEKCIJU")
    while True:
        code = input("Unesite šifru projekcije koju izmenjujete: ")
        if validations.validation_screening_code(code):
            break
        user_functions.continue_search()
    while True:
        print("[1] Dani prikazivanja\n[2] Vreme početka i kraja\n[3] Sala")
        choice = input("Šta želite da izmenite? >> ")
        if choice == "1":
            while True:
                new_days = input("Unesite dane prikazivanja: ")
                if validations.validation_days(new_days):
                    projections[code]["days"] = new_days
                    break
                user_functions.continue_search()
        elif choice == "2":
            while True:
                while True:
                    new_start_time = input("Unesite vreme početka projekcije: ")
                    if validations.validation_time(new_start_time):
                        break
                    user_functions.continue_search()
                while True:
                    new_end_time = input("Unesite vreme kraja projekcije: ")
                    if validations.validation_time(new_end_time):
                        break
                    user_functions.continue_search()
                hall = projections[code]["hall"]
                days = projections[code]["days"]
                if validations.validation_projection(hall, new_start_time, new_end_time, days):
                    projections[code]["start time"] = new_start_time
                    projections[code]["end time"] = new_end_time
                    break
                user_functions.continue_search()
            break
        elif choice == "3":
            while True:
                while True:
                    for hall in movie_halls.keys():
                        print(hall)
                    new_hall = input("Unesite salu održavanja projekcije: ")
                    if validations.validation_hall(new_hall):
                        break
                    user_functions.continue_search()
                days = projections[code]["days"]
                start_time = projections[code]["start time"]
                end_time = projections[code]["end time"]
                if validations.validation_projection(new_hall, start_time, end_time, days):
                    projections[code]["hall"] = new_hall
                    break
                user_functions.continue_search()
            break
        else:
            print("Unesite odgovarajuću stavku!!!")
    print("PROJEKCIJA USPEŠNO IZMENJENA")
    edit_projections_function()


def edit_projections_function():
    while True:
        print("[0] Nastavite izmenu\n[x] Nazad")
        choice = input("Unesite željenu stavku: ")
        if choice == "0":
            edit_projections()
        elif choice.lower() == "x":
            screenings_functions.generate_screenings()
            save.save_data()
            break
        else:
            print("Unesite odgovarajuću opciju!!!")

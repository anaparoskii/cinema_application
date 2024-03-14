import datetime
from variables import *


def check_role(username):
    for user in all_users:
        if username == user[0]:
            role = user[3]
            return role


def validation_username(username):
    for user in all_users:
        if username == user[0]:
            print("Korisničko ime već postoji!!!")
            return False
    return True


def validation_password(password):
    if len(password) < 6 or password.isalpha():
        print("Šifra mora da sadrži barem 6 karaktera i 1 broj!!!")
        return False
    return True


def validation_is_word(input_value):
    if input_value.isnumeric():
        print("Unos ne sme da sadrži brojeve!!!")
        return False
    return True


def validation_time(input_value):
    try:
        datetime.datetime.strptime(input_value, '%H:%M')
        return True
    except ValueError:
        print("Unesite vreme u odgovarajućem formatu!")
        return False


def validation_date(input_value):
    try:
        datetime.datetime.strptime(input_value, '%d.%m.%Y.')
        return True
    except ValueError:
        print("Unesite datum u odgovarajućem formatu!")
        return False


def validation_name(input_value):
    for movie in all_movies:
        if input_value == movie[0]:
            print("Takav film već postoji u sistemu!!!")
            return False
    return True


def validation_genre(input_value):
    input_genre = input_value.split(", ")
    for genre in input_genre:
        if genre in genres:
            return True
    print("Unos nije odgovarajuć!!!")
    return False


def validation_genre_search(input_value):
    for genre in genres:
        if input_value in genre:
            return True
    print("Unos nije odgovarajuć!!!")
    return False


def validation_length(input_value):
    if input_value.isnumeric():
        return True
    print("Unos mora biti broj!!!")
    return False


def validation_year(input_value):
    if input_value.isnumeric() and len(input_value) == 4:
        return True
    print("Format unosa nije validan (godina je formata ČETIRI BROJA!)!!!")
    return False


def validation_days(input_value):
    days = input_value.split(", ")
    for weekday in days:
        if weekday in working_days:
            return True
    else:
        print("Unos nije odgovarajuć!!!")
        return False


def validation_projection(input_hall, input_start_time, input_end_time, input_days):
    for projection_code, projection in projections.items():
        if projection["hall"] == input_hall.upper() and input_days.lower() in projection["days"].lower() and (
                (projection["start time"][0:2] <= input_start_time[0:2] <= projection["end time"][0:2]) or
                (projection["start time"][0:2] <= input_end_time[0:2] <= projection["end time"][0:2])):
            print("Postoji projekcija koja se tada prikazuje!!!")
            return False
    return True


def validation_hall(input_value):
    for hall in movie_halls.keys():
        if input_value.upper() in hall:
            return True
    else:
        print("Takva sala ne postoji!!!")
        return False


def check_movie(input_movie_name):
    for movie in all_movies:
        if input_movie_name.lower() in movie[0].lower():
            return True
    print("Ne postoji takav film u sistemu!!!")
    return False


def validation_editing(input_value, index):
    if index == 0:
        if validation_name(input_value):
            return True
        return False
    elif index == 1:
        if validation_genre(input_value):
            return True
        return False
    elif index == 2:
        if validation_length(input_value):
            return True
        return False
    elif index == 3 or index == 4 or index == 5:
        if validation_is_word(input_value):
            return True
        return False
    elif index == 6:
        if validation_year(input_value):
            return True
        return False


def validation_projection_search(input_value, index):
    if index == 1:
        if validation_date(input_value):
            return True
        return False
    elif index == 2:
        if check_movie(input_value):
            return True
        return False
    elif index == 3 or index == 4:
        if validation_time(input_value):
            return True
        return False
    elif index == 5:
        if validation_hall(input_value):
            return True
        return False


def validation_movie_search(input_value, index):
    if index == 0:
        if check_movie(input_value):
            return True
        return False
    elif index == 1:
        if validation_genre_search(input_value):
            return True
        return False
    elif index == 3 or index == 4 or index == 5:
        if validation_is_word(input_value):
            return True
        return False
    elif index == 6:
        if validation_year(input_value):
            return True
        return False


def check_ticket_price(day, projection):
    import datetime
    if datetime.datetime.strptime(day, "%d.%m.%Y.").weekday() == 1:
        new_price = float(projection["ticket price"]) - 50.00
    elif datetime.datetime.strptime(day, "%d.%m.%Y.").weekday() > 4:
        new_price = float(projection["ticket price"]) + 50.00
    else:
        new_price = float(projection["ticket price"])
    return new_price


def validation_seat(screening_code, selected_seat):
    for row in hall_seats[screening_code.upper()]:
        for i in range(len(row)):
            if selected_seat.upper() == row[i]:
                return True
    print("Ne postoji takvo sedište!")
    return False


def validation_ticket_key(input_value):
    for key in tickets.keys():
        if input_value in str(key):
            return True
    print("Ne postoji takva karta!")
    return False


def validation_screening_code(input_value):
    for key in screenings.keys():
        if input_value in key:
            return True
    print("Ne postoji projekcija sa takvom šifrom!")
    return False


def validation_start_time(screening_key):
    today_string = datetime.datetime.today().strftime('%d.%m.%Y.')
    today = today_string.split(".")
    year_now = int(today[2])
    month_now = int(today[1])
    day_now = int(today[0])
    screening_date = screenings[screening_key]["date"]
    date = screening_date.split(".")
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    now_string = datetime.datetime.now().strftime('%H:%M')
    now = now_string.split(":")
    hour_now = int(now[0])
    minute_now = int(now[1])
    second_now = 0
    start_time = projections[screening_key[0:4]]["start time"].split(":")
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    start_second = 0
    current = datetime.datetime(year_now, month_now, day_now, hour_now, minute_now, second_now)
    start = datetime.datetime(year, month, day, start_hour, start_minute, start_second)
    limit = start - datetime.timedelta(minutes=30)
    if current >= limit:
        return True
    print("Još uvek mogu da se preuzmu rezervacije!!!")
    return False


def validation_employee(input_value):
    for user in all_users:
        if input_value.lower() in user[0].lower() and user[3] != "Kupac":
            return True
    print("Ne postoji registrovani radnik sa takvim imenom!!!")
    return False


def validation_client(input_value):
    for ticket in tickets.values():
        if input_value in ticket["client"]:
            return True
    print("Ne postoji karta rezervisana pod ovim imenom!!!")
    return False


def validation_client_screening(input_client, input_screening):
    for ticket in tickets.values():
        if input_client in ticket["client"] and input_screening in ticket["screening code"]:
            return True
    print("Ovaj klijent nije rezervisao kartu za odabrani termin!!!")
    return False


def validation_client_screening_seat(input_client, input_screening, input_seat):
    for ticket in tickets.values():
        if (input_client in ticket["client"] and input_screening in ticket["screening code"]
                and input_seat in ticket["seat"]):
            return True
    print("Ovaj klijent nije rezervisao odabrano sedište za odabrani termin!!!")
    return False


def split_date(date):
    values = date.split(".")
    day = values[0]
    month = values[1]
    year = values[2]
    date_split = datetime.datetime(int(year), int(month), int(day))
    return date_split


def validation_reserved_screening(input_value):
    for ticket in tickets.values():
        if ticket["status"] == "rezervisana" and input_value.upper() in ticket["screening code"]:
            return True
    print("Ne postoji rezervacija za ovaj termin!!!")
    return False

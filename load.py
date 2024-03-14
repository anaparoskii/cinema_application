from variables import *
import seating
import validations
import screenings_functions


def load_data():
    with open('files/users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line[:len(line) - 1]
            words = line.split("|")
            all_users.append(words)
    file.close()
    with open('files/movies.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line[:len(line) - 1]
            words = line.split("|")
            all_movies.append(words)
    file.close()
    with open('files/projections.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            projection_code, hall, start_time, end_time, weekdays, movie, ticket_price = line.split("|")
            projections[projection_code] = {"code": projection_code,
                                            "hall": hall,
                                            "start time": start_time,
                                            "end time": end_time,
                                            "days": weekdays,
                                            "movie": movie,
                                            "ticket price": ticket_price}
    file.close()
    with open('files/dates.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            screening_code, date, status = line.split("|")
            screenings[screening_code] = {"code": screening_code,
                                          "date": date,
                                          "status": status}
    file.close()
    screenings_functions.delete_old_screenings()
    screenings_functions.generate_screenings()
    with open('files/halls.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            hall_code, number_of_rows, seats = line.split("|")
            movie_halls[hall_code] = {"code": hall_code,
                                      "rows": number_of_rows,
                                      "seats": seats}
    file.close()
    with open('files/tickets.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            key, seat, ticket_buyer, screening_code, date, status = line.split("|")
            tickets[key] = {"ticket key": key,
                            "seat": seat,
                            "client": ticket_buyer,
                            "screening code": screening_code,
                            "date sold": date,
                            "status": status}
    file.close()
    with open('files/sold_tickets.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            key, seat, ticket_buyer, screening_code, date_sold, price, seller = line.split("|")
            sold_tickets[key] = {"ticket key": key,
                                 "seat": seat,
                                 "client": ticket_buyer,
                                 "screening code": screening_code,
                                 "date sold": date_sold,
                                 "ticket price": price,
                                 "sold by": seller}
    file.close()
    for projection_value in projections.values():
        for screening_value in screenings.values():
            if int(screening_value["code"][0:4]) == int(projection_value["code"]):
                day = screening_value["date"]
                if screening_value["status"] == "valid":
                    repertoire[screening_value["code"]] = {"date": day,
                                                           "movie": projection_value["movie"],
                                                           "start time": projection_value["start time"],
                                                           "end time": projection_value["end time"],
                                                           "hall": projection_value["hall"],
                                                           "ticket price":
                                                               validations.check_ticket_price(day, projection_value)}
    for repertoire_key, repertoire_item in repertoire.items():
        repertoire_value.append([repertoire_key,
                                 repertoire_item["date"],
                                 repertoire_item["movie"],
                                 repertoire_item["start time"],
                                 repertoire_item["end time"],
                                 repertoire_item["hall"],
                                 repertoire_item["ticket price"]])
    seating.seats_chart()
    seating.taken_seats()

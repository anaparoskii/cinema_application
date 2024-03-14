from variables import *


def save_reports(letter):
    if letter == "a":
        with open('reports/report_a.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + value[1] + "|"
                           + value[2] + "|"
                           + value[3] + "|"
                           + value[4] + "|"
                           + value[5] + "\n")
        file.close()
    elif letter == "b":
        with open('reports/report_b.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + value[1] + "|"
                           + value[2] + "|"
                           + value[3] + "|"
                           + value[4] + "|"
                           + value[5] + "\n")
        file.close()
    elif letter == "c":
        with open('reports/report_c.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + value[1] + "|"
                           + value[2] + "|"
                           + value[3] + "|"
                           + value[4] + "|"
                           + value[5] + "\n")
        file.close()
    elif letter == "d":
        with open('reports/report_d.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + str(value[1]) + "|"
                           + str(value[2]) + "\n")
        file.close()
    elif letter == "e":
        with open('reports/report_e.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + value[1] + "|"
                           + value[2] + "|"
                           + str(value[3]) + "|"
                           + str(value[4]) + "\n")
        file.close()
    elif letter == "f":
        with open('reports/report_f.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + str(value[1]) + "|"
                           + str(value[2]) + "\n")
        file.close()
    elif letter == "g":
        with open('reports/report_g.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + value[1] + "|"
                           + str(value[2]) + "|"
                           + str(value[3]) + "\n")
        file.close()
    elif letter == "h":
        with open('reports/report_h.txt', 'w') as file:
            for value in report:
                file.write(value[0] + "|"
                           + str(value[1]) + "|"
                           + str(value[2]) + "\n")
        file.close()


def save_data():
    with open('files/users.txt', 'w') as file:
        for user in all_users:
            file.write(user[0] + "|"
                       + user[1] + "|"
                       + user[2] + "|"
                       + user[3] + "\n")
    file.close()
    with open('files/movies.txt', 'w') as file:
        for movie in all_movies:
            file.write(movie[0] + "|"
                       + movie[1] + "|"
                       + movie[2] + "|"
                       + movie[3] + "|"
                       + movie[4] + "|"
                       + movie[5] + "|"
                       + movie[6] + "\n")
    file.close()
    with open('files/projections.txt', 'w') as file:
        for projection_code, projection in projections.items():
            file.write(str(projection["code"]) + "|"
                       + projection["hall"] + "|"
                       + projection["start time"] + "|"
                       + projection["end time"] + "|"
                       + projection["days"] + "|"
                       + projection["movie"] + "|"
                       + str(projection["ticket price"]) + "\n")
    file.close()
    with open('files/dates.txt', 'w') as file:
        for screening_code, screening in screenings.items():
            file.write(screening_code + "|"
                       + screening["date"] + "|"
                       + screening["status"] + "\n")
    file.close()
    with open('files/tickets.txt', 'w') as file:
        for key, ticket in tickets.items():
            file.write(str(key) + "|"
                       + ticket["seat"] + "|"
                       + ticket["client"] + "|"
                       + ticket["screening code"] + "|"
                       + ticket["date sold"] + "|"
                       + ticket["status"] + "\n")
    file.close()
    with open('files/sold_tickets.txt', 'w') as file:
        for key, ticket in sold_tickets.items():
            file.write(str(key) + "|"
                       + ticket["seat"] + "|"
                       + ticket["client"] + "|"
                       + ticket["screening code"] + "|"
                       + ticket["date sold"] + "|"
                       + str(ticket["ticket price"]) + "|"
                       + ticket["sold by"] + "\n")
    file.close()

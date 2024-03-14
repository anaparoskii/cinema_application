from variables import *


def seats_chart():
    for screening in screenings.values():
        code = screening["code"]
        hall = projections[code[0:4]]["hall"]
        number_of_rows = movie_halls[hall]["rows"]
        seats = movie_halls[hall]["seats"]
        seat_chart = []
        letters = []
        for letter in range(ord("A"), ord(seats) + 1):
            letters.append(chr(letter))
        for i in range(int(number_of_rows) + 1):
            seat_chart.append([])
            for j in letters:
                seat_chart[i].append(j + str(i))
        hall_seats[code] = seat_chart


def taken_seats():
    for ticket in tickets.values():
        screening = ticket["screening code"]
        seat = ticket["seat"]
        hall = hall_seats[screening]
        for row in hall:
            for i in range(len(row)):
                if row[i] == seat:
                    row[i] = "XX"


def new_taken_seat(screening_code, seat):
    for row in hall_seats[screening_code]:
        for i in range(len(row)):
            if row[i] == seat:
                row[i] = "XX"
                break


def available_seat(screening_code, seat):
    for row in hall_seats[screening_code]:
        for i in range(len(row)):
            if str(row[0])[1:2] == seat[1:2]:
                row[ord(seat[0:1]) - 65] = seat
                break

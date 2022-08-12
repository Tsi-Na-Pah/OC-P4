""" Generate Static Data Randomly"""
import random

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]
MONTH = [1,2,3,4,5,6,7,8,9,10,11,12]
DAY = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
YEAR = [1973,1980,1990,1995,1996,1997,1998,1999,2000,2001,2002]
GENDER = ["M", "F"]


def random_static_player_data():

    name_size = 10
    lastname = ""
    firstname = ""
    random.shuffle(ALPHABET)
    for i in range(name_size):
        lastname = lastname + ALPHABET[i]
    random.shuffle(ALPHABET)
    for i in range(name_size):
        firstname = firstname + ALPHABET[i]
    random.shuffle(GENDER)
    gender = GENDER[0]
    random.shuffle(DAY)
    random.shuffle(MONTH)
    random.shuffle(YEAR)
    birthdate = str(DAY[0]) + "/" + str(MONTH[0]) + "/" + str(YEAR[0])

    player_info = {
        "LastName": lastname,
        "FirstName": firstname,
        "BirthDate": birthdate,
        "Gender": gender,
        "Rank": 0
    }

    return player_info






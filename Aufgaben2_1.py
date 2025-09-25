#Aufgabe 1
def test_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#Aufgabe 2
def preis(stations, halbtax):
    if stations >= 10:
        wants_day_pass = input("Der Preis ist teurer als eine Tageskarte, willst du eine Tageskarte kaufen? (yes|no)")
        if wants_day_pass == "yes":
            print(f"Die Kosten für die Tageskarte betragen {5 if halbtax else 10}Fr")
            return
    print(f"Die Kosten für die Einzelfahrt betragen {stations / 2 if halbtax else stations}Fr")

#stations = input("Wie viele Stationen willst du fahren?")
#halbtax = input("Besitzt du in Halbpreis Abo? (yes|no)")
#if halbtax == "yes":
#    preis(int(stations), True)
#else:
#    preis(int(stations), False)

#Aufgabe 3
def print_line(max_number):
    for i in range(1, max_number + 1):
        print(i)

#print_line(12)

#Aufgabe 4
def print_fizz_buzz(max_number):
    for i in range(1, max_number + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Aufgabe 5
def print_fizz_buzz(max_number):
    for i in range(1, max_number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Aufgabe aus Unterricht
colors = [ "Rot", "Blau", "Grün", "Gelb", "Lila", "Orange", "Pink", "Braun", "Schwarz", "Weiss"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Aufgabe 6/7/8
punkte = [
    ["Fabian", 5, 6, 7],
    ["Marco", 3, 5, 2],
    ["Mara", 5, 5, 6],
    ["Elena", 3, 2, 7]]

def punkte_liste(punkt_liste):
    average_sum = 0

    for punkt in punkt_liste:
        sum = punkt[1] + punkt[2] + punkt[3]
        mark = sum*5/20+1
        print(f"Name: {punkt[0]}\nSumme: {sum}\nNote: {mark}\n-------------------")
        average_sum += mark

    print(f"Der Notendurchschnitt beträgt {average_sum/len(punkt_liste)}")

punkte_liste(punkte)
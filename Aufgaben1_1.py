# Aufgabe 1
def hallo():
    print("Hello World")

#Aufgabe 2
def summe(zahl_0, zahl_1, zahl_2):
    summe = zahl_0 + zahl_1 + zahl_2
    return summe

#Aufgabe 3
def multiplizieren(zahl_1, zahl_2):
    resultat = zahl_1 * zahl_2
    return resultat

#Aufgabe 4
def persoenliche_gruesse(name):
    print("Hello " + name)

#Aufgabe 5
def addiere(a, b):
    return a + b

#Aufgabe 6
def dividiere(a, b):
    return a / b

#Aufgabe 7
def quadrat(zahl):
    return zahl * zahl

#Aufgabe 8
def zeige_infos(name, alter):
    print("Mein Name ist " + name + "und ich bin " + str(alter) + " Jahre alt.")

#Aufgabe 9
def biggest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

#Aufgabe 10:
def multiply_list(list):
    result = 1
    for element in list:
        result = result * element
    return result

#Aufgabe 11:
def laenge_string(s):
    count = 0
    for letter in s:
        count += 1
    return count

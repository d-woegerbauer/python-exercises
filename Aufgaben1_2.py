#Aufgabe 1
def get_sum_average_of_string(string):
    sum = 0
    count = 0
    string_numbers = "0123456789"
    for letter in string:
        if letter in string_numbers:
            sum += int(letter)
            count += 1
    return f"Summe: {sum}; Durchschnitt: {sum/count}"

#Aufgabe 2
def reverse_string(string):
    new_string = ""
    for letter in string:
        new_string = letter + new_string
    return new_string

#Aufgabe 3
def count_vowels(string):
    vowel_count = 0
    vowels = "aeiou"
    for letter in string:
        if letter in vowels:
            vowel_count += 1
    return vowel_count

#Aufgabe 4
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

#Aufgabe 5
def word_count(string):
    string = string.strip()

    if not string:
        return 0

    words = string.split()

    return len(words)

#Aufgabe 6
def is_palindrome(string):
    string = string.lower().replace(" ", "")

    return True if string == string[::-1] else False

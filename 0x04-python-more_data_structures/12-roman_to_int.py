#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int = 0
    roman_numerals_character_map = {
            "I": 1, "IV": 4, "V": 5,
            "IX": 9, "X": 10, "XL": 40,
            "L": 50, "XC": 90, "C": 100,
            "CD": 400, "D": 500, "CM": 900, "M": 1000}
    for roman_numerals in roman_string:
        roman_to_int += roman_numerals_character_map.get(roman_numerals)
    return (roman_to_int)

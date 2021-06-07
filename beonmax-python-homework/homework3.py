# Парсинг римских чисел
# Написать функцию, которая принимает на вход строку - римское число, а
# возвращает это число в арабском виде. Например, если передаём "XV" - должна
# вернуть 15, если передаём "IV" - должна вернуть 4.
# Вот список римских символов и их отображение на арабские числа:
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000

def parse_roman(num):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
    result = 0
    for ind, ch in enumerate(num):
        if (ind + 1) == len(num) or roman_num[ch] >= roman_num[num[ind + 1]]:
            result += roman_num[ch]
        else:
            result -= roman_num[ch]
    return result


# coach's solution
# romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


# def parse_roman(roman):
#     result = 0
#     for i, c in enumerate(roman):
#         if i + 1 < len(roman) and romans[roman[i] < romans[roman[i + 1]]]:
#             result -= romans[roman[i]]
#         else:
#             result += romans[roman[i]]
#     return result

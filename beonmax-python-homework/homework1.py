# Реализуйте одну классическую и достаточно простую игру: "Угадай число"
# Компьютер загадывает число от 1 до 50 и даёт 6 попыток пользователю, чтобы
# тот смог угадать загаданное число. Когда пользователь вводит число, компьютер
# проверяет угадано ли число и если не угадано, то сообщает пользователю
# меньше ли или больше загаданное число. Если пользователь угадал - то
# сообщает о том, что число отгадано.
# Подсказка: для "загадывания" числа используйте модуль random: импортируйте
# его и для генерации (загадывания) числа вызовите метод random.randint(1, 50)
import random


def guess_number():
    num = random.randint(1, 50)
    count = 0
    while True:
        user_num = int(input('Guess a number from 1 to 50?'))
        count += 1
        if user_num == num:
            print(f"You won. Number of attempts = {count}")
            break
        if user_num < num:
            print(f"Try again. The hidden number is greater than {user_num}")
        if user_num > num:
            print(f"Try again. The hidden number is less than {user_num}")
        if user_num != num and count == 6:
            print(f'You loss. My number was {num}')
            break


guess_number()

# coach's solution
# import random
#
# tries = 0
# number = random.randint(1, 50)
# print(
#     'Hmmm... Try to guess what number between 1 and 50 I was thinking about :)')
# while tries < 6:
#     guess = int(input('Take a guess: '))
#     tries += 1
#     if guess < number:
#         print('Your guess is too low')
#     if guess > number:
#         print('Your guess is too high')
#     if guess == number:
#         print(f'Congratulations! You guessed my number in {tries} guesses')
#         break
#     if guess != number and tries == 6:
#         print(f"Sorry, but you didn't make it. My number was: {number}")

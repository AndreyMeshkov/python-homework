from random import randint


def guess_number():
    num = randint(1, 100)
    count = 0
    while True:
        count += 1
        user_num = int(input('What is number?'))
        if user_num == num:
            print(f"You won. Number of attempts = {count}")
            answer = input(f'Would you like to play one more time? (y/n)')
            if answer == 'y':
                print('Begin')
                guess_number()
            elif answer == 'n':
                print('Good bye!')
                break
        elif user_num < num:
            print(f"Try again. The hidden number is greater than {user_num}")
        elif user_num > num:
            print(f"Try again. The hidden number is less than {user_num}")


guess_number()

# coach's solution
# import random
#
# x = random.randint(1, 100)
# user_num = 0
# cnt = 0
#
# while True:
#     user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
#     cnt += 1
#     if user_num == x:
#         print(f'Ты угадал число за {cnt} попыток')
#         print("""
#                 ------------
#                 |           |
#                 |  0     0  |
#                 |     <     |
#                 |  .     .  |
#                 |   `...`   |
#                 ------------
#                 """)
#         if input('Сыграем еще? "y|n":') == 'y':
#             x = random.randint(1, 100)
#             cnt = 0
#         else:
#             print('Спасибо за игру')
#             break
#     elif user_num > x:
#         print('Мое число меньше')
#     else:
#         print('Мое число больше')

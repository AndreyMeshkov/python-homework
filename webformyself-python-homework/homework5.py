# num = 25
# count = 1
# is_answer_right = False
# while not is_answer_right:
#     user_num = int(input('What is number?'))
#     if user_num == num:
#         print(f"You won. Number of attempts = {count}")
#         is_answer_right = True
#     elif user_num < num:
#         print(f"Try again. The hidden number is greater than {user_num}")
#         count += 1
#     elif user_num > num:
#         print(f"Try again. The hidden number is less than {user_num}")
#         count += 1


def guess_number(num):
    count = 1
    is_answer_right = False
    while not is_answer_right:
        user_num = int(input('What is number?'))
        if user_num == num:
            print(f"You won. Number of attempts = {count}")
            is_answer_right = True
        elif user_num < num:
            print(f"Try again. The hidden number is greater than {user_num}")
            count += 1
        elif user_num > num:
            print(f"Try again. The hidden number is less than {user_num}")
            count += 1


guess_number(33)

# coach's solution
# x = 75
# user_num = 0
# cnt = 0
# while True:
#     user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
#     cnt += 1
#     if user_num == x:
#         print(f'Ты угадал число за {cnt} попыток')
#         print('Спасибо за игру')
#         break
#     elif user_num > x:
#         print('Мое число меньше')
#     else:
#         print('Мое число больше')

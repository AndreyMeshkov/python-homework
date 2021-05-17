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

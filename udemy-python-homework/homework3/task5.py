height = int(input("What is your height in cm?"))
price = 0
if height < 120:
    print("Can't ride")
else:
    print("Can ride")
    age = int(input("What is your age?"))
    if age < 12:
        price += 5
        print("Child tickets are $5")
    elif age <= 18:
        price += 7
        print("Youth tickets are $7")
    elif age < 45:
        price += 12
        print("Adult tickets are $5")
    elif age <= 55:
        price += 0
        print("You have a free ride on us!")
    want_photo = input("Want photo? Y or N?")
    if want_photo == "Y":
        price += 3
    print(f"The total bill is {price}$")

# Coach's solution:

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Love Calculator
# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."
#
# e.g.
#
# name1 = "Angela Yu"
#
# name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
#
# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.
# e.g. When you hit run, this is what should happen:
#
# https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr
#
# The testing code will check for print output that is formatted like one of the lines below:
#
# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."
# Hint
# The lower() function changes all the letters in a string to lower case.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
#
# The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
#
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:
#
# https://repl.it/@appbrewery/day-3-5-test-your-code
#
# This repl includes my testing code that will check if your code meets this assignment's objectives.
#
# Solution
# https://repl.it/@appbrewery/day-3-5-solution

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()
count_t = name1_lower_case.count("t") + name2_lower_case.count("t")
count_r = name1_lower_case.count("r") + name2_lower_case.count("r")
count_u = name1_lower_case.count("u") + name2_lower_case.count("u")
count_e = name1_lower_case.count("e") + name2_lower_case.count("e")
count_l = name2_lower_case.count("l") + name1_lower_case.count("l")
count_o = name2_lower_case.count("o") + name1_lower_case.count("o")
count_v = name2_lower_case.count("v") + name1_lower_case.count("v")
total1 = count_t + count_r + count_u + count_e
total2 = count_l + count_o + count_v + count_e
result = int(str(total1) + str(total2))
if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")

# Coach's solution:
#
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

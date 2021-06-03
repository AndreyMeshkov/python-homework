# task 1
words = ['мадам', 'топот', 'test', 'madam', 'word']
res = []
for i in words:
    if i == i[::-1]:
        res.append(i)
print(res)
# coach's solution 1
# palindromes = []
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
# print(palindromes)
# coach's solution 2
# palindromes = [word for word in words if word == word[::-1]]
# print(palindromes)

# task 2
my_str = ['Око за око', "А роза упала на лапу Азора", 'Около Миши молоко']
res2 = []
for i in my_str:
    if i.replace(' ', '').upper() == i[::-1].replace(' ', '').upper():
        res2.append(i)
print(res2)
# coach's solution 1
# palindromes = []
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
# print(palindromes)

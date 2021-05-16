# task 1
# l1 = [1, 2, 3]
# l2 = []
# for num in l1:
#     l2.append(num * 2)
# print(l1, l2, sep='\n')

def multiply(l):
    l2 = [i * 2 for i in l]
    return l2


print(multiply([1, 2, 3, 4, 5, 6, 6]))


# task 2
# res = 0
# for num in l1:
#     res += num ** 2
# print(res)

def sum_squere(l):
    return sum([i ** 2 for i in l])


print(sum_squere([1, 2, 3, 4, 5, 6, 7]))


# task 3
# time1 = 3
# time2 = 6.7
# time3 = 11.8
# print(int(time1 * 0.5))
# print(int(time2 * 0.5))
# print(int(time3 * 0.5))
def count_water(time):
    return int(time * 0.5)


print(count_water(3))
print(count_water(6.7))
print(count_water(11.8))

# task 4
s = 'Hello world'


# if ' ' in s:
#     s = s.upper()
# else:
#     s = s.lower()
# print(s)
def say_smt(string):
    if ' ' in string:
        return string.upper()
    else:
        return string.lower()


print(say_smt('Hello World'))

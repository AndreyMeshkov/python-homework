# task 1
l1 = [1, 2, 3]
l2 = []
for num in l1:
    l2.append(num * 2)
print(l1, l2, sep='\n')

# task 2
res = 0
for num in l1:
    res += num ** 2
print(res)

# task 3
time1 = 3
time2 = 6.7
time3 = 11.8
print(int(time1 * 0.5))
print(int(time2 * 0.5))
print(int(time3 * 0.5))

# task 4
s = 'Hello world'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)

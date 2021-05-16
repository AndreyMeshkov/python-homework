# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f'{i} * {j} = {i * j}\t', end='')
#     print('')
def create_multiplication_table(start, end):
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            print(f'{i} * {j} = {i * j}\t', end='')
        print('')


create_multiplication_table(4, 9)

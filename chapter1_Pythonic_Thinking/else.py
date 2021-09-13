# for i in range(3):
#     print('Loop', i)
#     if i == 1:
#         # print(i)
#         break
# else:
#     print('Else block!')


a = 4
b = 9


# for i in range(2, min(a, b) + 1):
#     print('Testing', i)
#     if a % i == 0 and b % i == 0:
#         print('Not coprime')
#         break
#
# else:
#     print('Coprime')

# def coprime(a, b):
#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             return False
#         return True
#
#
# assert coprime(4, 9)
# assert not coprime(3, 6)

def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)

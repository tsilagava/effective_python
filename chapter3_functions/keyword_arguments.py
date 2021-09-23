def remainder(number, divisor):
    return number % divisor
#
#
# assert remainder(20, 7) == 6
#
# print(remainder(20, 7))
# remainder(number=20, 7)


# my_kwargs = {
#     'number': 20,
#     'divisor': 7,
# }
#
# assert remainder(**my_kwargs) == 6


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


print_parameters(name='Tea', surname='Silagava')




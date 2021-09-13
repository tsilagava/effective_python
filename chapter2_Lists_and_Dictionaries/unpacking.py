# car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
# car_ages_descending = sorted(car_ages, reverse=True)
#
# print(car_ages_descending)
#
# oldest, second_oldest, *others = car_ages_descending
#
# print(oldest)
# print(second_oldest)
#
# oldest, *others, youngest = car_ages_descending
# print(oldest, youngest, others)
#
# *others, second_youngest, youngest = car_ages_descending
# print(youngest, second_youngest, others)

short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)
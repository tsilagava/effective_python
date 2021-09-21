numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}


# def sort_priority(values, groups):
#     found = False
#
#     def helper(x):
#         if x in groups:
#             found = True
#             return 0, x
#         return 1, x
#     values.sort(key=helper)
#     return found
#
#
# found = sort_priority(numbers, group)
# print(numbers)
# print(found)


# def sort_priority(values, groups):
#     found = False
#
#     def helper(x):
#         if x in groups:
#             nonlocal found
#             found = True
#             return 0, x
#         return 1, x
#     values.sort(key=helper)
#     return found
#
#
# found = sort_priority(numbers, group)
# print(numbers)
# print(found)


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in group:
            self.found = True
            return 0, x
        return 1, x


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True



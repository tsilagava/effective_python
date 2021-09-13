# class MyClass:
#     def __init__(self):
#         self.aligator = 'hatchling'
#         self.eliphant = 'calf'
#
#
# a = MyClass()
#
# print(MyClass.__dict__)
#
# for key, value in a.__dict__.items():
#     print(f'{key} = {value}')
#
# print(a.__dict__)

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
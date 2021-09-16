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
#
#
def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
#
#
def get_winners(ranks):
    return next(iter(ranks))
#
# ranks = {}
# populate_ranks(votes, ranks)
# print(ranks)
# winner = get_winners(ranks)
# print(winner)

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)



def get_winners(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name


def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('must provide a dict instance')
    return next(iter(ranks))



sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winners(sorted_ranks)
print(winner)
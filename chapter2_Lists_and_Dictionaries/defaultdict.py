# visits = {
#     'Mexico': {'Tulum', 'Puerto Vallarta'},
#     'Japan': {'Hakone'},
# }
#
# visits.setdefault('France', set()).add('Arles')
#
# print(visits)

# class Visits:
#     def __init__(self):
#         self.data = {}
#
#     def add(self, country, city):
#         city_set = self.data.setdefault(country, set())
#         city_set.add(city)
#
# visits = Visits()
# visits.add('Georgia', 'Tbilisi')
# print(visits.data)


from collections import defaultdict

class Visists:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visists()
visits.add('Paris', 'France')
print(visits.data)
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight}) '
#
# tools = [
#     Tool('level', 3.5),
#     Tool('hammer', 1.25),
#     Tool('screwdriver', 0.5),
#     Tool('chisel', 0.25),
# ]
#
# print(f'unsorted: {tools}')
# # print(tools.sort())
# tools.sort(key = lambda x:x.name)
# print(f'sorted by name: {tools}')
#
# tools.sort(key = lambda x:x.weight)
# print(f'sorted by weight: {tools}')


places = ['home', 'work', 'New York', 'Paris']

# places.sort()
# print('Case sensitive: ', places)
places.sort(key = lambda x:x.lower())
# print('Case insensitive: ', places)

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key = lambda x : (x.weight, x.name))
print(power_tools)

power_tools.sort(key = lambda x : (x.weight, x.name), reverse=True)
print(power_tools)

power_tools.sort(key = lambda x : (-x.weight, x.name))
print((power_tools))

power_tools.sort(key = lambda x:x.name)
power_tools.sort(key = lambda x:x.weight, reverse=True)
print((power_tools))
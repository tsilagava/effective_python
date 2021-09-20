counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

key = 'wheat'

# if key in counters:
#     count = counters[key]
# else:
#     count = 0
#
#
# counters[key] = count + 1
#
# print(counters)

# try:
#     count = counters[key]
# except KeyError:
#     count = 0
# counters[key] = count + 1

# count = counters.get(key, 0)
# counters[key] = count + 1

votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

# if key in votes:
#     names = votes[key]
# else:
#     votes[key] = names = []
#
# names.append(who)
#
# print(votes)

# try:
#     names = votes[key]
# except KeyError:
#     votes[key] = names = []
#
# names.append(who)
#
# print(votes)

# names = votes.get(key)
# if names is None:
#     votes[key] = names = []
# names.append(who)
#
# print(votes)

# if (names := votes.get(key)) is None:
#     votes[key] = who
#
# print(votes)

names = votes.setdefault(key, [])
names.append(who)

print(votes)
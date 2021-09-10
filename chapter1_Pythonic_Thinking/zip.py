names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count


print(longest_name)

names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)

import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
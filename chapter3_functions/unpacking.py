lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

minimum, maximum = get_stats(lengths)
print(f'min: {minimum}, max: {maximum}')

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)

print(f'longest: {longest:>4.0%}, shortest: {shortest:>4.0%}')
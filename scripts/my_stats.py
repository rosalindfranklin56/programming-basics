def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def count_above(numbers, limit):
    count = 0
    for n in numbers:
        if n > limit:
            count = count + 1
    return count
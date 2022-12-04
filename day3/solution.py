import string


def part1(input) -> int:
    total = 0
    with open(input) as f:
        for l in f:
            intersection = set(l[: len(l) // 2]).intersection(l[len(l) // 2 :])
            total += string.ascii_letters.index(min(intersection)) + 1
    return total


def part2(input) -> int:
    listed = []
    total = 0
    with open(input) as f:
        for l in f:
            listed.append(l.strip())
        for i in range(3, len(listed) + 3, 3):
            intersection = set(listed[i - 3]) & set(listed[i - 2]) & set(listed[i - 1])
            total += string.ascii_letters.index(min(intersection)) + 1
    return total

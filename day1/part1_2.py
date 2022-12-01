calories = []
with open("./day1/input.txt", "r") as f:
    elve = 0
    for line in f:
        if not line.strip():
            calories.append(elve)
            elve = 0
        if line.strip():
            elve += int(line.strip())


calories = sorted(calories, reverse=True)
print(sum(calories[:3]))

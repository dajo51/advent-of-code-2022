def part1(input) -> int:
    total = 0
    with open(input) as f:
        for l in f:
            splitted = l.strip().split(",")
            first_elve = set(
                range(
                    int(splitted[0].split("-")[0]), int(splitted[0].split("-")[1]) + 1
                )
            )
            second_elve = set(
                range(
                    int(splitted[1].split("-")[0]), int(splitted[1].split("-")[1]) + 1
                )
            )
            if first_elve <= second_elve or second_elve <= first_elve:
                total += 1
    return total


def part2(input) -> int:
    total = 0
    with open(input) as f:
        for l in f:
            splitted = l.strip().split(",")
            first_elve = set(
                range(
                    int(splitted[0].split("-")[0]), int(splitted[0].split("-")[1]) + 1
                )
            )
            second_elve = set(
                range(
                    int(splitted[1].split("-")[0]), int(splitted[1].split("-")[1]) + 1
                )
            )
            if first_elve.intersection(second_elve) or second_elve.intersection(
                first_elve
            ):
                total += 1
    return total

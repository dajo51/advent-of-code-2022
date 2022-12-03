import string

points = 0
with open("./day2/input.txt", "r") as f:
    index = 0
    for line in f:
        splitted = line.strip().split()
        player1 = string.ascii_uppercase.index(splitted[0]) + 1
        player2 = string.ascii_uppercase.index(splitted[1]) - 22
        print(player1, player2)
        if player1 < player2:
            points += 6 + player2
        elif player1 == player2:
            points += 3 + player2
        else:
            points += player2
        if index > 5:
            break
        print(points)
        index += 1

print(string.ascii_uppercase.index("C") + 1)

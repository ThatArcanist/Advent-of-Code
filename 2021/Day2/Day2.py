movements = open("Day2input.txt", "r").readlines()

# Question 1
depth = 0
horizontal = 0

for move in movements:
    move = move.split(" ")
    if(move[0] == "forward"):
        horizontal += int(move[1])
    if(move[0] == "down"):
        depth += int(move[1])
    if(move[0] == "up"):
        depth -= int(move[1])

print(depth * horizontal)

# Question 2
aim = 0
depth = 0
horizontal = 0

for move in movements:
    move = move.split(" ")
    if(move[0] == "forward"):
        horizontal += int(move[1])
        depth += aim * int(move[1])
    if(move[0] == "down"):
        aim += int(move[1])
    if(move[0] == "up"):
        aim -= int(move[1])

print(depth * horizontal)
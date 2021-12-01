# Question 1
radarOutput = open("Day1input.txt", "r").readlines()
lines = sum(1 for line in  open("Day1input.txt", "r"))

first = -1
second = -1

total = 0

for line in radarOutput:
    second = int(line)
    if second > first and first != -1:
        total += 1
    first = second
    
print(total)

# Question 2
total = 0
currentLine = 0
window = -1
lastWindow = -1

for line in radarOutput:
    if currentLine == 0:
        window = (int(radarOutput[0]) + int(radarOutput[1]) + int(radarOutput[2]))
        print(window)
        lastWindow = window
        currentLine += 1
    elif (currentLine + 2) > lines:
        break
    else:
        window = int(radarOutput[currentLine - 1]) + int(radarOutput[currentLine]) + int(radarOutput[currentLine + 1])
        if window > lastWindow:
            total += 1
        lastWindow = window
        currentLine += 1
print(total)
        
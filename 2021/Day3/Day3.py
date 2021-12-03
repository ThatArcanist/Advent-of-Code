lines = open("Day3input.txt", "r").readlines()

def resetInput(lines):
    splitLines = []
    for line in lines:
        line = line.replace('\n', '')
        line = list(line)
        splitLines.append(line)
    return splitLines

# question 1
splitLines = resetInput(lines)

ones = 0
zeros = 0
highBit = ""
lowBit = ""

for i in range(0, len(splitLines[0])):
    for line in splitLines:
        if line[i] == "0":
            zeros += 1
        if line[i] == "1":
            ones += 1
    if zeros > ones:
        highBit += "0"
        lowBit += "1"
    else:
        highBit += "1"
        lowBit += "0"
    zeros = 0
    ones = 0

highBitInt = int(highBit, 2)
lowBitInt = int(lowBit, 2)
print(highBitInt * lowBitInt)

# Question 2
# Oxygen
splitLines = resetInput(lines)

for i in range(0, len(splitLines[0])):
    if(len(splitLines) < 2):
        break
    
    zeros = [line for line in splitLines if line[i] == "0"]
    ones = [line for line in splitLines if line[i] == "1"]

    if len(zeros) > len(ones):
        splitLines = [line for line in splitLines if line[i] == "0"]
    else:
        splitLines = [line for line in splitLines if line[i] == "1"]

oxy = splitLines

#Carbon
splitLines = resetInput(lines)

for i in range(0, len(splitLines[0])):
    if(len(splitLines) < 2):
        break
    
    zeros = [line for line in splitLines if line[i] == "0"]
    ones = [line for line in splitLines if line[i] == "1"]

    if len(zeros) <= len(ones):
        splitLines = [line for line in splitLines if line[i] == "0"]
    else:
        splitLines = [line for line in splitLines if line[i] == "1"]

carbon = splitLines

oxy = ''.join(oxy[0])
carbon = ''.join(carbon[0])
print(int(oxy, 2) * int(carbon, 2))

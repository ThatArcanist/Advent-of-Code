import re

class Board:

    def __init__(self):
        self.board = []

    def showBoard(self):
        for row in self.board:
            print("".join(row))
        print(" ")

    def checkNumber(self, input):
        for i in range (0, len(self.board)):
            for number in self.board[i]:
                if number == input:
                    # row = [n.replace(input, "X") for n in self.board[i]]
                    row = [n.replace(input, "X") if n == input else n for n in self.board[i]]
                    self.board[i] = row

    def checkWin(self):
        bingo = True
        # Check Horizontal
        for row in self.board:
            for number in row:
                if number != "X":
                    bingo = False
            if bingo == True:
                return True
            else:
                bingo = True


        # Check Vertical
        rowSize = len(self.board[0])
        for i in range(0, rowSize):
            for row in self.board:
                if row[i] != "X":
                    bingo = False
            if bingo == True:
                return True
            else:
                bingo = True

        return False

def parseInput():
    input = open("Day4input.txt", "r")
    lines = input.readlines()

    # Read numbers
    numbers = lines.pop(0)
    numbers = numbers.split(",")

    # Remove an extra space
    lines.pop(0)

    # Create Boards
    boards = []
    newBoard = Board()

    for line in lines:
        line.strip()
        line = " ".join(line.split())
        # line = re.sub(" +", " ", line)
        # line = line.replace("\n", "")
        
        if line == "":
            boards.append(newBoard)
            newBoard = Board()
            continue
        else:
            line = line.split(" ")
            newBoard.board.append(line)

    return numbers, boards

# Question 1
input = parseInput()
numbers = input[0]
boards = input[1]
winner = False

for number in numbers:
    for board in boards:
        board.checkNumber(number)
        if board.checkWin() == True:
            
            #Count remaining numbers
            totalLeft = 0
            for row in board.board:
                for num in row:
                    if num != "X":
                        totalLeft += int(num)

            print (totalLeft * int(number))
            winner = True

        if winner == True:
            break

    if winner == True:
        break

# Question 2
input = parseInput()
numbers = input[0]
boards = input[1]
winners = []
lastWinner = Board()
lastNumber = 0
loser = False

for number in numbers:
    i = 0
    winners = []
    for board in boards:
        board.checkNumber(number)
        if board.checkWin() == True:
            lastWinner = boards[i]
            lastNumber = int(number)
            winners.append(int(i))
        if len(boards) < 1:
            loser = True
            break
        i += 1
    if len(winners) > 0:
            for winnerNum in sorted(winners, reverse=True):
                boards.pop(winnerNum)
    if loser:
        break
    

#Count remaining numbers
totalLeft = 0
for row in lastWinner.board:
    for num in row:
        if num != "X":
            totalLeft += int(num)

print (totalLeft * int(lastNumber))

            
            
                
                

        


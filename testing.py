from random import randint

def print_board(board):
  for row in board:
    print(" ".join(row))

def check_board_limit(coord, boardsize):
  if (coord < 0) or (coord >= boardsize):
    return False
  else:
    return True

def check_overlap(startingPoint, size, direction, board):
  if size == 5:
  	return True
  currentRow = startingPoint[0]
  currentCol = startingPoint[1]
  for i in range(size):
    if((board[currentRow][currentCol] == "|") or(board[currentRow][currentCol] == "-")):
      return False
    else:
      if(direction == 0):
      	currentRow -= 1
      elif(direction == 1):
      	currentRow += 1
      elif(direction == 2):
      	currentCol -= 1
      else:
      	currentCol += 1
  return True

def create_ship(ship, boardlength, board):
  shiplength = 0
  if(ship == 0):
    shiplength = 5
  elif(ship == 1):
    shiplength = 4
  elif(ship == 4):
    shiplength = 2
  else:
    shiplength = 3

  ## Choose a starting point for the Carrier
  startingPoint = [randint(0, boardlength-1), randint(0, boardlength-1)]
  print("Starting point = (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")" )

  ## Now let's randomly choose if it's going up(0), down(1), left(2) or right(3)
  direction = randint(0, 3)

  ## Check if we stay within the limits, going on that direction, otherwise pick another direction
  invalidDirection = True
  directionsTried = 0
  while invalidDirection and directionsTried < 4:
    ## Going upwards
    if direction == 0:
      endingPoint = startingPoint[0] - (shiplength - 1)
    
      ## Check if the finish point would be within the grid 
      if(check_board_limit(endingPoint, boardlength) and check_overlap(startingPoint, shiplength, direction, board)):
        currentPoint = startingPoint
        print("Going up from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")
      
        ## If the boat fits, put it in
        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "|"
          print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[0] -= 1
      
        ## and break off the loop
        invalidDirection = False
    
      ## If boat doesn't fit, move to the "next" direction
      ## Also clear the "endingPoint" back to the starting point
      else:
        direction = 1
        directionsTried += 1

    ## Going downwards
    if direction == 1:
      endingPoint = startingPoint[0] + (shiplength - 1)

      if(check_board_limit(endingPoint, boardlength) and check_overlap(startingPoint, shiplength, direction, board)):
        currentPoint = startingPoint
        print("Going down from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "|"
          print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[0] += 1

        invalidDirection = False

      else:
        direction = 2
        directionsTried += 1

    ## Going left
    if direction == 2:
      endingPoint = startingPoint[1] - (shiplength - 1)

      if(check_board_limit(endingPoint, boardlength) and check_overlap(startingPoint, shiplength, direction, board)):
        currentPoint = startingPoint
        print("Going left from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "-"
          print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[1] -= 1

        invalidDirection = False

      else:
        direction = 3
        directionsTried += 1

    ## Going right
    if direction == 3:
      endingPoint = startingPoint[1] + (shiplength - 1)

      if(check_board_limit(endingPoint, boardlength) and check_overlap(startingPoint, shiplength, direction, board)):
        currentPoint = startingPoint
        print("Going right from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "-"
          print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[1] += 1

        invalidDirection = False

      else:
        direction = 0
        directionsTried += 1
  if directionsTried >= 4:
    create_ship(ship, boardlength, board)

## Creating empty boards for the computer
shipboard_AI = []
trackboard_AI = []

boardlength = 10

for x in range(boardlength):
  shipboard_AI.append(["O"] * boardlength)
  trackboard_AI.append(["O"] * boardlength)

for ship in range(5):
  create_ship(ship, boardlength, shipboard_AI)

print_board(shipboard_AI)
## Python Battleship ##
## by José Flores

## In battleship there are 5 ships: 
##   Ship Name   |   Size
##    Carrier    |    5
##   Battleship  |    4
##    Cruiser    |    3
##   Submarine   |    3
##   Destroyer   |    2

## These ships can be arranged either horizontally or vertically, without overlapping
## This game will let you play versus an "AI" (although not really, not using any AI-related algorithms)
## You will choose where to place your ships, the computer's will be placed randomly, according to the rules.
## You will have a board with your ships, where you can track where the computer has attacked
## You will also have a "tracking" board, to keep track of where you have attacked

####################################################################################################################
from random import randint
import os
import time
### FUNCTIONS ###

def print_board(board):
  counter = 0
  print("\\ 0 <---COLUMNS---> 9")
  for row in board:
    if counter == 0:
      print("0 " + " ".join(row))
    elif counter == 1:
      print("^ " + " ".join(row))
    elif (counter == 2) or (counter == 7):
      print("| " + " ".join(row))
    elif counter == 3:
      print("R " + " ".join(row))
    elif counter == 4:
      print("O " + " ".join(row))
    elif counter == 5:
      print("W " + " ".join(row))
    elif counter == 6:
      print("S " + " ".join(row))
    elif counter == 8:
      print("v " + " ".join(row))
    elif counter == 9:
      print("9 " + " ".join(row))
    #print(" ".join(row))
    counter += 1

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def check_board_limit(coord, boardsize):
  if (coord < 0) or (coord >= boardsize):
    return False
  else:
    return True

## This function checks that the boat that is being placed does not overlap with existing boats
def check_overlap(startingPoint, size, direction, board):
  ## If it's the first boat, it won't overlap with any other boats
  if size == 5:
    return True
  ## Storing the current points as separate integers because I was having problems using lists
  currentRow = startingPoint[0]
  currentCol = startingPoint[1]

  ## Check if the spot is taken
  for i in range(size):
    if((board[currentRow][currentCol] == "|") or (board[currentRow][currentCol] == "-")):
      return False
      ## If the spot is not taken iterate until either a spot is taken or there's no more ship to check
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

def check_possible_directions(startingPoint, size, board, boardsize):
  endingPoints = {
  0: [startingPoint[0]-(size-1), startingPoint[1]],
  1: [startingPoint[0]+(size-1), startingPoint[1]],
  2: [startingPoint[0], startingPoint[1]-(size-1)],
  3: [startingPoint[0], startingPoint[1]+(size-1)]
  }
  if((check_board_limit(endingPoints[0][1], boardsize) is True) and (check_overlap(startingPoint, size, 0, board) is True)):
    return True
  elif((check_board_limit(endingPoints[1][1], boardsize) is True) and (check_overlap(startingPoint, size, 1, board) is True)):
    return True
  elif((check_board_limit(endingPoints[2][2], boardsize) is True) and (check_overlap(startingPoint, size, 2, board) is True)):
    return True
  elif((check_board_limit(endingPoints[3][2], boardsize) is True) and (check_overlap(startingPoint, size, 3, board) is True)):
    return True
  else:
    return False

def place_ship(startingPoint, size, direction, board):
  currentPoint = startingPoint
  shippy = ""
  if (direction == 0) or (direction == 1):
    shippy = "|"
  else:
    shippy = "-"
  for i in range(size):
    board[currentPoint[0]][currentPoint[1]] = shippy
    if (direction == 0):
      currentPoint[0] -= 1
    elif (direction == 1):
      currentPoint[0] += 1
    elif (direction == 2):
      currentPoint[1] -= 1
    else:
      currentPoint[1] += 1


## This function will be used in creating the ships for the AI
def create_ship(ship, boardlength, board):
  ## Determine the size of the ship based on which ship it is
  shiplength = 0
  if(ship == 0):
    shiplength = 5
  elif(ship == 1):
    shiplength = 4
  elif(ship == 4):
    shiplength = 2
  else:
    shiplength = 3

  ## Choose a starting point for the ship
  startingPoint = [randint(0, boardlength-1), randint(0, boardlength-1)]
  #print("Starting point = (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")" )

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
        #print("Going up from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")
      
        ## If the ship fits, put it in
        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "|"
          #print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[0] -= 1
      
        ## and break off the loop
        invalidDirection = False
    
      ## If ship doesn't fit, move to the "next" direction
      ## Also clear the "endingPoint" back to the starting point
      ## Aaaand add 1 to the amount of directions tried
      else:
        direction = 1
        directionsTried += 1

    ## Going downwards
    if direction == 1:
      endingPoint = startingPoint[0] + (shiplength - 1)

      if(check_board_limit(endingPoint, boardlength) and check_overlap(startingPoint, shiplength, direction, board)):
        currentPoint = startingPoint
        #print("Going down from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "|"
          #print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
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
        #print("Going left from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "-"
          #print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
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
        #print("Going right from, (" + str(startingPoint[0]) + ", " + str(startingPoint[1]) + ")")

        for i in range(shiplength):
          shipboard_AI[currentPoint[0]][currentPoint[1]] = "-"
          #print("Placed ship part on point (" + str(currentPoint[0]) + ", " + str(currentPoint[1]) + ")")
          currentPoint[1] += 1

        invalidDirection = False

      else:
        direction = 0
        directionsTried += 1
  if directionsTried >= 4:
    create_ship(ship, boardlength, board)

####################################################################################################################
os.system('cls')
boardlength = 10

## Creating empty boards for the computer
shipboard_AI = []
trackboard_AI = []


for x in range(boardlength):
  shipboard_AI.append(["O"] * boardlength)
  trackboard_AI.append(["O"] * boardlength)

## Let's place the ships for the computer by descending size
for ship in range(5):
  create_ship(ship, boardlength, shipboard_AI)

#print_board(shipboard_AI)
## Now that the computer has its ships all set up, let's make the user place the boats
shipboard_user = []
trackboard_user = []

## Temporarily fill the user's boards
for x in range(boardlength):
  shipboard_user.append(["0"] * boardlength)
  trackboard_user.append(["0"] * boardlength)

## Defining a dictionary with the ship's info, this can be used before as well
ship_dict = {
  0: ['Carrier', 5],
  1: ['Battleship', 4],
  2: ['Cruiser', 3],
  3: ['Submarine', 3],
  4: ['Destroyer', 2]
}

print("Computer's board is set up. Choose where you wanna place your ships.")
time.sleep(2)
for i in range(5):
  row = -1
  column = -1
  direction = -1
  cancelInput = True

  while (cancelInput is True):
    cancelInput = False
    ## Get the starting points for the ship and validate
    invalid = True
    while (invalid is True):
      row = -1
      column = -1
      os.system('cls')
      print("Where do you want to set up your " + str(ship_dict[i][0]) + "? (it takes up " + str(ship_dict[i][1]) + " spaces)")
      print("")
      print_board(shipboard_user)
      print("")
      print("Starting point: ")
      row = int(input("Row: "))
      column = int(input("Column: "))
      if (check_board_limit(row, boardlength) is False) or (check_board_limit(column, boardlength) is False):
        print("Invalid selection, select another point")
        time.sleep(2)
      elif (shipboard_user[row][column] == "|") or (shipboard_user[row][column] == "-"):
        print("There's already part of a ship at that point, select another point")
        time.sleep(2)
      elif (check_possible_directions([row, column], ship_dict[i][1], shipboard_user, boardlength) is False):
        print("This ship won't fit in any direction, from this point, select another point")
        time.sleep(2)
      else:
        invalid = False

    ## Get the direction the user wants the ship to go
    while (direction < 0) or (direction > 4):
      direction = -1
      direction = int(input("What direction do you want the ship to go? (0 = up, 1 = down, 2 = left, 3 = right, 4 = choose a different starting point):\n"))
      if (direction < 0) or (direction > 4):
        print("Invalid input")
        time.sleep(2)
      elif (direction == 4):
        cancelInput = True
      elif (direction == 0):
        if (check_board_limit(row-(ship_dict[i][1]-1), boardlength) is True):
          if (check_overlap([row, column], ship_dict[i][1], direction, shipboard_user) is True):
            place_ship([row, column], ship_dict[i][1], direction, shipboard_user)
          else:
            print("Ship would overlap with another ship in that direction")
            time.sleep(2)
            direction = -1
        else:
          print("Ship would go out of the board in that direction")
          direction = -1
      elif (direction == 1):
        if (check_board_limit(row+(ship_dict[i][1]-1), boardlength) is True): 
          if (check_overlap([row, column], ship_dict[i][1], direction, shipboard_user) is True):
            place_ship([row, column], ship_dict[i][1], direction, shipboard_user)
          else:
            print("Ship would overlap with another ship in that direction")
            time.sleep(2)
            direction = -1
        else:
          print("Ship would go out of the board in that direction")
          direction = -1
      elif (direction == 2):
        if (check_board_limit(column-(ship_dict[i][1]-1), boardlength) is True):
          if (check_overlap([row, column], ship_dict[i][1], direction, shipboard_user)):
            place_ship([row, column], ship_dict[i][1], direction, shipboard_user)
          else:
            print("Ship would overlap with another ship in that direction")
            time.sleep(2)
            direction = -1
        else:
          print("Ship would go out of the board in that direction")
          direction = -1
      elif (direction == 3):
        if (check_board_limit(column+(ship_dict[i][1]-1), boardlength) is True):      
          if (check_overlap([row, column], ship_dict[i][1], direction, shipboard_user)):  
            place_ship([row, column], ship_dict[i][1], direction, shipboard_user)
          else:
            print("Ship would overlap with another ship in that direction")
            time.sleep(2)
            direction = -1
        else:
          print("Ship would go out of the board in that direction")
          direction = -1
      else:
        print("something broked")
        time.sleep(2)

print("   _____          __  __ ______    _____ _______       _____ _______ _____ _   _  _____") 
print("  / ____|   /\   |  \/  |  ____|  / ____|__   __|/\   |  __ \__   __|_   _| \ | |/ ____|")
print(" | |  __   /  \  | \  / | |__    | (___    | |  /  \  | |__) | | |    | | |  \| | |  __ ")
print(" | | |_ | / /\ \ | |\/| |  __|    \___ \   | | / /\ \ |  _  /  | |    | | | . ` | | |_ |")
print(" | |__| |/ ____ \| |  | | |____   ____) |  | |/ ____ \| | \ \  | |   _| |_| |\  | |__| |")
print("  \_____/_/    \_\_|  |_|______| |_____/   |_/_/    \_\_|  \_\ |_|  |_____|_| \_|\_____|")
                                                                                        
                                                                                        
time.sleep(2)
os.system('cls')
print("YOUR TURN!")
print("Your board:")
print_board(shipboard_user)
print("")
print("Your moves:")
print_board(trackboard_user)
print("H = Hit")
print("M = Miss")




# # Everything from here on should go in your for loop!
# # Be sure to indent four spaces!
# for turn in range(4):
#   print "Turn #", turn+1
#   guess_row = int(raw_input("Guess Row: "))
#   guess_col = int(raw_input("Guess Col: "))

#   if guess_row == ship_row and guess_col == ship_col:
#     print "Congratulations! You sunk my battleship!"
#     break
#   else:
#     if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
#       print "Oops, that's not even in the ocean."
#     elif(board[guess_row][guess_col] == "X"):
#       print "You guessed that one already."
#     else:
#       print "You missed my battleship!"
#       board[guess_row][guess_col] = "X"
#     # Print (turn + 1) here!
#     print_board(board)
    
#     if turn == 3:
#       print "Game Over"
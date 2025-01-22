board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
currentPlayer = "X"
winner = None
gameRunning = True

# Beilegendes Spielbrett generieren
def printBoard(board):
    print("┌───┬───┬───┐")
    print(f"│ {board[0]} │ {board[1]} │ {board[2]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[3]} │ {board[4]} │ {board[5]} │")
    print("├───┼───┼───┤")
    print(f"│ {board[6]} │ {board[7]} │ {board[8]} │")
    print("└───┴───┴───┘")

# Spielereingaben
def playerInput(board):
    global currentPlayer
    while True:
        inp = input(f"Enter a number 1-9 Player (X)  " if currentPlayer == "X" else f"Enter a number 1-9  Player (O)  ")
        if inp.lower() == 'restart':
            restartGame()
            return
        elif inp.lower() == 'end':
            endGame()
            return
        elif inp.isdigit():
            inp = int(inp)
            if 1 <= inp <= 9 and board[inp - 1].isdigit():
                board[inp - 1] = currentPlayer
                break
            else:
                print("Invalid move, try again!")
        else:
            print("Invalid input, try again!")

# Spielwiederholen
def restartGame():
    global board, currentPlayer, winner, gameRunning
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    currentPlayer = "X"
    winner = None
    gameRunning = True
    print("Game restarted!")

#Spielend
def endGame():
    global gameRunning
    gameRunning = False
    print("Game ended. Thanks for playing!")
    exit()

# Überprüfen ob es einen Sieger gibt
# Horizontal
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i].isalpha():
            winner = currentPlayer
            return True
    return False

# Vertikal
def checkVertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i].isalpha():
            winner = currentPlayer
            return True
    return False

# Diagonal/Kreuz 
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0].isalpha()) or \
       (board[2] == board[4] == board[6] and board[2].isalpha()):
        winner = currentPlayer
        return True
    return False

def checkWin():
    return checkHorizontal(board) or checkVertical(board) or checkDiagonal(board)

# Unentschieden überprüfen 
def checkTie(board):
    if all(cell.isalpha() for cell in board) and winner is None:
        print("It's a tie!")
        return True
    return False

# Spielerwechseln
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

#Hauptloop
def main():
    global gameRunning
    while gameRunning:
        printBoard(board) 
        playerInput(board)  
        if checkWin(): 
            printBoard(board)  #
            print(f"The winner is {currentPlayer}") 
            while True:
                restart = input('Do you want to restart? (Y/N): ').lower()
                if restart == 'y':
                    restartGame()
                    break
                elif restart == 'n':
                    endGame()
                else:
                    print("Invalid input, try again.")

        elif checkTie(board):
            printBoard(board)  
            print("It's a tie!")  
            while True:
                restart = input('Do you want to restart? (Y/N): ').lower()
                if restart == 'y':
                    restartGame()
                    break
                elif restart == 'n':
                    gameRunning = False  
                    break
                else:
                    print("Invalid input, try again.")

        else:
            switchPlayer()

if __name__ == "__main__":
    main()

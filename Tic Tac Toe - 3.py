def print_board():  # creating function display game board
    global board  # making board list global to use all over the program
    print("\n\n\n\tTIC TAC TOE\n")  # title to code
    print("     |     |")
    print("  " + board[0] + "  |  " + board[1] +
          "  |  " + board[2])  # printing
    # of board
    print("     |     |")
    # with player's
    print("-----------------")
    # game symbols
    print("     |     |")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("     |     |")


def player1_input():  # creating function to get player 1 value
    player1 = " "  # first empty the variable where you gonna store value
    # this while run until user input right value (1 - 9) as well as checks there is no overwriting on board
    while player1 not in "1 2 3 4 5 6 7 8 9".split() or not space_check(int(player1)):
        # user input: raw_input
        player1 = input(
            "Player 1: Choose Where To Place Your Mark 'O' 1 - 9 : ")
    # assigning player 1 symbol to the position which is inputted by the player
    board[int(player1)-1] = "O"


def player2_input():  # creating function to get player 2 value
    player2 = " "  # same as above player 1 input function
    # same as above player 1 input function
    while player2 not in "1 2 3 4 5 6 7 8 9".split() or not space_check(int(player2)):
        # same as above player 1 input function
        player2 = input(
            "Player 2: Choose Where To Place Your Mark 'X' 1 - 9 : ")
    board[int(player2)-1] = "X"  # same as above player 1 input function


def retry():  # creating retry function to play again choice
    if ((board[0] == "O" or board[0] == "X") and (board[1] == "O" or board[1] == "X") and (board[2] == "O" or board[2] == "X") and (board[3] == "O" or board[3] == "X") and (board[4] == "O" or board[4] == "X") and (board[5] == "O" or board[5] == "X") and (board[6] == "O" or board[6] == "X") and (board[7] == "O" or board[7] == "X") and (board[8] == "O" or board[8] == "X")):  # checking is board is full
        if match_draw:  # if above condition and this condition true it mean's board is full as well as match_draw is true then there'll will Match Draw
            print("\n\t MATCH DRAW")
        re = " "  # making replay (re) variable empty
        while re not in "Y N y n".split():  # this while run until user input Y y N n
            # user inout to play again
            re = input("Do You Want To Play Again (Y/N) : ")
        if (re == "Y") or (re == "y"):  # excute when user input Y or y
            global game_on  # making game_on variable global to use all over the program
            game_on = False  # assigning game_on False to destroy current game process
        elif (re == "N") or (re == "n"):  # excute when user input N or n
            print("\n\tThanks For Play")  # exit banner
            exit()  # exit funtion to stop program
        else:
            pass
    else:
        pass


def win_lose():  # defining function to check player's win or lose
    global match_draw
    if ((board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O")):  # checking is player 1 win by all combination of winning
        # wining banner of Player 1
        print("\n\tCongratulation! Player 1 is the WINNER of Match...")
        match_draw = False  # making match_draw variable False
        for i in range(0, 9):  # filling board with "O" so retry fucntion excute
            board[i] = "O"
    elif((board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X")):  # same as for player 2
        # same as player 1
        print("\n\tCongratulation! Player 2 is the WINNER of Match...")
        match_draw = False  # same as player 1
        for i in range(0, 9):  # same as player 1
            board[i] = "X"


def space_check(position):  # checking is board block is empty as given position or index
    return board[position-1] == ' '


while True:  # starting point of program : excute infinity
    match_draw = True
    game_on = True
    board = [" "]*9  # destroying all the previous values of boards

    while game_on:  # run until game_on is equals to False
        clear = "\n" * 100  # to make python console clear
        print(clear)
        print_board()
        win_lose()
        retry()
        if game_on == False:
            break
        player1_input()
        print(clear)
        print_board()
        win_lose()
        retry()
        if game_on == False:
            break
        player2_input()
        print(clear)
        print_board()
        win_lose()
        retry()
        if game_on == False:
            break  # End of prgram

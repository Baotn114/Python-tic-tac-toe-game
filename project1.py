import random
test_board = ['#','X','O','X','O','X','O','X','O','X'] # board to test function

#### Display board ####

def display_board(board):
    print("_________________")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("_________________")
    

# display_board(test_board)


#### Input Player ####

def player_input():
    cont = True
    while cont:
        choice = input("Choose your X or O: ")
        
        if choice == "X" or choice == "O":
            cont = False
    return choice
        
# player_input()

#### Place Marker ####

def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)


#### Win check ####

def win_check(board, mark):
    return (board[7] == board[8] == board[9] == mark or
            board[7] == board[5] == board[3] == mark or
            board[7] == board[4] == board[1] == mark or
            board[4] == board[5] == board[6] == mark or 
            board[1] == board[2] == board[3] == mark or
            board[1] == board[5] == board[9] == mark or
            board[8] == board[5] == board[2] == mark or
            board[9] == board[6] == board[3] == mark)

# print(win_check(test_board, 'O'))


#### Randomly choose players ####

def choose_first():
    num = random.randint(1, 2)
    return num

# print(choose_first())

#### Space Check ####

def space_check(board, position):
    return board[position] == ' '

# print(space_check(test_board, 9))


#### Full board check ####

def full_board_check(board):
    for item in board:
        if item == ' ':
            return False # False if the board not full
    return True # True if the board is full

# print(full_board_check(test_board))

#### Player Choice ####

def player_choice(board):
    choice = 'Wrong'
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Postion (1 - 9): ")
        if choice.isdigit() == False:
            print("Please choose a digit in 1 - 9")
            
        if choice.isdigit() == True:
            if int(choice) not in range(1, 10):
                # print("Please choose a number between 1 and 9")
                within_range = False
            else:
                within_range = True
                
    num = int(choice)
    
    if space_check(board, num):
        return num
    else:
        return False
    

# # print(player_choice(test_board))
# player_choice(test_board)

#### Replay ####

def replay():
    cont = True
    
    while cont == True:
        choice = input("Do you want to play again? (y or n): ")
        if choice not in ['y', 'n']:
            print("Please choose only y or n")
            cont = True
        elif choice in ['y', 'n']:
            if choice == 'y':
                cont = False
                return True
            else:
                cont = False
                return False    
    
print('Welcome to Tic Tac Toe!')

while True:
    board_game = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    player1_marker = player_input() #player 1 choose marker
    player2_marker = player_input() #player 2 choose marker
    
    choice = input("Do you want to play? y or n: ")
    
    if choice == 'y':
        game_on = True
    else:
        game_on = False
    
    turn = choose_first()
    while game_on:
        print("Player " + str(turn) + " goes")
        if turn == 1: #player1 goes
            #here is the turn = 1 rerun again if the turn is reassign as number 1 (turn = 1)
            display_board(board_game)
            position = player_choice(board_game)
            if position != False:
                place_marker(board_game, player1_marker, position)
                display_board(board_game)
                if win_check(board_game, player1_marker):
                    print("Player 1 wins!")
                    game_on = False
                elif full_board_check(board_game):
                        print("The game is draw!")
                        game_on = False
                else:
                    turn = 2
            elif position == False:
                print("Please choose another position!")
                turn = 1
                
        elif turn == 2: #player2 goes 
            #here is the turn = 2 rerun again if the turn is reassign as number 2 (turn = 2)
            display_board(board_game)
            position = player_choice(board_game)
            if position != False:
                place_marker(board_game, player2_marker, position)
                display_board(board_game)
                if win_check(board_game, player2_marker):
                    print("Player 2 wins!")
                    game_on = False
                elif full_board_check(board_game):
                        print("The game is draw!")
                        game_on = False
                else:
                    turn = 1
            elif position == False: #if the position is not vacant, get the player 2 to choose again by assigning the turn = 2 again
                print("Please choose another position!")
                turn = 2
    
    if replay():
        game_on = True
    else:
        break
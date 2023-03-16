
import random

def choose_first():
    x = random.randint(1,2)
    if x == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def choose_next(player):
    if player=='Player 1':
        return 'Player 2'
    else:
        return 'Player 1'
    
def display_board(board):
    
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(f'-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        marker = marker.upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return(player1,player2)

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    if board[1]+board[2]+board[3] == mark*3:
        return True
    elif board[4]+board[5]+board[6] == mark*3:
        return True
    elif board[7]+board[8]+board[9] == mark*3:
        return True
    elif board[1]+board[4]+board[7] == mark*3:
        return True
    elif board[2]+board[5]+board[8] == mark*3:
        return True
    elif board[3]+board[6]+board[9] == mark*3:
        return True
    elif board[1]+board[5]+board[9] == mark*3:
        return True
    elif board[3]+board[5]+board[7] == mark*3:
        return True
    else:
        return False
    
def space_check(board, position):
    
    if board[position] == '' or board[position] == ' ':
        return True
    else:
        return False
    
def full_board_check(board):
    
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):

    while True:    
        pos = int(input("Enter position: "))
        if space_check(board, pos):
            return pos
        print('Position not available. Try again.')

def replay():
    
    x = input('Would you like to play again? Y/N: ')
    if x == 'Y' or x == 'y':
        return True
    return False

print('Welcome to Tic Tac Toe!')

while True:
    #Set the game up here
    game_board = [' ']*10
    player1,player2 = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    display_board(game_board)


    while game_on:
        #Set marker for player
        if turn == 'Player 1':
            marker = player1
        else:
            marker = player2
            
        print(turn)
        pos = player_choice(game_board)
        place_marker(game_board,marker,pos)
        print('\n'*12)
        display_board(game_board)
        if win_check(game_board,marker):
            print(f'{turn} is the winner!')
            break
        elif full_board_check(game_board):
            print('Tie Game!')
            break
        turn = choose_next(turn)

    if not replay():
        break
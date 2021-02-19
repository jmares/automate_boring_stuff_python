board = {
    'top_l': ' ', 'top_m': ' ', 'top_r': ' ',
    'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
    'low_l': ' ', 'low_m': ' ', 'low_r': ' '    
}

def print_board(board):
    print('   |   |   ')
    print(' ' + board['top_l'] + ' | ' + board['top_m'] + ' | ' + board['top_r'])
    print('   |   |   ')
    print('---+---+---')
    print('   |   |   ')
    print(' ' + board['mid_l'] + ' | ' + board['mid_m'] + ' | ' + board['mid_r'])
    print('   |   |   ')
    print('---+---+---')
    print('   |   |   ')
    print(' ' + board['low_l'] + ' | ' + board['low_m'] + ' | ' + board['low_r'])
    print('   |   |   ')


turn = 'X'
for i in range(9):
    print_board(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

print_board(board)
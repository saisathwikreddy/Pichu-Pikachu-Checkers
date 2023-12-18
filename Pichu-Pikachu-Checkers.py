#
# Code by: Sai Sathwik Reddy Varikoti,
#          Bindu Madhavi Dokala,
#          Pranay Chowdary Namburi

import sys
import time
from copy import deepcopy

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def convert_string_to_board_matrix(board, N):
    return [[board[i + j] for j in range(N)] for i in range(0, len(board), N)]

def convert_board_matrix_to_string(board, N):
    return "".join(["".join([board[i][j] for j in range(N)]) for i in range(0, len(board))])

# To calculate the score of each board after a move is done
def score(player, pieces_dict):
    white_Pichus = 0
    white_Pikachus = 0
    white_Raichus = 0
    black_Pichus = 0
    black_Pikachus = 0
    black_Raichus = 0

    # Find the number of pieces of each colour and type
    for each_key in pieces_dict.keys():
            if(each_key == 'w'):
                white_Pichus += len(pieces_dict[each_key])

            elif(each_key == 'W'):
                white_Pikachus += len(pieces_dict[each_key])

            elif(each_key == '@'):
                white_Raichus += len(pieces_dict[each_key])

            elif(each_key == 'b'):
                black_Pichus += len(pieces_dict[each_key])

            elif(each_key == 'B'):
                black_Pikachus += len(pieces_dict[each_key])

            elif(each_key == '$'):
                black_Raichus += len(pieces_dict[each_key])

    # calculate the difference between player and opponent pieces
    # Find the power level by multiplying a piece with the number of directions it can move
    # Also multiply with the number of directions it can move
    temp_score = ((black_Pichus - white_Pichus) * 2) + (((black_Pikachus * 2) - (white_Pikachus * 2)) * 3)  + (((black_Raichus * 3) - (white_Raichus * 3)) * 8)
    if(player == 'b'):
        return temp_score
    
    else:
        return temp_score * -1

# To check if the player won or not
def gameWon(player, opponent, pieces_dict):
    for each_piece in opponent:
        if(each_piece in pieces_dict):
            if(len(pieces_dict[each_piece]) > 0):
                return False

    return True

# To get all white pichus moves'
def get_all_white_pichu_moves(board, N, pieces_dict):
    all_white_pichu_moves = []
    if('w' in pieces_dict):
        for x, y in pieces_dict['w']:
            possible_move_1 = None
            possible_move_2 = None

            # To check it we at the second last row, so that we can convert it to Raichu
            if(x == N - 2):
                # Can move to right only if it is before the last. 
                # If the piece is in last column it can't move right since it is the right most column.
                if(y < N - 1):
                    possible_move_1 = board[x + 1][y + 1]
                
                # Can move to left only if it is before the first column. 
                # If the piece is in first column it can't move left since it is the left most column.
                if(y > 0):
                    possible_move_2 = board[x + 1][y - 1]

                if(possible_move_1 is not None and possible_move_1 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x + 1][y + 1] = '@'
                    temp_pieces_dict['w'].remove((x, y))
                    if('@' in temp_pieces_dict):
                        temp_pieces_dict['@'].append((x + 1, y + 1))

                    else:
                        temp_pieces_dict['@'] = [(x + 1, y + 1)]
                    
                    all_white_pichu_moves.append((temp_board, temp_pieces_dict))

                if(possible_move_2 is not None and possible_move_2 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x + 1][y - 1] = '@'
                    temp_pieces_dict['w'].remove((x, y))
                    if('@' in temp_pieces_dict):
                        temp_pieces_dict['@'].append((x + 1, y - 1))

                    else:
                        temp_pieces_dict['@'] = [(x + 1, y - 1)]
                    
                    all_white_pichu_moves.append((temp_board, temp_pieces_dict))

            else:
                if(y < N - 1):
                    possible_move_1 = board[x + 1][y + 1]
                if(y > 0):
                    possible_move_2 = board[x + 1][y - 1]

                if(possible_move_1 is not None and possible_move_1 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x + 1][y + 1] = 'w'
                    temp_pieces_dict['w'].remove((x, y))
                    temp_pieces_dict['w'].append((x + 1, y + 1))
                    all_white_pichu_moves.append((temp_board, temp_pieces_dict))

                # If we have a opponent pichu, then we just kill and move too the next diagonal
                elif(possible_move_1 is not None and possible_move_1 == 'b'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    # So check if we have empty place to move after killing it,
                    # Or whether we have any piece blocking our move
                    if(y + 1 < N - 1 and  x + 1 < N - 1 and temp_board[x + 2][y + 2] == '.'):
                        temp_board[x][y] = '.'
                        if(x + 2 == N - 1):
                            temp_board[x + 2][y + 2] = '@'
                            if('@' in temp_pieces_dict):
                                temp_pieces_dict['@'].append((x + 2, y + 2))

                            else:
                                temp_pieces_dict['@'] = [(x + 2, y + 2)]

                        else:
                            temp_board[x + 2][y + 2] = 'w'
                            if('w' in temp_pieces_dict):
                                temp_pieces_dict['w'].append((x + 2, y + 2))

                            else:
                                temp_pieces_dict['w'] = [(x + 2, y + 2)]

                        temp_board[x + 1][y + 1] = '.'
                        temp_pieces_dict['b'].remove((x + 1, y + 1))
                        temp_pieces_dict['w'].remove((x, y))
                        all_white_pichu_moves.append((temp_board, temp_pieces_dict))

                # Similar logic as for move 1
                if(possible_move_2 is not None and possible_move_2 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x + 1][y - 1] = 'w'
                    temp_pieces_dict['w'].remove((x, y))
                    temp_pieces_dict['w'].append((x + 1, y - 1))
                    all_white_pichu_moves.append((temp_board, temp_pieces_dict))

                elif(possible_move_2 is not None and possible_move_2 == 'b'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    if(y - 1 > 0 and  x + 1 < N - 1 and temp_board[x + 2][y - 2] == '.'):
                        temp_board[x][y] = '.'
                        if(x + 2 == N - 1):
                            temp_board[x + 2][y - 2] = '@'
                            if('@' in temp_pieces_dict):
                                temp_pieces_dict['@'].append((x + 2, y - 2))

                            else:
                                temp_pieces_dict['@'] = [(x + 2, y - 2)]

                        else:
                            temp_board[x + 2][y - 2] = 'w'
                            if('w' in temp_pieces_dict):
                                temp_pieces_dict['w'].append((x + 2, y - 2))

                            else:
                                temp_pieces_dict['w'] = [(x + 2, y - 2)]

                        # print(temp_board)
                        # print(temp_pieces_dict)
                        temp_board[x + 1][y - 1] = '.'
                        temp_pieces_dict['b'].remove((x + 1, y - 1))
                        temp_pieces_dict['w'].remove((x, y))
                        all_white_pichu_moves.append((temp_board, temp_pieces_dict))

    return all_white_pichu_moves

# To get all white pikachus moves'
def get_all_white_pikachu_moves(board, N, pieces_dict):
    all_white_pikachu_moves = []
    if('W' in pieces_dict):
        for x,y in pieces_dict['W']:
            possible_moves_left = []
            possible_moves_right = []
            possible_moves_down= []

            # We can move upto 2 steps. So generating all the possible moves.
            # Then we check whether each step is valid or not
            for each_left_column_index in range(y - 1, max(y - 3, -1), -1):
                possible_moves_left.append((x, each_left_column_index))

            for each_right_column_index in range(y + 1, min(y + 3, N)):
                possible_moves_right.append((x, each_right_column_index))

            for each_down_row_index in range(x + 1, min(x + 3, N)):
                possible_moves_down.append((each_down_row_index, y))

            # Check for all the left steps
            for x_left, y_left in possible_moves_left:
                if(board[x_left][y_left] == '.'):
                    # check if it is one step ahead or two steps ahead
                    if(abs(y - y_left) > 1):
                        if(board[x_left][y_left + 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_left][y_left] = 'W'
                            temp_pieces_dict['W'].remove((x, y))
                            temp_pieces_dict['W'].append((x_left, y_left))
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_left][y_left + 1] in 'bB'):
                            if(y_left - 1 >= 0 and board[x_left][y_left - 1] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                temp_board[x_left][y_left - 1] = 'W'
                                temp_pieces_dict['W'].remove((x, y))
                                temp_pieces_dict[temp_board[x][y_left + 1]].remove((x_left, y_left + 1))
                                temp_board[x_left][y_left + 1] = '.'
                                temp_pieces_dict['W'].append((x_left, y_left - 1))
                                all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                            else: break

                        elif(board[x_left][y_left + 1] in 'wW@'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_board[x_left][y_left] = 'W'
                        temp_pieces_dict['W'].remove((x, y))
                        temp_pieces_dict['W'].append((x_left, y_left))
                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_left][y_left] in 'bB'):
                    # check if the opponent piece is one step ahead or two steps ahead
                    if(abs(y - y_left) > 1):
                        # If the next place after the opponent is empty or not
                        # Since the piece is two steps ahead,
                        # Then check if the space between the player and opponent is clear or not
                        if((board[x_left][y_left + 1] == '.') and (y_left - 1 >= 0) and board[x_left][y_left - 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_left][y_left - 1] = 'W'
                            temp_pieces_dict['W'].remove((x, y))
                            temp_pieces_dict[temp_board[x_left][y_left]].remove((x_left, y_left))
                            temp_board[x_left][y_left] = '.'
                            temp_pieces_dict['W'].append((x_left, y_left - 1))
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(y_left > 0 and board[x_left][y_left - 1] == '.'):
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_left][y_left]].remove((x_left, y_left))
                        temp_board[x_left][y_left] = '.'
                        temp_pieces_dict['W'].remove((x, y))
                        temp_board[x_left][y_left - 1] ='W'
                        temp_pieces_dict['W'].append((x_left, y_left - 1))
                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break

            # similar logic as left

            # Check for all the right steps
            for x_right, y_right in possible_moves_right:
                if(board[x_right][y_right] == '.'):
                    if(abs(y - y_right) > 1):
                        if(board[x_right][y_right - 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_right][y_right] = 'W'
                            temp_pieces_dict['W'].remove((x, y))
                            temp_pieces_dict['W'].append((x_right, y_right))
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_right][y_right - 1] in 'bB'):
                            if(y_right + 1 <= N - 1 and board[x_right][y_right + 1] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                temp_board[x_right][y_right + 1] = 'W'
                                temp_pieces_dict['W'].remove((x, y))
                                temp_pieces_dict[temp_board[x][y_right - 1]].remove((x_right, y_right - 1))
                                temp_board[x][y_right - 1] = '.'
                                temp_pieces_dict['W'].append((x_right, y_right + 1))
                                all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_right][y_right - 1] in 'wW@'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_board[x_right][y_right] = 'W'
                        temp_pieces_dict['W'].remove((x, y))
                        temp_pieces_dict['W'].append((x_right, y_right))
                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_right][y_right] in 'bB'):
                    if(abs(y - y_right) > 1):
                        if((board[x_right][y_right - 1] == '.') and (y_right + 1 <= N - 1) and board[x_right][y_right + 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_right][y_right + 1] = 'W'
                            temp_pieces_dict['W'].remove((x, y))
                            temp_pieces_dict[temp_board[x_right][y_right]].remove((x_right, y_right))
                            temp_board[x_right][y_right] = '.'
                            temp_pieces_dict['W'].append((x_right, y_right + 1))
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(y_right < N - 1 and board[x_right][y_right + 1] == '.'):
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_right][y_right]].remove((x_right, y_right))
                        temp_board[x_right][y_right] = '.'
                        temp_pieces_dict['W'].remove((x, y))
                        temp_board[x_right][y_right + 1] ='W'
                        temp_pieces_dict['W'].append((x_right, y_right + 1))
                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break

            # Check for all the down steps
            for x_down, y_down in possible_moves_down:
                if(board[x_down][y_down] == '.'):
                    if(abs(x - x_down) > 1):
                        if(board[x_down - 1][y_down] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            if(x_down == N - 1):
                                temp_board[x_down][y_down] = '@'
                                if('@' in temp_pieces_dict):
                                    temp_pieces_dict['@'].append((x_down, y_down))

                                else: temp_pieces_dict['@'] = [(x_down, y_down)]
                                
                            else:
                                temp_board[x_down][y_down] = 'W'
                                temp_pieces_dict['W'].append((x_down, y_down))

                            temp_pieces_dict['W'].remove((x, y))
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_down - 1][y_down] in 'bB'):
                            if(x_down + 1 <= N - 1 and board[x_down + 1][y_down] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                if(x_down + 1 == N - 1):
                                    temp_board[x_down + 1][y_down] = '@'
                                    if('@' in temp_pieces_dict):
                                        temp_pieces_dict['@'].append((x_down + 1, y_down))

                                    else: temp_pieces_dict['@'] = [(x_down + 1, y_down)]

                                else:
                                    temp_board[x_down + 1][y_down] = 'W'
                                    temp_pieces_dict['W'].append((x_down + 1, y_down))
                                
                                temp_pieces_dict['W'].remove((x, y))
                                temp_pieces_dict[temp_board[x_down - 1][y_down]].remove((x_down - 1, y_down))
                                temp_board[x_down - 1][y_down] = '.'
                                all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_down - 1][y_down] in 'wW@'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        if(x_down == N - 1):
                            temp_board[x_down][y_down] = '@'
                            if('@' in temp_pieces_dict):
                                temp_pieces_dict['@'].append((x_down, y_down))

                            else: temp_pieces_dict['@'] = [(x_down, y_down)]
                            
                        else:
                            temp_board[x_down][y_down] = 'W'
                            temp_pieces_dict['W'].append((x_down, y_down))
                            
                        temp_pieces_dict['W'].remove((x, y))
                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_down][y_down] in 'bB'):
                    if(abs(x - x_down) > 1):
                        if((board[x_down - 1][y_down] == '.') and (x_down + 1 <= N - 1) and board[x_down + 1][y_down] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            if(x_down + 1 == N - 1):
                                temp_board[x_down + 1][y_down] = '@'
                                if('@' in temp_pieces_dict):
                                    temp_pieces_dict['@'].append((x_down + 1, y_down))

                                else: temp_pieces_dict['@'] = [(x_down + 1, y_down)]
                                
                            else:
                                temp_board[x_down + 1][y_down] = 'W'
                                temp_pieces_dict['W'].append((x_down + 1, y_down))

                            temp_pieces_dict['W'].remove((x, y))
                            temp_pieces_dict[temp_board[x_down][y_down]].remove((x_down, y_down))
                            temp_board[x_down][y_down] = '.'
                            all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(x_down < N - 1 and board[x_down + 1][y_down] == '.'):
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_down][y_down]].remove((x_down, y_down))
                        temp_board[x_down][y_down] = '.'
                        temp_pieces_dict['W'].remove((x, y))
                        if(x_down + 1 == N - 1):
                            temp_board[x_down + 1][y_down] = '@'
                            if('@' in temp_pieces_dict):
                                temp_pieces_dict['@'].append((x_down + 1, y_down))

                            else: temp_pieces_dict['@'] = [(x_down + 1, y_down)]
                            
                        else:
                            temp_board[x_down + 1][y_down] = 'W'
                            temp_pieces_dict['W'].append((x_down + 1, y_down))

                        all_white_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break
            
    return all_white_pikachu_moves

# To get all white raichus moves'
def get_all_white_raichu_moves(board, N, pieces_dict):
    all_white_raichu_moves = []
    if('@' in pieces_dict):
        for x, y in pieces_dict['@']:
            # First define the increments need to move in all directions
            left = (0, -1)
            left_up = (-1, -1)
            up = (-1, 0)
            right_up = (-1, 1)
            right = (0, 1)
            right_down = (1, 1)
            down = (1, 0)
            down_left = (1, -1)
            all_directions = [left, left_up, up, right_up, right, right_down, down, down_left]

            # Traverse in all the directions
            for each_direction in all_directions:
                # Step size to increment 
                step_size = 1
                # Possible move
                new_x, new_y = x + (each_direction[0] * step_size), y + (each_direction[1] * step_size)
                # To check whether we have killed a opponent piece in that direction or not
                opponents_killed = False
                # The position of the opponent piece killed 
                opponent_piece_x = None
                opponent_piece_y = None

                # if the possible move is within the board or not
                while(0 <= new_x < N and 0 <= new_y < N):
                    temp_board = deepcopy(board)
                    temp_pieces_dict = deepcopy(pieces_dict)

                    # If it is empty space then we can move our piece
                    if(board[new_x][new_y] == '.'):
                        temp_board[x][y] = '.'
                        temp_pieces_dict['@'].remove((x, y))
                        # If we have already killed, then we have to remove the opponent piece
                        # Hence we stored it in first place
                        # If not killed, then no need to do anything
                        if(opponents_killed and opponent_piece_x is not None and opponent_piece_y is not None):
                            temp_pieces_dict[temp_board[opponent_piece_x][opponent_piece_y]].remove((opponent_piece_x, opponent_piece_y))
                            temp_board[opponent_piece_x][opponent_piece_y] = '.'

                        temp_board[new_x][new_y] = '@'
                        temp_pieces_dict['@'].append((new_x,new_y))
                        all_white_raichu_moves.append((temp_board, temp_pieces_dict))

                    # If we have any opponent piece, then we check whether we have already killed in that direction or not
                    # If we didn't kill, then we can kill it.
                    # If we already killed, then we cannot kill or move beyond that
                    # Hence we break here
                    elif(board[new_x][new_y] in 'bB$' and (not opponents_killed)):
                        opponent_piece_x = new_x
                        opponent_piece_y = new_y
                        opponents_killed = True

                    # If we encounter any other piece instead of '.' or opponent piece 
                    # i.e., same player piece,
                    # Then also we can't move here or beyond this point, since it is not empty
                    # Hence we break here
                    else: break

                    step_size += 1
                    new_x, new_y = x + (each_direction[0] * step_size), y + (each_direction[1] * step_size)

    return all_white_raichu_moves

# All black moves' logic is similalr to white pieces
# Except that we just change the direction down to up,
# Since black move up the board

# To get all black pichus moves'
def get_all_black_pichu_moves(board, N, pieces_dict):
    all_black_pichu_moves = []
    if('b' in pieces_dict):
        for x, y in pieces_dict['b']:
            possible_move_1 = None
            possible_move_2 = None
            # print(x, y)
            # print(pieces_dict)
            if(x == 1):
                if(y < N - 1):
                    possible_move_1 = board[x - 1][y + 1]
                
                if(y > 0):
                    possible_move_2 = board[x - 1][y - 1]

                if(possible_move_1 is not None and possible_move_1 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x - 1][y + 1] = '$'
                    temp_pieces_dict['b'].remove((x, y))
                    if('$' in temp_pieces_dict):
                        temp_pieces_dict['$'].append((x - 1, y + 1))

                    else:
                        temp_pieces_dict['$'] = [(x - 1, y + 1)]
                    
                    all_black_pichu_moves.append((temp_board, temp_pieces_dict))

                if(possible_move_2 is not None and possible_move_2 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x - 1][y - 1] = '$'
                    temp_pieces_dict['b'].remove((x, y))
                    if('$' in temp_pieces_dict):
                        temp_pieces_dict['$'].append((x - 1, y - 1))

                    else:
                        temp_pieces_dict['$'] = [(x - 1, y - 1)]
                    
                    all_black_pichu_moves.append((temp_board, temp_pieces_dict))

            else:
                if(y < N - 1):
                    possible_move_1 = board[x - 1][y + 1]
                if(y > 0):
                    possible_move_2 = board[x - 1][y - 1]

                if(possible_move_1 is not None and possible_move_1 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x - 1][y + 1] = 'b'
                    temp_pieces_dict['b'].remove((x, y))
                    temp_pieces_dict['b'].append((x - 1, y + 1))
                    all_black_pichu_moves.append((temp_board, temp_pieces_dict))

                elif(possible_move_1 is not None and possible_move_1 == 'w'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    if(y + 1 < N - 1 and  x - 1 > 0 and temp_board[x - 2][y + 2] == '.'):
                        temp_board[x][y] = '.'
                        if(x - 2 == 0):
                            temp_board[x - 2][y + 2] = '$'
                            if('$' in temp_pieces_dict):
                                temp_pieces_dict['$'].append((x - 2, y + 2))

                            else:
                                temp_pieces_dict['$'] = [(x - 2, y + 2)]

                        else:
                            temp_board[x - 2][y + 2] = 'b'
                            if('b' in temp_pieces_dict):
                                temp_pieces_dict['b'].append((x - 2, y + 2))

                            else:
                                temp_pieces_dict['b'] = [(x - 2, y + 2)]

                        temp_pieces_dict['w'].remove((x - 1, y + 1))
                        temp_board[x - 1][y + 1] = '.'
                        temp_pieces_dict['b'].remove((x, y))
                        all_black_pichu_moves.append((temp_board, temp_pieces_dict))

                if(possible_move_2 is not None and possible_move_2 == '.'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    temp_board[x][y] = '.'
                    temp_board[x - 1][y - 1] = 'b'
                    temp_pieces_dict['b'].remove((x, y))
                    temp_pieces_dict['b'].append((x - 1, y - 1))
                    all_black_pichu_moves.append((temp_board, temp_pieces_dict))

                elif(possible_move_2 is not None and possible_move_2 == 'w'):
                    temp_pieces_dict = deepcopy(pieces_dict)
                    temp_board = deepcopy(board)
                    if(y - 1 > 0 and  x - 1 > 0 and temp_board[x - 2][y - 2] == '.'):
                        temp_board[x][y] = '.'
                        if(x - 2 == 0):
                            temp_board[x - 2][y - 2] = '$'
                            if('$' in temp_pieces_dict):
                                temp_pieces_dict['$'].append((x - 2, y - 2))

                            else:
                                temp_pieces_dict['$'] = [(x - 2, y - 2)]

                        else:
                            temp_board[x - 2][y - 2] = 'b'
                            if('b' in temp_pieces_dict):
                                temp_pieces_dict['b'].append((x - 2, y - 2))

                            else:
                                temp_pieces_dict['b'] = [(x - 2, y - 2)]

                        temp_pieces_dict['w'].remove((x - 1, y - 1))
                        temp_board[x - 1][y - 1] = '.'
                        temp_pieces_dict['b'].remove((x, y))
                        all_black_pichu_moves.append((temp_board, temp_pieces_dict))

    # for each_move, each_move_pieces_dict in all_black_pichu_moves:
        # print("----------------")
        # print(each_move)
        # print(each_move_pieces_dict)
        # print("----------------")

    return all_black_pichu_moves

# To get all black pikachus moves'
def get_all_black_pikachu_moves(board, N, pieces_dict):
    all_black_pikachu_moves = []
    if('B' in pieces_dict):
        for x, y in pieces_dict['B']:
            possible_moves_left = []
            possible_moves_right = []
            possible_moves_up= []

            for each_left_column_index in range(y - 1, max(y - 3, -1), -1):
                possible_moves_left.append((x, each_left_column_index))

            for each_right_column_index in range(y + 1, min(y + 3, N)):
                possible_moves_right.append((x, each_right_column_index))

            for each_up_row_index in range(x - 1, max(x - 3, -1), -1):
                possible_moves_up.append((each_up_row_index, y))

            for x_left, y_left in possible_moves_left:
                if(board[x_left][y_left] == '.'):
                    if(abs(y - y_left) > 1):
                        if(board[x_left][y_left + 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_left][y_left] = 'B'
                            temp_pieces_dict['B'].remove((x, y))
                            temp_pieces_dict['B'].append((x_left, y_left))
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_left][y_left + 1] in 'wW'):
                            if(y_left - 1 >= 0 and board[x_left][y_left - 1] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                temp_board[x_left][y_left - 1] = 'B'
                                temp_pieces_dict['B'].remove((x, y))
                                temp_pieces_dict[temp_board[x_left][y_left + 1]].remove((x_left, y_left + 1))
                                temp_board[x_left][y_left + 1] = '.'
                                temp_pieces_dict['B'].append((x_left, y_left - 1))
                                all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                            else: break

                        elif(board[x_left][y_left + 1] in 'bB$'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_board[x_left][y_left] = 'B'
                        temp_pieces_dict['B'].remove((x, y))
                        temp_pieces_dict['B'].append((x_left, y_left))
                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_left][y_left] in 'wW'):
                    if(abs(y - y_left) > 1):
                        if((board[x_left][y_left + 1] == '.') and (y_left - 1 >= 0) and board[x_left][y_left - 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_left][y_left - 1] = 'B'
                            temp_pieces_dict['B'].remove((x, y))
                            temp_pieces_dict[temp_board[x_left][y_left]].remove((x_left, y_left))
                            temp_board[x_left][y_left] = '.'
                            temp_pieces_dict['B'].append((x_left, y_left - 1))
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(y_left > 0 and board[x_left][y_left - 1] == '.'):
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_left][y_left]].remove((x_left, y_left))
                        temp_board[x_left][y_left] = '.'
                        temp_pieces_dict['B'].remove((x, y))
                        temp_board[x_left][y_left - 1] ='B'
                        temp_pieces_dict['B'].append((x_left, y_left - 1))
                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break

            for x_right, y_right in possible_moves_right:
                if(board[x_right][y_right] == '.'):
                    if(abs(y - y_right) > 1):
                        if(board[x_right][y_right - 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_right][y_right] = 'B'
                            temp_pieces_dict['B'].remove((x, y))
                            temp_pieces_dict['B'].append((x_right, y_right))
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_right][y_right - 1] in 'wW'):
                            if(y_right + 1 <= N - 1 and board[x_right][y_right + 1] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                temp_board[x_right][y_right + 1] = 'B'
                                temp_pieces_dict['B'].remove((x, y))
                                temp_pieces_dict[temp_board[x][y_right - 1]].remove((x_right, y_right - 1))
                                temp_board[x][y_right - 1] = '.'
                                temp_pieces_dict['B'].append((x_right, y_right + 1))
                                all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_right][y_right - 1] in 'bB$'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_board[x_right][y_right] = 'B'
                        temp_pieces_dict['B'].remove((x, y))
                        temp_pieces_dict['B'].append((x_right, y_right))
                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_right][y_right] in 'wW'):
                    if(abs(y - y_right) > 1):
                        if((board[x_right][y_right - 1] == '.') and (y_right + 1 <= N - 1) and board[x_right][y_right + 1] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            temp_board[x_right][y_right + 1] = 'B'
                            temp_pieces_dict['B'].remove((x, y))
                            temp_pieces_dict[temp_board[x_right][y_right]].remove((x_right, y_right))
                            temp_board[x_right][y_right] = '.'
                            temp_pieces_dict['B'].append((x_right, y_right + 1))
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(y_right < N - 1 and board[x_right][y_right + 1] == '.'):
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_right][y_right]].remove((x_right, y_right))
                        temp_board[x_right][y_right] = '.'
                        temp_pieces_dict['B'].remove((x, y))
                        temp_board[x_right][y_right + 1] ='B'
                        temp_pieces_dict['B'].append((x_right, y_right + 1))
                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break

            for x_up, y_up in possible_moves_up:
            #     print(x_up, y_up)
            #     print(board[x_up][y_up])
                if(board[x_up][y_up] == '.'):
                    if(abs(x - x_up) > 1):
                        if(board[x_up + 1][y_up] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            if(x_up == 0):
                                temp_board[x_up][y_up] = '$'
                                if('$' in temp_pieces_dict):
                                    temp_pieces_dict['$'].append((x_up, y_up))

                                else: temp_pieces_dict['$'] = [(x_up, y_up)]
                                
                            else:
                                temp_board[x_up][y_up] = 'B'
                                temp_pieces_dict['B'].append((x_up, y_up))

                            temp_pieces_dict['B'].remove((x, y))
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_up + 1][y_up] in 'wW'):
                            if(x_up - 1 >= 0 and board[x_up - 1][y_up] == '.'):
                                temp_board = deepcopy(board)
                                temp_pieces_dict = deepcopy(pieces_dict)
                                temp_board[x][y] = '.'
                                if(x_up - 1 == 0):
                                    temp_board[x_up - 1][y_up] = '$'
                                    if('$' in temp_pieces_dict):
                                        temp_pieces_dict['$'].append((x_up - 1, y_up))

                                    else: temp_pieces_dict['$'] = [(x_up - 1, y_up)]

                                else:
                                    temp_board[x_up - 1][y_up] = 'B'
                                    temp_pieces_dict['B'].append((x_up - 1, y_up))
                                
                                temp_pieces_dict['B'].remove((x, y))
                                temp_pieces_dict[temp_board[x_up + 1][y_up]].remove((x_up + 1, y_up))
                                temp_board[x_up + 1][y_up] = '.'
                                all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        elif(board[x_up - 1][y_up] in 'bB$'):
                            break

                    else:
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        if(x_up == 0):
                            temp_board[x_up][y_up] = '$'
                            if('$' in temp_pieces_dict):
                                temp_pieces_dict['$'].append((x_up, y_up))

                            else: temp_pieces_dict['$'] = [(x_up, y_up)]
                            
                        else:
                            temp_board[x_up][y_up] = 'B'
                            temp_pieces_dict['B'].append((x_up, y_up))
                            
                        temp_pieces_dict['B'].remove((x, y))
                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                elif(board[x_up][y_up] in 'wW'):
                    if(abs(x - x_up) > 1):
                        if((board[x_up + 1][y_up] == '.') and (x_up - 1 <= 0) and board[x_up - 1][y_up] == '.'):
                            temp_board = deepcopy(board)
                            temp_pieces_dict = deepcopy(pieces_dict)
                            temp_board[x][y] = '.'
                            if(x_up - 1 == 0):
                                temp_board[x_up - 1][y_up] = '$'
                                if('$' in temp_pieces_dict):
                                    temp_pieces_dict['$'].append((x_up - 1, y_up))

                                else: temp_pieces_dict['$'] = [(x_up - 1, y_up)]
                                
                            else:
                                temp_board[x_up - 1][y_up] = 'B'
                                temp_pieces_dict['B'].append((x_up - 1, y_up))

                            temp_pieces_dict['B'].remove((x, y))
                            temp_pieces_dict[temp_board[x_up][y_up]].remove((x_up, y_up))
                            temp_board[x_up][y_up] = '.'
                            all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                        else: break

                    elif(x_up > 0 and board[x_up - 1][y_up] == '.'):
                        # print('in elif with diff equal to 1')
                        temp_board = deepcopy(board)
                        temp_pieces_dict = deepcopy(pieces_dict)
                        temp_board[x][y] = '.'
                        temp_pieces_dict[temp_board[x_up][y_up]].remove((x_up, y_up))
                        temp_board[x_up][y_up] = '.'
                        temp_pieces_dict['B'].remove((x, y))
                        if(x_up - 1 == 0):
                            temp_board[x_up - 1][y_up] = '$'
                            if('$' in temp_pieces_dict):
                                temp_pieces_dict['$'].append((x_up - 1, y_up))

                            else: temp_pieces_dict['$'] = [(x_up - 1, y_up)]
                            
                        else:
                            temp_board[x_up - 1][y_up] = 'B'
                            temp_pieces_dict['B'].append((x_up - 1, y_up))

                        all_black_pikachu_moves.append((temp_board, temp_pieces_dict))

                else: break

    return all_black_pikachu_moves

# To get all black raichus moves'
def get_all_black_raichu_moves(board, N, pieces_dict):
    all_black_raichu_moves = []
    if('$' in pieces_dict):
        for x, y in pieces_dict['$']:
            left = (0, -1)
            left_up = (-1, -1)
            up = (-1, 0)
            right_up = (-1, 1)
            right = (0, 1)
            right_down = (1, 1)
            down = (1, 0)
            down_left = (1, -1)
            all_directions = [left, left_up, up, right_up, right, right_down, down, down_left]

            for each_direction in all_directions:
                step_size = 1
                new_x, new_y = x + (each_direction[0] * step_size), y + (each_direction[1] * step_size)
                opponents_killed = False
                opponent_piece_x = None
                opponent_piece_y = None
                while(0 <= new_x < N and 0 <= new_y < N):
                    temp_board = deepcopy(board)
                    temp_pieces_dict = deepcopy(pieces_dict)
                    if(board[new_x][new_y] == '.'):
                        temp_board[x][y] = '.'
                        temp_pieces_dict['$'].remove((x, y))
                        if(opponents_killed and opponent_piece_x is not None and opponent_piece_y is not None):
                            temp_pieces_dict[temp_board[opponent_piece_x][opponent_piece_y]].remove((opponent_piece_x, opponent_piece_y))
                            temp_board[opponent_piece_x][opponent_piece_y] = '.'

                        temp_board[new_x][new_y] = '$'
                        temp_pieces_dict['$'].append((new_x,new_y))
                        all_black_raichu_moves.append((temp_board, temp_pieces_dict))

                    elif(board[new_x][new_y] in 'wW@' and (not opponents_killed)):
                        opponent_piece_x = new_x
                        opponent_piece_y = new_y
                        opponents_killed = True

                    else: break

                    step_size += 1
                    new_x, new_y = x + (each_direction[0] * step_size), y + (each_direction[1] * step_size)


    return all_black_raichu_moves

# To get all the valid possible for a player from the board
def get_all_possible_valid_moves_of_player_in_board(board, N, player, pieces_dict):
    all_possible_valid_moves = []

    # Check if we need the moves of white or black
    if(player == 'w'):
        # Getting the moves of white pichus
        all_possible_valid_moves += get_all_white_pichu_moves(board, N, pieces_dict)
        # Getting the moves of white pikachus
        all_possible_valid_moves += get_all_white_pikachu_moves(board, N, pieces_dict)
        # Getting the moves of white raichus
        all_possible_valid_moves += get_all_white_raichu_moves(board, N, pieces_dict)

    if(player == 'b'):
        # Getting the moves of black pichus    
        all_possible_valid_moves += get_all_black_pichu_moves(board, N, pieces_dict)
        # Getting the moves of black pikachus
        all_possible_valid_moves += get_all_black_pikachu_moves(board, N, pieces_dict)
        # Getting the moves of black raichus
        all_possible_valid_moves += get_all_black_raichu_moves(board, N, pieces_dict)

    # print(all_possible_valid_moves)

    return all_possible_valid_moves

def minimax(board, N, player, pieces_dict, max, depth, alpha, beta):
    opponent = 'wW@' if player == 'b' else 'bB$'

    did_we_win_the_game_or_not = gameWon(player, opponent, pieces_dict)
    if(depth == 0 or did_we_win_the_game_or_not):
        return board, score(player, pieces_dict), did_we_win_the_game_or_not
    
    best_move = None
    win_state_for_best_move = False
    if(max):
        maxValue = float('-inf')
        for each_move, each_move_updated_pieces_dict in get_all_possible_valid_moves_of_player_in_board(board, N, player, pieces_dict):
            _, each_move_score, gameWonOrNot = minimax(each_move, N, player, each_move_updated_pieces_dict, False, depth - 1, alpha, beta)
            if(each_move_score > maxValue):
                maxValue = each_move_score
                best_move = each_move
                win_state_for_best_move = gameWonOrNot


            if(alpha < each_move_score):
                alpha = each_move_score
                # best_move = each_move

            if(beta <= alpha):
                break

        return best_move, maxValue, win_state_for_best_move


    else:
        minValue = float('inf')
        for each_move, each_move_updated_pieces_dict in get_all_possible_valid_moves_of_player_in_board(board, N, opponent[0], pieces_dict):
            _, each_move_score, gameWonOrNot = minimax(each_move, N, player, each_move_updated_pieces_dict, True, depth - 1, alpha, beta)
            if(each_move_score < minValue):
                minValue = each_move_score
                best_move = each_move
                win_state_for_best_move = gameWonOrNot

            if(beta > each_move_score):
                beta = each_move_score
                # best_move = each_move

            if(beta <= alpha):
                break
        
        return best_move, minValue, win_state_for_best_move
        



def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #

    board_matrix = convert_string_to_board_matrix(board, N)
    # Create a dictionary of the position of pieces on the board.
    # So that we can access this dictionary instead of checking the whole board again and again
    pieces_dict = {}
    for i in range(len(board_matrix)):
        for j in range(N):
            element_at_i_j = board_matrix[i][j]
            if(element_at_i_j != '.'):
                if(element_at_i_j in pieces_dict):
                    pieces_dict[element_at_i_j].append((i, j))

                else: pieces_dict[element_at_i_j] = [(i, j)]

    # print(pieces_dict)
            
    # print(board_matrix)
    # print(convert_board_matrix_to_string(board_matrix, N))
    # for each_move, each_move_updated_pieces_dict in get_all_possible_valid_moves_of_player_in_board(board_matrix, N, player, pieces_dict):
    #     print('===================')
    #     print(each_move_updated_pieces_dict)
    #     print(board_to_string(convert_board_matrix_to_string(each_move, N), N))
    #     print('=================')
            

    # Made the depth dynamic so that we can run the algorithm till the maximum depth it can reach before terminating at the time limit
    depth = 1
    while(True):
        # print('depth = ', depth)
        best_move_for_current_depth, score, gameWonOrNot = minimax(board_matrix, N, player, pieces_dict, True, depth, float('-inf'), float('inf'))        
        yield convert_board_matrix_to_string(best_move_for_current_depth, N)
        # We can stop execution since we already reached the winning state
        if(gameWonOrNot): break

        depth += 1
    
    


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)

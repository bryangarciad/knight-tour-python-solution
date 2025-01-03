type Coordinate = (int, int)
type Board = [[int]]

board_size = 8

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
possible_knight_moves = list(zip(move_x, move_y))

board = [[-1 for i in range(board_size)] for i in range(board_size)]

def is_safe_to_move(position: Coordinate, board: Board):
    x, y = position
    return (0 <= x < board_size and
            0 <= y < board_size and
            board[x][y] == -1)

def get_all_valid_possible_knight_moves(current_knight_position: Coordinate):
    possible_moves = []
    for x, y in possible_knight_moves:
        new_position = (current_knight_position[0] + x, current_knight_position[1] + y)
        if is_safe_to_move(position=new_position, board=board):
            possible_moves.append(new_position)
    return possible_moves

def knigh_tour_solution(position: Coordinate, moves=1):
    if moves == board_size**2:
        return True
    
    x, y = position
    board[x][y] = moves

    possible_positions = get_all_valid_possible_knight_moves(position)
    for possible_position in possible_positions:
        if knigh_tour_solution(position=possible_position, moves=moves+1):
            return True
    
    board[x][y] = -1
    return False

knigh_tour_solution((0, 0))

for row in board:
    print(row)

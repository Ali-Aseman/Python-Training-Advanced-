board_width = 10    
board_length = 10
cell_width = 3

#                  10  *   "| 0 "   +  "|"     
floor_width = board_width * (cell_width + 1) + 1

board = []

for _ in range(board_length):
    row = []
    for _ in range(board_width):
        row.append(0)
    board.append(row)

def print_board():
    def cell_repr(item):
        return str(item).center(cell_width)

    floor_repr = "-" * floor_width
    print(floor_repr)
    for row in board:
        row_repr = "|" + "|".join(map(cell_repr, row)) + "|"
        print(row_repr)
        print(floor_repr)

print_board() 
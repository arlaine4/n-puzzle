def do_move(dico, grid, move, switch):
    pos = puzzle.index(0) ## Find position of zero
    if move == 'up':
        grid[pos], grid[pos - size] = grid[pos - size], grid[pos]
    if move == 'down':
        grid[pos], grid[pos + size] = grid[pos + size], grid[pos]
    if move == 'right':
        grid[pos], grid[pos + 1] = grid[pos + 1], grid[pos]
    if move == 'left':
        grid[pos], grid[pos - 1] = grid[pos - 1], grid[pos]
    return new_grid, switch + 1

def get_childs_and_infos(dico, grid):
    pos = grid.index(0)
    moves = []
    if not pos < size:                                      #BAS
        moves.append('down')
    if not pos >= len(grid) - size:                       #HAUT
        moves.append('up')
    if not pos % size == 0:                                 #DROITE
        moves.append('right')
    if not (pos + 1) % dico['size'] == 0 and pos != 0:      #GAUCHE
        moves.append('left')
    return moves


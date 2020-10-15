def do_move(dico, grid, move, switch):
    pos = grid.index(0) ## Find position of zero
    if move == 'up':
        grid[pos], grid[pos - dico['size']] = grid[pos - dico['size']], grid[pos]
    if move == 'down':
        grid[pos], grid[pos + dico['size']] = grid[pos + dico['size']], grid[pos]
    if move == 'right' and pos + 1:
        grid[pos], grid[pos + 1] = grid[pos + 1], grid[pos]
    if move == 'left':
        grid[pos], grid[pos - 1] = grid[pos - 1], grid[pos]
    return grid, switch + 1

def get_moves(dico, grid):
    pos = grid.index(0)
    moves = []
    if not pos < dico['size']:                                      #HAUT
        moves.append('up')
    if not pos >= len(grid) - dico['size']:                       #BAS
        moves.append('down')
    if not pos % dico['size'] == 0:                                 #GAUCHE
        moves.append('left')
    if not (pos + 1) % dico['size'] == 0 and pos != 0:      #DROITE
        moves.append('right')
    return moves


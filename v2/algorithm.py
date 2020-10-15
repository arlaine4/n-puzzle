from copy import deepcopy

def do_move(dico, grid, move):
    x, y = get_0_pos(grid)
    new_grid = deepcopy(grid)
    if move == 'down':                  #BAS
        tmp = new_grid[x + 1][y]
        new_grid[x + 1][y] = 0
        new_grid[x][y] = tmp
    if move == 'up':                    #HAUT
        tmp = new_grid[x - 1][y]
        new_grid[x - 1][y] = 0
        new_grid[x][y] = tmp
    if move == 'right':                 #DROITE
        tmp = new_grid[x][y + 1]
        new_grid[x][y + 1] = 0
        new_grid[x][y] = tmp
    if move == 'left':                  #GAUCHE
        tmp = new_grid[x][y - 1]
        new_grid[x][y - 1] = 0
        new_grid[x][y] = tmp
    return new_grid

def get_childs_and_infos(dico, grid):
    x, y = get_0_pos(grid)
    moves = []
    if x + 1 < dico["size"]:                #BAS
        moves.append('down')
    if x - 1 >= 0 and x < dico['size']:     #HAUT
        moves.append('up')
    if y + 1 < dico['size']:                #DROITE
        moves.append('right')
    if y - 1 >= 0 and x < dico['size']:     #GAUCHE
        moves.append('left')
    return moves

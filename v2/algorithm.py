import heuristics as he
from copy import deepcopy

def heuristic_and_move(dico, grid, move, switchs, h_type, closed, ideal_grid, queue, cost):
    new_puzzle, nb = do_move(dico, deepcopy(grid), move)
    if tuple(new_puzzle) in closed:
        return queue, switchs
    h_c, g_c = he.call_heuristic(dico, new_puzzle, h_type, ideal_grid, nb)
    f_c = h_c + g_c
    if not any(grid in item[1] for item in queue.queue):
        queue.put((f_c, new_puzzle, grid, cost + 1))
        switchs += 1
    return queue, switchs

def do_move(dico, grid, move):
    pos = grid.index(0) ## Find position of zero
    if move == 'up':
        nb = grid[pos - dico['size']]
        grid[pos], grid[pos - dico['size']] = grid[pos - dico['size']], grid[pos]
    if move == 'down':
        nb = grid[pos + dico['size']]
        grid[pos], grid[pos + dico['size']] = grid[pos + dico['size']], grid[pos]
    if move == 'right' and pos + 1:
        nb = grid[pos + 1]
        grid[pos], grid[pos + 1] = grid[pos + 1], grid[pos]
    if move == 'left':
        nb = grid[pos - 1]
        grid[pos], grid[pos - 1] = grid[pos - 1], grid[pos]
    return grid, nb

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


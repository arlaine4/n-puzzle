def get_childs_and_infos(dico, grid, ideal_grid):
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

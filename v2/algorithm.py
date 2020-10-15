

def get_childs_and_infos(dico, grid, ideal_grid):
    x, y = get_0_pos(grid)
    if x + 1 < dico["size"]:                #BAS
        next_x, next_y =  x + 1, y
    if x - 1 >= 0 and x < dico['size']:     #HAUT
        next_x, next_y =  x - 1, y
    if y + 1 < dico['size']:                #DROITE
        next_x, next_y =  x, y + 1
    if y - 1 >= 0 and x < dico['size']:     #GAUCHE
        next_x, next_y =  x, y - 1
    # Determine ce qu'on fait/renvoi
    return 

import set_ideal_grid as sid
import utils
import heuristics

def Astar(dico, h_type, visu):
    ideal_grid = sid.set_ideal_grid(dico)
    grid = utils.load_grid(dico)
    grid = utils.cast_list_to_numpy_array(grid, dico["size"])
    print(grid)

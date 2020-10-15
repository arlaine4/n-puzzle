import set_ideal_grid as sid
import utils
import heuristics
import queue as q

def shortest_way(grid, ideal_grid, dico, h_type, visu):
    queue = q.PriorityQueue() #file prio 
    closed = set() #nodes deja explorees
    path = [] #ensemble des etats de la grille sous forme de tuple

def Astar(dico, h_type, visu):
    ideal_grid = sid.set_ideal_grid(dico)
    grid = utils.load_grid(dico) #chargement de la grille
    grid = utils.cast_list_to_numpy_array(grid, dico["size"]) #cast en type numpy
    shortest_way(grid, ideal_grid, dico, h_type, visu)

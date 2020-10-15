import set_ideal_grid as sid
import utils
import heuristics
import queue as q
import algorithm as algo

def shortest_way(grid, ideal_grid, dico, h_type, visu):
    queue = q.PriorityQueue() #file prio
    closed = set() #nodes deja explorees
    path = [] #ensemble des etats de la grille sous forme de tuple
    queue.put((0, grid, grid, 0))
    iteration = 0
    switchs = 0
    while iteration <= dico["iteration"]:
        g_c, grid, parent, f_c = queue.get()
        closed.add(tuple(grid))
        path.append((grid, parent, g_c))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            print(grid)
            print(move)
            queue, switchs = algo.do_move(dico, grid, move, switchs)

def Astar(dico, h_type, visu):
    ideal_grid = sid.set_ideal_grid(dico)
    grid = utils.load_grid(dico) #chargement de la grille
    grid = utils.cast_list_to_numpy_array(grid, dico["size"]) #cast en type numpy
    shortest_way(grid, ideal_grid, dico, h_type, visu)

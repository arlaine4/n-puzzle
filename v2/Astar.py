import set_ideal_grid as sid
import utils
import queue as q
import algorithm as algo
import time

def shortest_way(grid, ideal_grid, dico, h_type, visu):
    queue = q.PriorityQueue() #file prio
    closed = set() #nodes deja explorees
    path = [] #ensemble des etats de la grille sous forme de tuple
    queue.put((0, grid, grid, 0))
    iteration = 0
    switchs = 0
    while iteration <= dico["iteration"]:
        g_c, grid, parent, cost = queue.get()
        if (grid == ideal_grid):
            return ideal_grid
        closed.add(tuple(grid))
        print(grid)
        path.append((grid, parent, g_c))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            queue, switchs = algo.heuristic_and_move(dico, grid, move, switchs, h_type, closed, ideal_grid, queue, cost)
        iteration += 1
        print (iteration)


def Astar(dico, h_type, visu):
    ideal_grid = sid.set_ideal_grid(dico)
    grid = utils.load_grid(dico) #chargement de la grille
    grid = utils.cast_list_to_numpy_array(grid, dico["size"]) #cast en type numpy
    start_t = time.time()
    grid = shortest_way(grid, ideal_grid, dico, h_type, visu)
    end_t = time.time()
    for i in range(len(grid)):
        if (i%dico['size'] == 0):
            print()
        print(grid[i], end=' ')
    print()
    print ("Temp d'execution:", round(((end_t - start_t)), 2), "seconde(s)")

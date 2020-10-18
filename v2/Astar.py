import set_ideal_grid as sid
import visu
import utils
import queue as q
import algorithm as algo
import time
import visu

def shortest_way(grid, ideal_grid, dico, h_type, visu_bool):
    queue = q.PriorityQueue() #File prio
    closed = set() #nodes deja explorees
    path = []
    queue.put((0, grid, grid, 0))
    iteration = 0
    switchs = 0 #mouvements effectues
    if visu_bool is True:
        stdscr = visu.init_visu()
    else:
        stdscr = None
    while iteration < dico["iteration"]:
        g_c, grid, parent, cost = queue.get()
        if grid == ideal_grid:
            return ideal_grid, switchs, iteration, stdscr
        closed.add(tuple(grid))
        #if iteration % 100 == 0:
            #print(grid)
            #print("Loop", iteration)
        path.append((grid, parent, g_c))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            queue, switchs = algo.heuristic_and_move(dico, grid, move, switchs, h_type, \
                    closed, ideal_grid, queue, cost)
        iteration += 1

def Astar(dico, h_type, visu_bool):
        ideal_grid = sid.set_ideal_grid(dico)
        grid = utils.load_grid(dico) #chargement de la grille
        grid = utils.cast_list_to_numpy_array(grid, dico["size"]) #cast en type numpy
        start_t = time.time() if visu_bool == False else 0
        if visu_bool is False:
            grid, states, complexity, stdscr = shortest_way(grid, ideal_grid, dico, h_type, visu_bool)
        elif visu_bool is True:
            visu.shortest_way_visu(grid, ideal_grid, dico, h_type)
        end_t = time.time() if visu_bool == False else 0
        if not visu_bool:
            print("\nFinal grid: ", end='')
            for i in range(len(grid)):
                    if (i % dico['size'] == 0):
                            print()
                    print(grid[i], end=' ')
            print()
        if not visu_bool:
            print("Resolution time:", round(((end_t - start_t)), 2), "seconde(s)")
            print("Complexity in time: ", complexity)
            print("Complexity in size: ", states)
        else:
            print("There's no timer when the -visual option is activated")

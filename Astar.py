import solver
import heuristics as h
import re
import numpy as np
from copy import deepcopy

def convert_multi_d_to_numpy(grid, size):
    npgrid = np.zeros((size, size), dtype=int)
    npgrid = npgrid.astype(np.int16)
    test = str(grid).split()
    l = 0
    n = 0
    for i in test:
        tmp = re.sub('[^0-9]', '', i)
        if l == size and n < size:
            l = 0
            n += 1
        npgrid[n][l] = int(tmp)
        l += 1
    return npgrid

def get_start_pos(grid):
    pos = {"x" : 0, "y" : 0}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                pos["x"] = i; pos["y"] = j
                return pos
    return pos

def compare_childs_costs(dico, grid, current_node, h_type):
    x = current_node.pos["x"]
    y = current_node.pos["y"]
    childs = []
    cur_pos = {"x" : x, "y" : y} # POSITION DU ZERO
    # TEST DE MOUVEMENT VERS LE BAS, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if x + 1 < dico["size"]:
        print('\nBAS')
        node_b = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_b = {"x" : x + 1, "y" : y} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_b, grid, cur_pos, next_pos_b, h_type))
    # TEST DE MOUVEMENT VERS LE HAUT, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if x - 1 > 0 and x < dico['size']:
        print('\nHAUT')
        node_h = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_h = {"x" : x - 1, "y" : y} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_h, grid, cur_pos, next_pos_h, h_type))
    # TEST DE MOUVEMENT VERS LA DROITE, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if y + 1 < dico['size']:
        print('\nDROITE')
        node_d = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_d = {"x" : x, "y" : y + 1} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_d, grid, cur_pos, next_pos_d, h_type))
    # TEST DE MOUVEMENT VERS LA GAUCHE, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if y - 1 > 0 and x < dico['size']:
        print('\nGAUCHE')
        node_g = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_g = {"x" : x, "y" : y - 1} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_g, grid, cur_pos, next_pos_g, h_type))



def get_child_cost(dico, node, grid, cur_pos, next_pos, h_type):
    tmpgrid = deepcopy(grid) # Deepcopy de la grid pour ne pas modifier l'original
    print("before move :\n", tmpgrid)
    # Deplacement de la piece
    value = tmpgrid[next_pos['x']][next_pos['y']]
    tmpgrid[cur_pos['x']][cur_pos['y']] = value
    tmpgrid[next_pos['x']][next_pos['y']] = 0
    # fin
    node.pos = {"x" : next_pos['x'], "y" : next_pos['y']} # assignation de la nouvel pos au child node
    node.h_c = h.call_heuristic(dico, tmpgrid, h_type) # assignation du coup heuristic au child node
    print("after move :\n", tmpgrid, '\n')
    return node

def shortest_way(dico, grid, closed_nodes, start_node, h_type):
    open_nodes = []
    next_node = None
    file_node = []
    childs = compare_childs_costs(dico, grid, start_node, h_type)


def Astar(dico, grid, closed_nodes, h_type):
    grid = convert_multi_d_to_numpy(grid, dico["size"])
    print("Starting grid:\n", grid)
    start = solver.Node()
    start.pos = get_start_pos(grid)
    closed_nodes.append(start)
    print("starting position : ",start.pos)
    shortest_way(dico, grid, closed_nodes, start, h_type)


import solver
import heuristics as h
import re
import numpy as np
from copy import deepcopy
import time

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

def get_childs_and_infos(dico, grid, current_node, h_type, ideal_grid):
    x = current_node.pos["x"]
    y = current_node.pos["y"]
    childs = []
    cur_pos = {"x" : x, "y" : y} # POSITION DU ZERO
    # TEST DE MOUVEMENT VERS LE BAS, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if x + 1 < dico["size"]:
        # print('\nBAS')
        node_b = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_b = {"x" : x + 1, "y" : y} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_b, grid, cur_pos, next_pos_b, h_type, ideal_grid))
    # TEST DE MOUVEMENT VERS LE HAUT, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if x - 1 >= 0 and x < dico['size']:
        # print('\nHAUT')
        node_h = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_h = {"x" : x - 1, "y" : y} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_h, grid, cur_pos, next_pos_h, h_type, ideal_grid))	
    # TEST DE MOUVEMENT VERS LA DROITE, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if y + 1 < dico['size']:
        # print('\nDROITE')
        node_d = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_d = {"x" : x, "y" : y + 1} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_d, grid, cur_pos, next_pos_d, h_type, ideal_grid))
    # TEST DE MOUVEMENT VERS LA GAUCHE, SI LE MOUVEMENT EST POSSIBLE ON CALCULE LE COUT H
    if y - 1 >= 0 and x < dico['size']:
        # print('\nGAUCHE')
        node_g = deepcopy(solver.Node()) # deepcopy pour eviter la reference et creer le child node
        next_pos_g = {"x" : x, "y" : y - 1} # POSITION DE LA PIECE QUI SERA ECHANGER AVEC LE ZERO
        childs.append(get_child_cost(dico, node_g, grid, cur_pos, next_pos_g, h_type, ideal_grid))
    #for child in childs:
        #print(child.nb, child.pos, child.h_c, child.g_c, child.f_c)
    childs = sort_childs_costs(childs)
    return childs

def	sort_childs_costs(childs):
	i = 0
	j = 0
	while i < len(childs):
		if i + 1 < len(childs) and childs[i+1] and childs[i].f_c > childs[i+1].f_c:
			tmp = deepcopy(childs[i+1])
			childs.remove(childs[i+1])
			childs.insert(0, tmp)
			i = 0
		else:
			i += 1
	return childs

def	get_child_move_cost(node, tmpgrid, ideal_grid):
	pos = node.pos
	x = 0; y = 0
	move = 0
	nb_to_look_for = node.nb
	for i in range(len(ideal_grid)):
		for j in range(len(ideal_grid[i])):
			if ideal_grid[i][j] == nb_to_look_for:
				x = i - pos["x"] ; y = j - pos["y"]
				move = abs(x) + abs(y)
				return move

def get_child_cost(dico, node, grid, cur_pos, next_pos, h_type, ideal_grid):
        tmpgrid = deepcopy(grid) # Deepcopy de la grid pour ne pas modifier l'original
        # print("before move :\n", tmpgrid)
        # Deplacement de la piece
        value = tmpgrid[next_pos['x']][next_pos['y']]
        tmpgrid[cur_pos['x']][cur_pos['y']] = value
        tmpgrid[next_pos['x']][next_pos['y']] = 0
        # fin
        node.nb = value
        node.pos = {"x" : next_pos['x'], "y" : next_pos['y']} # assignation de la nouvel pos au child node
        node.h_c = h.call_heuristic(dico, tmpgrid, h_type, ideal_grid) # assignation du coup heuristic au child node
        node.g_c = get_child_move_cost(node, tmpgrid, ideal_grid) # assignation du coup de deplacement
        node.f_c = node.g_c + node.h_c # assignation du coup f(x)
        # print("after move :\n", tmpgrid, '\n')
        return node

def	append_childs_to_file(file_node, childs):
        file_node.insert(0, childs)
        return file_node

def	move_top_child(dico, grid, new_node, current_node):
        value = grid[new_node.pos['x']][new_node.pos['y']]
        grid[current_node.pos['x']][current_node.pos['y']] = value
        grid[new_node.pos['x']][new_node.pos['y']] = 0
        return grid 

def shortest_way(dico, grid, closed_nodes, start_node, h_type, ideal_grid):
        open_nodes = []
        next_node = None
        file_node = []
        closed_nodes.append(start_node)
        childs = get_childs_and_infos(dico, grid, start_node, h_type, ideal_grid)
        file_node = append_childs_to_file(file_node, childs) #redoo in list type
        heuristic_cost = h.call_heuristic(dico, grid, h_type, ideal_grid)
        loop = 0
        while heuristic_cost != 0 and loop != 2000:
                #time.sleep(8)
                print("Grid before :\n", grid)
                tmpgrid = deepcopy(grid)
                grid = move_top_child(dico, grid, file_node[0][0], closed_nodes[len(closed_nodes) - 1]) #new grid with move
                old = deepcopy(closed_nodes[len(closed_nodes) - 1])
                closed_nodes.append(file_node[0][0]) #fermeture 1er elem
                file_node[0].pop(0) #pop le 1er elem vu que il est explored
                childs = get_childs_and_infos(dico, grid, closed_nodes[len(closed_nodes) - 1], h_type, ideal_grid)
                file_node = append_childs_to_file(file_node, childs) #maj file_node avec les new childs
                heuristic_cost = file_node[0][0].h_c #assignation cout heuristique
                #print(file_node[0][0].pos, closed_nodes[len(closed_nodes) - 1].pos)
                if file_node[0][0].pos['x'] == old.pos['x'] and \
                        file_node[0][0].pos['y'] == old.pos['y']:
                            print("grid before old: \n", grid)
                            file_node.pop(0)
                            grid = deepcopy(tmpgrid)
                            closed_nodes.pop(len(closed_nodes) - 1)
                            print("grid after old: \n", grid)
                print("Grid after : \n", grid)
                print(h.call_heuristic(dico, grid, h_type, ideal_grid))
                loop += 1

def Astar(dico, grid, closed_nodes, h_type, ideal_grid):
    grid = convert_multi_d_to_numpy(grid, dico["size"])
    print("Starting grid:\n", grid)
    start = solver.Node()
    start.pos = get_start_pos(grid)
    closed_nodes.append(start)
    print("starting position : ",start.pos)
    shortest_way(dico, grid, closed_nodes, start, h_type, ideal_grid)


import solver
import heuristics
import re
import numpy as np

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
    tmp_pos = {"x" : x, "y" : y}
    if x + 1 < dico["size"]:
        node = solver.Node()
        node.pos["x"] = x + 1 ; node.pos["y"] = y
        childs.append(get_child_cost(node, grid, tmp_pos, h_type))

def get_child_cost(node, grid, tmp_pos, h_type):
    print("before move :\n\n", grid)
    value = grid[node.pos['x']][node.pos['y']]
    grid[tmp_pos['x']][tmp_pos['y']] = value
    grid[node.pos['x']][node.pos['y']] = 0
    print("after move : \n\n", grid)

def shortest_way(dico, grid, closed_nodes, start_node, h_type):
    open_nodes = []
    next_node = None
    file_node = []
    childs = compare_childs_costs(dico, grid, start_node, h_type)


def Astar(dico, grid, closed_nodes, h_type):
    grid = convert_multi_d_to_numpy(grid, dico["size"])
    start = solver.Node()
    start.pos = get_start_pos(grid)
    closed_nodes.append(start)
    print("starting position : ",start.pos)
    shortest_way(dico, grid, closed_nodes, start, h_type)


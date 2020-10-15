from set_ideal_grid import *
from copy import deepcopy
import utils
import numpy as np
import re

def list_to_nparray(grid, size):
    npgrid = np.zeros((size, size), dtype='int16')
    test = str(grid).split()
    l = 0
    n = 0
    for i in test:
        tmp = re.sub('[^0-9]', '', i)
        if l == size and n < size:
            l = 0
            n += 1
        if tmp.isdigit():
            npgrid[n][l] = int(tmp)
            l += 1
    return npgrid

def base_travel_cost(grid, ideal_grid, nb):
    tmpx, tmpy = utils.get_0_pos(grid)
    x = 0; y = 0
    move = 0
    for i in range(len(ideal_grid)):
        for j in range(len(ideal_grid[i])):
            if ideal_grid[i][j] == nb:
                x = i - tmpx ; y = j - tmpy
                move = abs(x) + abs(y)
                return move

def call_heuristic(dico, grid, h_type, ideal_grid, nb):
	"""Determine quelle fonction heuristique a utiliser"""
	npgrid = list_to_nparray(grid, dico['size'])
	npideal = list_to_nparray(ideal_grid, dico['size'])
	if "hamming" in h_type:
		return h_hamming(dico, npgrid, npideal), base_travel_cost(npgrid, npideal, nb)
	elif "manhattan" in h_type:
		return h_manhattan(dico, npgrid, npideal), base_travel_cost(npgrid, npideal, nb)
	elif "linear_conflict" in h_type:
		return h_linear_conflict(dico, npgrid, npideal), base_travel_cost(npgrid, npideal, nb)

def	check_conflict(grid, ideal_grid, i, j):
	tmp_grid = deepcopy(grid)
	tmp_grid[i][j] = ideal_grid[i][j]
	if tmp_grid[i][j] == ideal_grid[i][j]:
		return True
	#print(grid[i][j], ideal_grid[i][j], '\n', grid, '\n', ideal_grid)
	return False

def h_manhattan(dico, grid, ideal_grid):
	size = dico["size"]
	manhattan = 0
	for i in range(size):
		for j in range(size):
			if grid[i][j] != ideal_grid[i][j]:
				manhattan += base_travel_cost(grid, ideal_grid, grid[i][j])
	return manhattan

def h_linear_conflict(dico, grid, ideal_grid):
	size = dico["size"]
	linear_conflict = 0
	nb_conflicts = 0
	for i in range(size):
		for j in range(size):
			if grid[i][j] != ideal_grid[i][j]:
				linear_conflict += base_travel_cost(grid, ideal_grid, grid[i][j])
				if check_conflict(grid, ideal_grid, i, j) is True:
					nb_conflicts += 1
	return linear_conflict + (nb_conflicts * 2)

def h_hamming(dico, grid, ideal_grid):
    size = dico["size"]
    hamming = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if ideal_grid[i][j] != grid[i][j] and grid[i][j] != 0:
                hamming[i][j] = 1
    h_ham = sum(sum(hamming))
    #print("Hamming heuristic atm is : " + str(h_ham))
    return h_ham

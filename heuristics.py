def static_additive_patern_database(grid):
    patern_grid = [[], [], []]
    return pater_grid

def h_manhattan():
    print("manhattan not done")
    return

    def h_linear_conflict():
    print("linear conflict not done")
    return

def h_hamming():
    print("hamming not done")
    return
        """tosolve = np.array(([8, 4, 5, 10], [11, 13, 12, 16], [3, 0 , 1, 14], [7, 2, 6, 15]))
        a_size = int(np.sqrt(tosolve.size))
        solution = np.zeros((a_size, a_size), dtype=int)
        i = 0
        j = 0
        n = 1
        a = 0
        b = 1
        cpy = a_size
        while n < tosolve.size:
            while i < cpy - a:
                solution[j][i] = n
                n += 1
                i += 1
            i -= 1
            j += 1
            while j < cpy - a:
                solution[j][i] = n
                n += 1
                j += 1
            j -= 1
            while i >= 0 + a:
                solution[j][i] = n
                n += 1
                i -= 1
            i += 1
            j -= 1
            a += 1
            while j >= 0 + a:
                solution[j][i] = n
                n += 1
                j -= 1
            a += 1
            n += 1
        print(solution)
        hamming = np.zeros((a_size, a_size), dtype=int)
        for i in range(a_size):
            for j in range(a_size):
                if solution[i][j] == tosolve[i][j] and tosolve[i][j] != 0:
                    hamming[i][j] = 1
        print(sum(sum(hamming)))"""

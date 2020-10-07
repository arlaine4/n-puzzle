import numpy as np
import re

def spiral_cw(A):
    A = np.array(A)
    out = []
    while(A.size):
        out.append(A[0])        # take first row
        A = A[1:].T[::-1]       # cut off first row and rotate counterclockwise
    return np.concatenate(out)

def base_spiral(nrow, ncol):
    return spiral_cw(np.arange(nrow*ncol).reshape(nrow,ncol))[::-1]

def to_spiral(A):
    A = np.array(A)
    B = np.empty_like(A)
    B.flat[base_spiral(*A.shape)] = A.flat
    return B

def from_spiral(A):
    A = np.array(A)
    return A.flat[base_spiral(*A.shape)].reshape(A.shape)

if __name__ == "__main__":
    size = 10
    A = np.arange(size**2).reshape(size,size)
    A += 1
    A[size-1][size-1] = 0
    test = []
    for i in range(size):
        for j in range(size):
            test.append(A[i][j])
    npgrid = np.zeros((size, size), dtype=int)
    l = 0
    n = 0
    for i in reversed(test):
        tmp = i
        if l == size and n < size:
            l = 0
            n += 1
        npgrid[n][l] = int(tmp)
        l += 1
    out = to_spiral(npgrid)
    print(test, '\n\n', npgrid,'\n\n', out)


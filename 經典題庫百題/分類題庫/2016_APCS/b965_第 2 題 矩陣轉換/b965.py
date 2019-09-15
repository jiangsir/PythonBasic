# b965: 第 2 題 矩陣轉換

import sys, random

row, col = 5, 10
matrix = [[random.randint(0,99) for i in range(col)] for j in range(row)]

def rotate(matrix):
    print('rotate')
    rmatrix = [[0 for i in range(row)] for j in range(col)]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            rmatrix[c][r] = matrix[r][c]
    return rmatrix

def flip(fmatrix):
    print('flip')
    for i in range(len(matrix)//2):
        temprow = fmatrix[i]
        fmatrix[i] = fmatrix[-(i+1)]
        fmatrix[-(i+1)] = temprow
    return fmatrix

def printMatrix(matrix):
    print('-----------------------------------')
    for row in matrix:
        print(row)


printMatrix(matrix)
fmatrix = flip(matrix)
printMatrix(fmatrix)

rmatrix = rotate(matrix)
printMatrix(rmatrix)



N, M = input().split()

def count1(matrix, x, y):
    '''
    計算 1 的個數
    '''
    count = 0
    for i in range(len(matrix[0])):
        if matrix[x][i] == 1:
            count += 1
    for i in range(len(matrix)):
        if matrix[i][y] == 1 and i!=x:
            count += 1
    return count

matrix1 = []
for i in range(int(N)):
    matrix1.append([int(x) for x in input().split()])

matrix2 = []
for i in range(int(N)):
    matrix2.append([int(x) for x in input().split()])

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if count1(matrix2, i, j) %2 == 1:
            matrix1[i][j] = 1-matrix1[i][j]

for row in matrix1:
    print(*row)
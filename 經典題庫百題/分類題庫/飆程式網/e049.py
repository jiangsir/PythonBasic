n, m = map(int, input().split())

matrix = [ [int(x) for x in input().split()] for i in range(n)]



def transpose1(matrix):
    '''
    其他語言的解法
    '''
    newmatrix = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newmatrix[j][i] = matrix[i][j]

    for row in newmatrix:
        print(*row)

def transpose2(matrix):
    '''
    使用列表推導式
    '''
    rmatrix = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
    for row in rmatrix:
        print(*row)
    


def transpose3(matrix):
    '''
    使用 zip
    '''
    zipped = zip(*matrix)
    for row in list(zipped):
        print(*row)


#print('原始 matrix:', matrix)
#print('轉置 matrix:')
transpose1(matrix)

#source code: 4662313 
# author: peatman5566
#

while True:
    try:
        m, n = [int(str) for str in input().split()]
    except:
        break
    
    A = []
    for i in range(m):
        B = [int(str) for str in input().split()]
        A.append(B)
    
    D = A[:][:]
    for i in range(m):
        for j in range(1, n):
            if A[i][j]:
                D[i][j] = D[i][j-1] + A[i][j]
        
    #print_2D(D)
    max_area = 0
    for i in range(m):
        for j in range(1, n):
            height = 2
            area = width = D[i][j]
            while (i-height+1) > -1:
                width = min(width, D[i-height+1][j])
                area = max(area, width*height)
                height += 1
            max_area = max(max_area, area)

    print(max_area)
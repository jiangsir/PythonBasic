'''
#矩陣 #矩陣乘法

'''
def mxdot1(mx1, mx2):
    zip_b = zip(*mx2)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in mx1]

def linedot(l1, l2):
    sum = 0
    for i, l in enumerate(l1):
        sum += l* l2[i]
    return sum

def mxdot2(mxa, mxb):
    ar = len(mxa)
    bc = len(mxb[0])
    mxc = [[0 for _ in range(bc)] for _ in range(ar)]
    #print('mxc=', mxc)
    for row in range(ar):
        #print('row=', row, 'mxa[row]=', mxa[row])
        for col in range(bc):
            mxc[row][col] = linedot(mxa[row], list(zip(*mxb))[col])

    return mxc


#ar, ac, br, bc = map(int, input().split())
N = int(input())
ar = ac = br = bc = N

mx1 = [[int(x) for x in input().split()] for i in range(ar)]

mx2 = [[int(x) for x in input().split()] for i in range(br)]


#print('mx1=', mx1, 'mx2=', mx2)

mxc = mxdot2(mx1, mx2)

for line in mxc:
    print(*line)
